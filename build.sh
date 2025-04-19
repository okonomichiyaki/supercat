#!/bin/zsh

for f in *.md; do
    gpp -o "/tmp/$f" -H $1 $f
done

pandoc -s --css=pandoc.css --metadata title=SUPERCAT \
       /tmp/000-SUPERCAT.md \
       /tmp/010-campaign.md \
       /tmp/010-F01-steward.md \
       /tmp/010-F02-founder.md \
       /tmp/010-F03-magnate.md \
       /tmp/010-F04-advocate.md \
       /tmp/010-F05-caretaker.md \
       /tmp/010-F06-partisan.md \
       /tmp/010-F07-admiral.md \
       /tmp/010-F08-believer.md \
       /tmp/020-bot\ turn\ start\ here.md \
       /tmp/030-general\ priorities.md \
       /tmp/040-prelude.md \
       /tmp/050-administration.md \
       /tmp/051-influence-doctrine.md \
       /tmp/060-aggression.md \
       /tmp/061-combat\ doctrine.md \
       /tmp/070-construction.md \
       /tmp/080-mobilization.md \
       /tmp/081-movement-doctrine.md \
       /tmp/091-vox-cards.md \
       /tmp/092-leaders-and-lore.md \
       /tmp/093-questions.md \
       /tmp/094-clarifications.md \
       /tmp/095-terminology.md \
       -o output.html
