import sys
import csv
import re
import argparse
import gspread

campaign = True

suits = {
    'Administration': {
        "output": "050-administration.md",
        "actions": ["Tax", "Repair", "Influence"]
    },
    'Aggression': {
        "output": "060-aggression.md",
        "actions": ["Move", "Battle", "Secure"]
    },
    'Construction': {
        "output": "070-construction.md",
        "actions": ["Build", "Repair"],
    },
    'Mobilization': {
        "output": "080-mobilization.md",
        "actions": ["Move", "Influence"]
    }
}

terms = [
    "claimed",
    "unclaimed",
    "claims",
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

def replacer(match):
    return f"<ins>{match.group(0)}</ins>"

pattern = r'\b(' + '|'.join(terms) + r')\b'
def highlight_terms(text):
    p = re.compile(pattern)
    return p.sub(replacer, text)

def indent(s, n):
    for i in range(0, n):
        s = "\t" + s
    return s

def priority_comment(p):
    if p != "" and p != "99":
        return f"<!-- priority={p} -->"
    else:
        return ""

def wrap_ifdef(row, stmt):
    if row['Campaign'] == "x":
        return f"<#ifdef campaign>\n{stmt}\n<#endif>"
    elif row['Base'] == "x":
        return f"<#ifdef base>\n{stmt}\n<#endif>"
    else:
        return stmt

def add_pref(row, lines):
    pref = row['Prefer']
    if pref != "":
        ctx = ""
        if row['PreferContext'] != "":
            ctx = f" {row['PreferContext']}"
        lines[-1] = lines[-1] + f" Prefer{ctx}:"
        i = 0
        if lines[-1].startswith("✦"):
            lines.append("")
        else:
            i = 1
        ps = [ indent(f"- {p.strip()}", i) for p in pref.split(";")]
        lines = lines + ps
    return lines

def ids(rows):
    i = ",".join([ row['Id'] for row in rows ])
    i = f"<span style=\"font-size: 12px;\">({i})</span>"
    return i

def build_statement(row):
    cond = row['Condition']
    pref = row['Prefer']
    action = row['Action']
    glue = row['GlueWord']
    goal = row['Goal']
    thing = f"{glue} {goal}"
    i = 0
    id_ = ids([row])
    quest = f"Can bot {action} {thing}? {id_}"
    lines = []
    p = row['Priority']
    pcomment = priority_comment(p)
    if cond != "":
        lines.append(f"✦ {cond}")
        lines.append("")
        lines.append(f"- {pcomment} {quest}")
    else:
        lines.append(f"✦ {pcomment} {quest}")
    lines = add_pref(row, lines)
    stmt = "\n".join(lines)
    return wrap_ifdef(row, stmt)

def merge_goals(rows):
    id_ = ids(rows)
    action = rows[0]['Action']
    pcomment = priority_comment(rows[0]['Priority'])
    things = [f"{row['GlueWord']} {row['Goal']}" for row in rows]
    if len(things) > 2:
        things = ", ".join(things[0:len(things)-1]) + f", or {things[-1]}"
    else:
        things = f"{things[0]} or {things[1]}"
    stmt = f"✦ {pcomment} Can bot {action} {things}? {id_}"
    return wrap_ifdef(rows[0], stmt)

def merge_actions(rows):
    id_ = ids(rows)
    cond = rows[0]['Condition']
    actions = [row['Action'] for row in rows]
    actions = " or ".join(actions)
    pcomment = priority_comment(rows[0]['Priority'])
    thing = f"{rows[0]['GlueWord']} {rows[0]['Goal']}"
    quest = f"Can bot {actions} {thing}? {id_}"
    lines = []
    if cond != "":
        lines.append(f"✦ {cond}")
        lines.append("")
        lines.append(f"- {pcomment} {quest}")
    else:
        lines.append(f"✦ {pcomment} {quest}")
    lines = add_pref(rows[0], lines)
    stmt = "\n".join(lines)
    return wrap_ifdef(rows[0], stmt)

def both_blank(a, b, k):
    return a[k] == "" and b[k] == ""

def equals(a, b, k):
    return a[k] == b[k]

def same_priority_and_action(a, b):
    return equals(a, b, 'Campaign') and equals(a, b, 'Base') and equals(a, b, 'Priority') and equals(a, b, 'Action') and both_blank(a, b, 'Condition') and both_blank(a, b, 'Prefer')

def same_priority_goal_cond(a, b):
    return equals(a, b, 'Campaign') and equals(a, b, 'Base') and equals(a, b, 'Priority') and equals(a, b, 'Goal') and equals(a, b, 'Condition') and equals(a, b, 'Prefer')

def cleanup(s):
    s = s.replace("  ", " ")
    s = s.replace("Battle", "favorable combat")
    s = highlight_terms(s)
    return s.strip()

def get_rows(filename):
    result = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)
    return result

def main():
    parser = argparse.ArgumentParser(
        prog='SUPERCAT',
        description='convert google sheet to markdown procedures')
    parser.add_argument('-c', '--campaign', action='store_true')
    args = parser.parse_args()
    campaign = args.campaign
    filename = '/tmp/supercat.csv'

    print("downloading gsheet...", end="")
    gc = gspread.oauth()
    sh = gc.open("SUPERCAT")
    bytes_ = sh.export(gspread.utils.ExportFormat.CSV)
    with open(filename, 'wb') as f:
        f.write(bytes_)
    print("done.")

    all_rows = get_rows(filename)
    filtered = [ row for row in all_rows if row['Hide'] != "x" ]
    print(f"all rows: {len(all_rows)} filtered rows: {len(filtered)}")
    for suit in suits:
        actions = " | ".join(suits[suit]["actions"])
        output = suits[suit]["output"]
        idx = 0
        stmts = []
        rows = [ row for row in filtered if row[suit] == '◉' ]
        print(f"got {len(rows)} rows for {suit}")
        print(f"generating {suit}", end="")
        for row in rows:
            print(".", end="")
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
        with open(output, 'w') as outf:
            outf.write(f"# {suit} - {actions}\n\n")
            outf.write("\n\n".join([ cleanup(s[0]) for s in stmts ]))
            outf.write("\n\n<div class=\"pagebreak\"> </div>\n")
        print(" done.")

if __name__ == "__main__":
    main()
