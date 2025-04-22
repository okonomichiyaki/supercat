import sys
import csv

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

def build_statement(row):
    i = 0
    q = f"Can bot {row['Action']} {row['article']} {row['Goal']}?"
    s = ""
    priority = ""
    if (row['Priority'] != "" and row['Priority'] != "99"):
        priority = f"<!-- priority={row['Priority']} -->"
    if (row['Condition'] != ""):
        s = f"✦ {priority} {row['Condition']}\n\n"
        s = s + f"- {q}\n"
    else:
        s = f"✦ {priority} {q}\n"
    if (row['Prefer'] != ""):
        s = s + "\n"
        s = s + indent("- Prefer:\n", i)
        i = i + 1
        ps = [ indent(f"- {p.strip()}", i) for p in row['Prefer'].split(";")]
        s = s + "\n".join(ps)
    return s

suit = sys.argv[1]
filename = sys.argv[2]

actions = " | ".join(suits[suit])
print(f"# {suit} - {actions}\n\n", end="")

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row[suit] == '◉'):
            stmt = build_statement(row)
            stmt = stmt.replace("  ", " ")
            stmt = stmt.strip()
            stmt = f"{stmt}\n\n"
            for term in terms:
                stmt = stmt.replace(term, f"<ins>{term}</ins>")
            print(stmt, end="")
