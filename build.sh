#!/bin/zsh

pandoc -s --css=pandoc.css --metadata title=SUPERCAT \
       00-SUPERCAT.md \
       00-terminology.md \
       01-bot\ turn\ start\ here.md \
       02-general\ priorities.md \
       03-prelude.md \
       04-administration.md \
       05-aggression.md \
       06-combat\ doctrine.md \
       07-construction.md \
       08-mobilization.md \
       99-clarifications.md \
       -o output.html
