#!/bin/zsh

pandoc -s --css=pandoc.css \
       00-how\ to\ play\ with\ SUPERCAT.md \
       00-questions.md \
       01-bot\ turn\ start\ here.md \
       02-general\ priorities.md \
       03-prelude.md \
       04-administration.md \
       05-aggression.md \
       06-combat\ doctrine.md \
       07-construction.md \
       08-mobilization.md \
       10-terminology.md \
       -o output.html
