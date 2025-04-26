#!/bin/zsh

rm output.html
cp $2 /tmp/single.md
gpp -o /tmp/gpp-single.md -H $1 /tmp/single.md
pandoc -s --css=pandoc.css /tmp/gpp-single.md > output.html
