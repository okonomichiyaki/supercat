import sys
import csv

campaign = True

suits = {
    'Administration': ["Tax", "Repair", "Influence"],
    'Aggression': ["Move", "Battle", "Secure"],
    'Construction': ["Build", "Repair"],
    'Mobilization': ["Move", "Influence"],
}

terms = ["claim",
"combat card",
"contend",
"contested card",
"double city",
"effective",
"favorable combat",
"new resources",
"partial move",
"task force",
"unbuilt city",
"unclaimed",
"uncontested card",
"undeclared ambition"]

def indent(s, n):
    for i in range(0, n):
        s = "\t" + s
    return s

def priority_comment(p):
    return f"<!-- priority={p} -->"

def build_statement(row):
    cond = row['Condition']
    pref = row['Prefer']
    action = row['Action']
    article = row['article']
    goal = row['Goal']
    thing = f"{article} {goal}"
    i = 0
    quest = f"Can bot {action} {thing}?"
    s = ""
    p = row['Priority']
    pcomment = ""
    if p != "" and p != "99":
        pcomment = priority_comment(p)
    if (cond != ""):
        s = f"✦ {pcomment} {cond}\n\n"
        s = s + f"- {quest}\n"
    else:
        s = f"✦ {pcomment} {quest}\n"
    if pref != "":
        s = s + "\n"
        s = s + indent("- Prefer:\n", i)
        i = i + 1
        ps = [ indent(f"- {p.strip()}", i) for p in pref.split(";")]
        s = s + "\n".join(ps)
    return s

def merge(rows):
    action = rows[0]['Action']
    pcomment = priority_comment(rows[0]['Priority'])
    things = [f"{row['article']} {row['Goal']}" for row in rows]
    if len(things) > 2:
        things = ", ".join(things[0:len(things)-1]) + f", or {things[-1]}"
    else:
        things = f"{things[0]} or {things[1]}"
    return f"✦ {pcomment} Can bot {action} {things}?"

def mergeable(a, b):
    return a['Priority'] == b['Priority'] and a['Action'] == b['Action'] and a['Condition'] == "" and b['Condition'] == "" and a['Prefer'] == "" and b['Prefer'] == ""

def cleanup(s):
    s = s.replace("  ", " ")
    s = s.replace("Battle", "favorable combat")
    for t in terms:
        s = s.replace(t, f"<ins>{t}</ins>")
    return s.strip()

suit = sys.argv[1]
filename = sys.argv[2]

actions = " | ".join(suits[suit])
print(f"# {suit} - {actions}\n\n", end="")

idx = 0
stmts = []
with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row[suit] == '◉' and (row['Campaign'] == "" or row['Campaign'] == "x" and campaign):
            if idx > 0 and mergeable(stmts[idx-1][1][0], row):
                rows = stmts[idx-1][1] + [row]
                stmts[idx-1] = (merge(rows), rows)
            else:
                stmt = build_statement(row)
                stmts = stmts + [(stmt, [row])]
                idx = idx + 1
    print("\n\n".join([ cleanup(s[0]) for s in stmts ]), end="")
