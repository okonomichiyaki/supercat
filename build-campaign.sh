#!/bin/zsh

pandoc -s --css=pandoc.css --metadata title=SUPERCAT \
       00z-campaign.md \
       00z-F01-steward.md	\
       00z-F02-founder.md \
       00z-F03-magnate.md	\
       00z-F04-advocate.md	\
       00z-F05-caretaker.md	\
       00z-F07-admiral.md \
       00z-F06-partisan.md	\
       00z-F08-believer.md \
       -o output.html
