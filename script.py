import sys
import csv

campaign = True

suits = {
    'Administration': ["Tax", "Repair", "Influence"],
    'Aggression': ["Move", "Battle", "Secure"],
    'Construction': ["Build", "Repair"],
    'Mobilization': ["Move", "Influence"],
}

terms = [
    # "unclaimed",
    # "claims",
    "claim",

    "uncontested card",
    "contested card",

    "unbuilt cities",
    "unbuilt city",

    "combat card",
    "contend",
    "double city",
    "effective",
    "favorable combat",
    "new resources",
    "partial move",
    "task force",
    "undeclared ambition"
]

def indent(s, n):
    for i in range(0, n):
        s = "\t" + s
    return s

def priority_comment(p):
    if p != "" and p != "99":
        return f"<!-- priority={p} -->"
    else:
        return ""

def build_statement(row):
    cond = row['Condition']
    pref = row['Prefer']
    action = row['Action']
    glue = row['GlueWord']
    goal = row['Goal']
    thing = f"{glue} {goal}"
    i = 0
    quest = f"Can bot {action} {thing}?"
    lines = []
    p = row['Priority']
    pcomment = priority_comment(p)
    if cond != "":
        lines.append(f"✦ {cond}")
        lines.append("")
        lines.append(f"- {pcomment} {quest}")
    else:
        lines.append(f"✦ {pcomment} {quest}")
    if pref != "":
        if lines[-1].startswith("✦"):
            lines.append("")
        ctx = ""
        if row['PreferContext'] != "":
            ctx = f" {row['PreferContext']}"
        lines.append(indent(f"- Prefer{ctx}:", i))
        i = i + 1
        ps = [ indent(f"- {p.strip()}", i) for p in pref.split(";")]
        lines = lines + ps
    return "\n".join(lines)

def merge_goals(rows):
    action = rows[0]['Action']
    pcomment = priority_comment(rows[0]['Priority'])
    things = [f"{row['GlueWord']} {row['Goal']}" for row in rows]
    if len(things) > 2:
        things = ", ".join(things[0:len(things)-1]) + f", or {things[-1]}"
    else:
        things = f"{things[0]} or {things[1]}"
    return f"✦ {pcomment} Can bot {action} {things}?"

def merge_actions(rows):
    cond = rows[0]['Condition']
    pref = rows[0]['Prefer']
    actions = [row['Action'] for row in rows]
    actions = " or ".join(actions)
    pcomment = priority_comment(rows[0]['Priority'])
    thing = f"{rows[0]['GlueWord']} {rows[0]['Goal']}"
    quest = f"Can bot {actions} {thing}?"
    lines = []
    if cond != "":
        lines.append(f"✦ {cond}")
        lines.append("")
        lines.append(f"- {pcomment} {quest}")
    else:
        lines.append(f"✦ {pcomment} {quest}")
    if pref != "":
        if lines[-1].startswith("✦"):
            lines.append("")
        ctx = ""
        if row['PreferContext'] != "":
            ctx = f" {row['PreferContext']}"
        lines.append(f"- Prefer{ctx}:")
        ps = [ indent(f"- {p.strip()}", 1) for p in pref.split(";")]
        lines = lines + ps

    return "\n".join(lines)

def both_blank(a, b, k):
    return a[k] == "" and b[k] == ""

def equals(a, b, k):
    return a[k] == b[k]

def same_priority_and_action(a, b):
    return equals(a, b, 'Priority') and equals(a, b, 'Action') and both_blank(a, b, 'Condition') and both_blank(a, b, 'Prefer')

def same_priority_goal_cond(a, b):
    return equals(a, b, 'Priority') and equals(a, b, 'Goal') and equals(a, b, 'Condition') and equals(a, b, 'Prefer')

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
            if idx > 0 and same_priority_and_action(stmts[idx-1][1][0], row):
                rows = stmts[idx-1][1] + [row]
                stmts[idx-1] = (merge_goals(rows), rows)
            elif idx > 0 and same_priority_goal_cond(stmts[idx-1][1][0], row):
                rows = stmts[idx-1][1] + [row]
                stmts[idx-1] = (merge_actions(rows), rows)
            else:
                stmt = build_statement(row)
                stmts = stmts + [(stmt, [row])]
                idx = idx + 1
    print("\n\n".join([ cleanup(s[0]) for s in stmts ]), end="")
    print("\n<div class=\"pagebreak\"> </div>", end="\n")
