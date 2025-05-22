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
    for suit in SUITS:
        print(f"<ul class=\"{suit}\">")
        rows = [ row for row in filtered if row[suit] == BULLET ]
        for row in rows:
            priority = int(row["Priority"])
            shorter = row["Shorter"]
            if priority < 99:
                print(f"<li>[{priority}] {shorter}</li>")
        print(f"</ul>")

if __name__ == "__main__":
    main()
