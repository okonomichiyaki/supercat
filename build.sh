#!/bin/zsh

# run preprocessor (gpp) on every md file, output to /tmp
# gpp filters out campaign-only and base-only text blocks
# uses ifdef/endif tags (-H flag indicates HTML style tags)
for f in *.md; do
    gpp -o "/tmp/$f" -H $1 $f
done

# cleanup prior build:
rm output.html

# run pandoc over the specific list of pages/sections, in the specified order:
cat pages.txt |
    while read line; do echo /tmp/${line}; done |
    xargs pandoc -s --css=pandoc.css --metadata title=SUPERCAT -o output.html
