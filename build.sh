#!/bin/zsh

for f in *.md; do
    gpp -o "/tmp/$f" -H $1 $f
done

rm output.html

cat pages.txt | while read line; do echo /tmp/${line}; done | xargs pandoc -s --css=pandoc.css --metadata title=SUPERCAT -o output.html
