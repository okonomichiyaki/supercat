import sys
import csv

suits = {
    'Administration': ["Tax", "Repair", "Influence"],
    'Aggression': ["Move", "Battle", "Secure"],
    'Construction': ["Build", "Repair"],
    'Mobilization': ["Move", "Influence"],
}

def flatten(xss):
    return [x for xs in xss for x in xs]

def get_suits(row):
    result = []
    for k in suits:
        if row[k] == '◉':
            result.append(k)
    return result

def build_name(name, row, idx, offset=0):
    letter = chr(ord('A') + idx)
    return f"{name}-{int(row['Id']) + offset}-{letter}"

def build_link(label, dest):
    return f"[[{label}->{dest}]]"

def build_passage(name, question, yes, no):
    return [
        f":: {name}",
        question,
        f"* {yes}",
        f"* {no}"
    ]

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

print("""
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
* [[General Priorities->GeneralPriorities-1-A]]

""")

filename = sys.argv[1]
passages = []
with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        passages = build_passages("GeneralPriorities", row)
        for passage in passages:
            for line in passage:
                print(line)
            print()
