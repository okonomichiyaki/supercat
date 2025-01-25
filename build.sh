#!/bin/zsh

pandoc -s --css=pandoc.css --metadata title=SUPERCAT \
       00-SUPERCAT.md \
       00-terminology.md \
       01-bot\ turn\ start\ here.md \
       02-general\ priorities.md \
       03-prelude.md \
       04-administration.md \
       04-influence-doctrine.md \
       05-aggression.md \
       06-combat\ doctrine.md \
       07-construction.md \
       08-mobilization.md \
       96-vox-cards.md \
       97-leaders-and-lore.md \
       98-questions.md \
       99-clarifications.md \
       -o output.html
