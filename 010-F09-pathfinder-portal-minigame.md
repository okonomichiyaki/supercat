## Find the Portal Minigame

This minigame makes it possible for the Pathfinder to be used in a solo game, enabling either the player or the bot to play them. Use this minigame when performing the Prelude ability on "Uncovering Clues" (F9-02). The same rules should be used whether the player or the bot is the Pathfinder.

The minigame retains all the mechanics of the Portal and the Clue tokens. The Portal is still secretly located on one of the planets, and the meaning of the Clue tokens is exactly the same as described on the cards "Uncovering Clues" and "Clues to the Portal" (F9-03).

Unlike the multiplayer game, the Portal is not in a single fixed location at the start of Act II and its location is uncertain until narrowed down to a single planet. A probabilistic method is used to hide the Portal's location from both the player and the bot. The Pathfinder (either bot or player) will need to narrow down the possible locations using an identical logical deduction process as they would in the original multiplayer game.

Each time "Uncovering Clues" is used, one "round" of the minigame will result in either a Clue token or the Portal token being placed on the map. The minigame builds a pool of cubes which are used to randomly determine which token to place. The distribution of cubes ensures that Clue tokens are never placed which contradict previous Clues.

### Components

- red and blue meeples <!-- (optionally yellow meeples as well) -->
	- no more than 6 of each color needed
- red, blue, and yellow cubes
	- no more than 10 of each red and blue are needed
	- no more than 1 yellow cube is needed
- a pawn
- a bag or cup, suitable for drawing cubes at random
- the chart below

*(substitute other small pieces or other colors as needed, but they should be distinguishable from each other, and whatever stands in for the "cubes" needs to be drawn from the bag/cup at random)*

<br/>

<!--
TODO: print friendly chart using icons
-->

| | Hex | Arrow | Moon |
| - | - | - | - |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

### Overview

Each space on the chart represents one of the 18 planets on the board, identified by the symbol (column) and cluster number (row). During the minigame pieces (meeples, cubes, and the pawn) will be added and removed from the chart and used to randomly select a Clue token.

The pawn is placed on the space corresponding to the target planet, i.e. the current "guess".
*(the planet where the Pathfinder's Flagship is located)* The pawn is placed at the start of the minigame and removed at the end.

Red and blue meeples are added to the chart and correspond to Clue tokens placed on the map. Meeples are never removed from the chart.

- a blue meeple matches a "check" token
- a red meeple matches an "x" token

Cubes are added to the chart during an individual round of the minigame and are removed and used in the randomization step at the end of each round. Each cube contributes to the probability that the Portal is or is not one of the planets in relation to the target planet. A red cube increases the chance that the portal is not at a related planet. A blue cube increases the chance that the Portal is at a related planet. A yellow cube contributes to the probability that the Portal is at the target planet.

<!--
Yellow meeples are optional. They do not correspond to Clue tokens but represent possible Portal locations. They will make it easier to drive the bot's logic.
-->

### Sequence of Play

1. Place the pawn on the chart in the space corresponding to the target planet.
2. Count the number of blue meeples already on the chart
3. Add and remove cubes to the chart according to the rules below
4. Place all cubes remaining on the chart into the cup
5. Draw one cube at random
6. If the drawn cube is yellow, then the portal was found
	1. Place the Portal token
7. Otherwise, place a meeple in the space matching the color of the cube
	2. If a blue meeple, place a Clue token with the "check" side faceup on the map
	3. If a red meeple, place a Clue token with the "x" side faceup on the map

### Adding and removing cubes

Important rules and reminders to follow when adding and removing cubes:

- Always add cubes first, exactly in the order described
- After adding cubes, only then remove any cubes as instructed
- A space is "empty" if it has nothing in it (no cube, no meeple, and no pawn)
- A piece "intersects" with another piece or space if they shares a column or row.
- A space will never have more than one cube
- A cube will never be placed in a space with a meeple
- A cube may be placed in a space with the pawn

When adding cubes to the chart, first count the number of blue meeples. Add cubes according to the section matching how many blue meeples are already present on the chart.

**Zero blue meeples**

- Space with pawn: add a yellow cube
- Empty spaces intersecting pawn: add blue cube
- Every other empty space: add red cube

**One or more blue meeples**

- Every space which intersects with ALL blue meeples AND intersects with the pawn
	- if pawn is in the space add a yellow cube
	- if space is empty add a blue cube
- Every space which intersects with ALL blue meeples:
	- if the space is empty add a red cube

**Removing cubes**

After adding cubes above, if there are any red meeples then some cubes may be removed:

- Remove cubes from every space intersecting with a red meeple. *(including any cube from the space with the pawn if it intersects with a red meeple)*
