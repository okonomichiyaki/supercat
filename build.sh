#!/bin/zsh

# run preprocessor (gpp) on every md file, output to /tmp
# gpp filters out campaign-only and base-only text blocks
# uses ifdef/endif tags (-H flag indicates HTML style tags)
for f in *.md; do
    gpp -o "/tmp/$f" -H $1 $f
done

# cleanup prior build:
rm output.html

# wrap terminology with tags:
for file in `cat pages.md`; do
    if [[ $file != "095-terminology.md" ]]; then
        while IFS= read -r phrase; do
            escaped=$(printf '%s\n' "$phrase" | sed 's/[][\.*^$/]/\\&/g')
            perl -i -pe '
      BEGIN {
        $phrase = shift;
      }
      s{
        (?<!<ins>)           # no tag open before
        \b\Q'"$phrase"'\E\b  # exact word match
        (?!<\/ins>)          # no tag close after
      }{<ins>$&</ins>}igx;
          ' "$escaped" "/tmp/$file"
        done < "terminology.txt"
    fi
done

# run pandoc over the specific list of pages/sections, in the specified order:
cat pages.md |
    while read line; do echo /tmp/${line}; done |
    xargs pandoc -s --css=pandoc.css --metadata title=SUPERCAT -o output.html
