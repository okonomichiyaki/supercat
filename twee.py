from __future__ import annotations # https://stackoverflow.com/a/33533514
import sys
import csv
from dataclasses import dataclass
import re

preamble = """
:: StoryTitle
SUPERCAT

:: StoryData
{
  "ifid": "83E66060-E0EF-4EFB-B682-3797FCB59892",
  "format": "Harlowe",
  "format-version": "3.3.9",
  "start": "Start Here",
  "zoom": 1
}

:: Start Here
* [[General Priorities->GeneralPriorities-1]]

"""

suits = {
    'Administration': ["Tax", "Repair", "Influence"],
    'Aggression': ["Move", "Battle", "Secure"],
    'Construction': ["Build", "Repair"],
    'Mobilization': ["Move", "Influence"],
}
keys = ['Name', 'Question', 'Yes', 'No']

def flatten(xss):
    return [x for xs in xss for x in xs]

def get_suits(row):
    result = []
    for k in suits:
        if row[k] == '◉':
            result.append(k)
    return result

def build_question(row):
    return f"Can bot {row['Action']} {row['GlueWord']} {row['Goal']}?"

def build_name(name, row, idx, offset=0):
    letter = chr(ord('A') + idx)
    return f"{name}-{int(row['Id']) + offset}-{letter}"

def build_link(label, dest):
    return f"[[{label}->{dest}]]"

def build_passage(name, question, yes, no):
    return {
        'Name': f":: {name}",
        'Question': question,
        'Yes': f"* {yes}",
        'No': f"* {no}"
    }

def build_passages(title, row):
    result = []
    idx = 0
    body = ""
    if row['Condition'] != '':
        name = build_name(title, row, idx)
        idx = idx + 1
        question = row['Condition']
        yes = build_link("Yes", build_name(title, row, idx))
        no = build_link("No", build_name(title, row, 0, 1))
        result.append(build_passage(name, question, yes, no))
    name = build_name(title, row, idx)
    question = f"Can bot {row['Action']} {row['GlueWord']} {row['Goal']}?"
    suits = get_suits(row)
    yes = " or ".join([ build_link(suit, suit) for suit in suits ])
    yes = f"Yes: {yes}"
    no = f"{build_link('No', build_name(title, row, 0, 1))}"
    result.append(build_passage(name, question, yes, no))
    return result


@dataclass
class Node:
    id: str
    title: str
    type: str
    suits: list[str]
    question: str
    prefer_context: str
    prefer: str
    priority: float
    next: Node = None
    hide: bool = False

    def name(self):
        return f"{self.title}-{self.id}"

    def to_passage(self):
        # TODO passage we link from each suit should be SUIT-ID, where ID is the current id
        suits = [ f"[[{suit}->{suit}]]" for suit in self.suits ]
        branch_suits = " or ".join(suits)
        branch_next = ""
        branch_next_next = ""
        if self.next:
            branch_next = self.next.name()
        if self.next and self.next.next:
            branch_next_next = self.next.next.name()

        yes = ""
        no = ""
        if self.type == "action":
            yes = f"* Yes: {branch_suits}"
            no = f"* [[No->{branch_next}]]"
        elif self.type == "condition":
            yes = f"* [[Yes->{branch_next}]]"
            no = f"* [[No->{branch_next_next}]]"

        return "\n".join([
            f":: {self.name()}",
            self.question,
            yes,
            no
        ])

    def nextnext(self):
        if self.next and self.next.next:
            return self.next.next
        else:
            return None

    def is_simple(self):
        return re.match('\d+\-[A-Z]', self.id) == None

    def is_not_simple(self):
        return not self.is_simple()

    def __repr__(self):
        next = None
        if self.next:
            next = self.next.id
        return f"Node(id={self.id}, t={self.type}, q={self.question}, next={next})"

def build_node(title, row, type="action", letter=None):
    id = row['Id']
    if letter:
        id = f"{id}-{letter}"
    return Node(
        id,
        title,
        type,
        get_suits(row),
        build_question(row),
        row['PreferContext'],
        row['Prefer'],
        float(row['Priority'])
    )

def build_cond_node(title, row, letter=None):
    node = build_node(title, row, "condition", letter)
    node.question = row['Condition']
    return node

def nodes_from_file(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        prev = None
        head = None
        for row in reader:
            if row['Condition'] == '':
                node = build_node("GeneralPriorities", row)
                if prev:
                    prev.next = node
                else:
                    head = node
                prev = node
            else:
                n1 = build_cond_node("GeneralPriorities", row, 'A')
                n2 = build_node("GeneralPriorities", row, letter='B')
                n1.next = n2
                if prev:
                    prev.next = n1
                else:
                    head = n1
                prev = n2
        return head

def print_nodes(head):
    n = head
    while n:
        print(n)
        n = n.next

def print_passages(head):
    n = head
    while n:
        print(n.to_passage())
        print()
        n = n.next

def mergeable(a, b):
    return a.is_not_simple() and b.is_not_simple() and a.question == b.question and a.priority == b.priority

def merge_nodes(head):
    n = head
    while n:
        if n.is_simple():
            n = n.next
        else:
            n0 = n
            p = n0.next
            m = n.nextnext()
            # check if the next-next node can be merged
            while p and m and mergeable(n0, m):
                # if they can be, merge by skipping over the next-next node:
                p.next = m.next
                p = m.next
                m = m.nextnext()
            n = p

def main():
    filename = sys.argv[1]
    passages = []
    head = nodes_from_file(filename)
    merge_nodes(head)
#    print_nodes(head)
    print(preamble)
    print_passages(head)

main()
