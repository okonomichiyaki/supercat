
# SUPERCAT: a procedural non-player system for Arcs

a bot intended for playing the board game Arcs solo, nicknamed "SUPERCAT".
it should be considered a very rough draft, but it's playable in its current state

build:

```
pandoc -s --css=pandoc.css \
00-how\ to\ play\ with\ SUPERCAT.md \
01-bot\ turn\ start\ here.md
02-general\ priorities.md \
03-prelude.md \
-o output.html
```
