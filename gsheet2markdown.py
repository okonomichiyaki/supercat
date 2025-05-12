import sys
import csv
import re
import argparse
import gspread

BULLET = '✦'

SUITS = {
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

def get_suits(rows):
    actions = []
    result = []
    for row in rows:
        actions.append(row["Action"])
        for suit in SUITS:
            if row[suit] ==  BULLET:
                result.append(suit)
    if actions == ["Battle"] and result == ["Aggression"]:
        return ["Combat card"]
    return list(set(result))

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

def get_flagship(row):
    if row['No Flagship'] == 'x':
        return "(ignore for Flagship)"
    elif row['Flagship'] == 'x':
        return "(Flagship only)"
    return ""

def build_statement(row, general=False):
    fs = get_flagship(row)
    cond = row['Condition']
    pref = row['Prefer']
    action = row['Action']
    glue = row['GlueWord']
    goal = row['Goal']
    if action == "":
        return wrap_ifdef(row, BULLET + " " + goal)
    thing = f"{glue} {goal}"
    i = 0
    id_ = ids([row])
    quest = f"Can bot {action} {thing}? {id_}"
    lines = []
    p = row['Priority']
    pcomment = priority_comment(p)
    if cond != "":
        lines.append(f"✦ {fs} {cond}")
        lines.append("")
        lines.append(f"- {pcomment} {quest}")
    else:
        lines.append(f"✦ {fs} {pcomment} {quest}")
    if general:
        lines[-1] = lines[-1] + " → " + "/".join(get_suits([row]))
    else:
        lines = add_pref(row, lines)
    stmt = "\n".join(lines)
    return wrap_ifdef(row, stmt)

def merge_goals(rows, general=False):
    id_ = ids(rows)
    print(f"merging goals: {id_}")
    action = rows[0]['Action']
    pcomment = priority_comment(rows[0]['Priority'])
    things = [f"{row['GlueWord']} {row['Goal']}" for row in rows]
    if len(things) > 2:
        things = ", ".join(things[0:len(things)-1]) + f", or {things[-1]}"
    else:
        things = f"{things[0]} or {things[1]}"
    stmt = f"✦ {pcomment} Can bot {action} {things}? {id_}"
    if general:
        stmt = stmt + " → " + "/".join(get_suits(rows))
    return wrap_ifdef(rows[0], stmt)

def merge_actions(rows, general=False):
    id_ = ids(rows)
    print(f"merging actions: {id_}")
    cond = rows[0]['Condition']
    actions = [row['Action'] for row in rows]
    actions = set(actions)
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
    if general:
        stmt = stmt + " → " + "/".join(get_suits(rows))
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
    s = s.replace("Battle", "favorable combat")
    return re.sub(r' +', ' ', s).strip()

def get_rows(filename):
    result = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)
    return result

def general_priorities(output, rows):
    filtered = [ row for row in rows if float(row['Priority']) < 99 ]
    print(f"generating General Priorities from {len(rows)} rows filtered to {len(filtered)} rows")
    stmts = []
    idx = 0
    for row in filtered:
        print(f"{row['Id']} - {row['Combined']}")
        if idx > 0 and same_priority_and_action(stmts[idx-1][1][0], row):
            rows = stmts[idx-1][1] + [row]
            stmts[idx-1] = (merge_goals(rows, True), rows)
        elif idx > 0 and same_priority_goal_cond(stmts[idx-1][1][0], row):
            rows = stmts[idx-1][1] + [row]
            stmts[idx-1] = (merge_actions(rows, True), rows, True)
        else:
            stmt = build_statement(row, True)
            stmts = stmts + [(stmt, [row])]
            idx = idx + 1
    with open(output, 'w') as outf:
        outf.write(f"# General Priorities\n\n")
        outf.write("\n\n".join([ cleanup(s[0]) for s in stmts ]))
        outf.write("\n\n<div class=\"pagebreak\"> </div>\n")

def main():
    parser = argparse.ArgumentParser(
        prog='SUPERCAT',
        description='convert google sheet to markdown procedures')
    parser.add_argument('-c', '--campaign', action='store_true')
    parser.add_argument('-a', '--api_key')
    parser.add_argument('-u', '--url')
    args = parser.parse_args()
    campaign = args.campaign
    api_key = args.api_key
    url = args.url
    filename = '/tmp/supercat.csv'

    print("downloading gsheet...", end="")
    gc = gspread.api_key(api_key)
    sh = gc.open_by_url(url)
    bytes_ = sh.export(gspread.utils.ExportFormat.CSV)
    with open(filename, 'wb') as f:
        f.write(bytes_)
    print("done.")

    all_rows = get_rows(filename)
    filtered = [ row for row in all_rows if row['Hide'] != "x" ]
    print(f"all rows: {len(all_rows)} filtered rows: {len(filtered)}")
    general_priorities("030-general-priorities.md", all_rows)
    for suit in SUITS:
        actions = " | ".join(SUITS[suit]["actions"])
        output = SUITS[suit]["output"]
        idx = 0
        stmts = []
        rows = [ row for row in filtered if row[suit] == BULLET ]
        print(f"got {len(rows)} rows for {suit}")
        print(f"generating {suit}", end="\n")
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
