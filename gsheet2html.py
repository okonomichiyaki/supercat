import sys
import csv
import re
import argparse
import gspread

BULLET = '✦'

SUITS = [
    'Administration',
    'Aggression',
    'Construction',
    'Mobilization'
]


def find_and_replace_in_file(filename, x, y):
    with open(filename, 'r') as f:
      old = f.read()
    new = old.replace(x, y)
    with open(filename, 'w') as f:
      f.write(new)

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
        description='convert google sheet to html for CIDEr card template')
#    parser.add_argument('-c', '--campaign', action='store_true')
    parser.add_argument('-a', '--api_key')
    parser.add_argument('-u', '--url')
    parser.add_argument('-f', '--file')
    args = parser.parse_args()
#    campaign = args.campaign
    api_key = args.api_key
    url = args.url
    filename = '/tmp/supercat.csv'

    gc = gspread.api_key(api_key)
    sh = gc.open_by_url(url)
    bytes_ = sh.export(gspread.utils.ExportFormat.CSV)
    with open(filename, 'wb') as f:
        f.write(bytes_)

    all_rows = get_rows(filename)
    filtered = [ row for row in all_rows if row['Hide'] != "x" and row["Campaign"] == "" ]
    uls = []
    for suit in SUITS:
        ul = [f"<ul class=\"{suit}\">"]
        rows = [ row for row in filtered if row[suit] == BULLET ]
        rows = rows[:12]
        for row in rows:
            priority = int(row["Priority"])
            shorter = row["Shorter"]
            ul += [f"<li>[{priority}] {shorter}</li>"]
        ul += ["</ul>"]
        uls += ["\n".join(ul)]
    html = "\n".join(uls)
    if args.file:
        find_and_replace_in_file(args.file, "XXX", html)
    else:
        print(html)

if __name__ == "__main__":
    main()
