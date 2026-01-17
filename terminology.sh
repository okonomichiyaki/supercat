#!/bin/zsh

grep -v '^:\|^#\|^$' 095-terminology.md >> terminology.md
sort -u -o terminology.md terminology.md
