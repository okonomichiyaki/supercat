#!/bin/zsh

for f in *.md; do
    gpp -o "/tmp/$f" -H $1 $f
done

pandoc -s --css=pandoc.css --metadata title=SUPERCAT \
       /tmp/00-SUPERCAT.md \
       /tmp/00z-campaign.md \
       /tmp/00-terminology.md \
       /tmp/01-bot\ turn\ start\ here.md \
       /tmp/02-general\ priorities.md \
       /tmp/03-prelude.md \
       /tmp/04-administration.md \
       /tmp/04-influence-doctrine.md \
       /tmp/05-aggression.md \
       /tmp/06-combat\ doctrine.md \
       /tmp/07-construction.md \
       /tmp/08-mobilization.md \
       /tmp/08-movement-doctrine.md \
       /tmp/96-vox-cards.md \
       /tmp/97-leaders-and-lore.md \
       /tmp/98-questions.md \
       /tmp/99-clarifications.md \
       -o output.html
