## Find the Portal Minigame

This minigame allows the Pathfinder "B" Fate to be used in a solo game. It enables either the player to play as the Pathfinder or the bot to play as the Pathfinder. Use this minigame when performing the Prelude ability on "Uncovering Clues" (card F9-02). The same rules should be used regardless of whether the player or the bot is the Pathfinder.

The minigame retains the same mechanical structure of the original multiplayer game. The Portal is still secretly located on one of the 18 planets and the Pathfinder uses the same deduction mechanics to narrow the possibilities down. The minigame replicates this via a probabilistic method, but the possible game states are identical to the multiplayer game.

### Components

- red, blue, and yellow meeples
	- no more than 6 of each color needed
- red, blue, and yellow cubes
	- no more than 10 of each color needed
- a pawn
- a bag or cup, suitable for drawing cubes at random
- the chart below

*(substitute other small pieces as needed, but they should be distinguishable from each other, and the "cubes" need to be drawn from the bag/cup at random)*

TODO: insert chart here

### Overview

Each space on the chart represents one of the 18 planets on the board, identified by the symbol (column) and cluster number (row). Pieces (pawn, meeples, and cubes) will be placed on this chart, representing information which is known about the location of the Portal (i.e. which Clue tokens have been placed).

The pawn is placed on the space corresponding to the target planet, i.e. the current "guess".
*(the planet where the Pathfinder's Flagship is located)*

Red and blue meeples on the chart correspond to Clue tokens placed on the map:

- a blue meeple matches a "check" token
- a red meeple matches an "x" token

Yellow meeples do not correspond to Clue tokens but represent possible Portal locations.

### Terminology

Intersect
: a piece on the chart "intersects" another piece if the two pieces share either a column or row

Corner
: TODO

### Sequence of Play

1. Place the pawn on the chart in the space corresponding to the target planet.
2. Follow the first set of procedures ("Start here") consulting the state of the chart.
3. If procedures lead to "PORTAL FOUND", skip to "Portal Found" section.
4. If procedures instruct you to "PLACE MEEPLE", skip to "Placing meeples" section.
5. If procedures instruct you to "BUILD BAG", add the specified number and color of cubes to the bag or cup.
6. Draw one cube at random.
7. If the cube was yellow, then the portal was found. Skip to "Portal Found" section
8. Otherwise, skip to "Placing meeples" section and place a meeple matching the color of the drawn cube.

### Start here:

✦ Are there no meeples on the chart? *(first guess)*

- BUILD BAG:
	- 1 yellow
	- 7 blue
	- 10 red

✦ Are there any yellow meeples on the chart? How many are there?

- 1 yellow meeple:
	- if pawn is with a yellow meeple: PORTAL FOUND
	- if pawn intersects a yellow meeple, PLACE MEEPLE: Blue
	- otherwise place a red meeple
- 2 yellow meeples, which do not intersect (do not share a row or column)
	- if pawn is with a yellow meeple: build bag with 2 cubes: 1 yellow, 1 red
	- if pawn is not with a yellow meeple but intersects a yellow meeple
- 2 or more yellow meeples all on the same column or row:
	- if pawn is with a yellow meeple: BUILD BAG with cubes equals to number of yellow meeples: 1 yellow, the rest blue
	- if pawn intersects a yellow meeple: BUILD BAG with cubes equal to number of yellow meeples, 1 blue, the rest red
	- if pawn not with yellow meeple and not intersecting yellow meeple, PLACE MEEPLE: Red

✦ Does the pawn intersect with 2 or more meeples? What color are they?

- All red
	- Are they on different columns and different rows? PLACE MEEPLE: Red
	- Are they 2 red meeples both on the same row as the pawn? PLACE MEEPLE: Blue
	- Are they 2 or more red meeples all on the same column as pawn? BUILD BAG with cubes equal to number of spaces without meeples in the column: 1 blue, the rest red
- All blue
	- Are they 2 blue meeples both on the same row as pawn? PORTAL FOUND
	- Are they 2+ blue meeples all on the same column as pawn? BUILD BAG with cubes equal to number of spaces without meeples in the column: 1 yellow, the rest blue
- Mix of red and blue
	- 1+ red and 1+ blue on the same row or column as pawn? -> place red meeple

✦ Does the pawn intersect with 1 meeple only? What color is it?

- Blue
	- How many blue meeples are on the chart (in total)?
		- If 2+ blue meeples, PLACE MEEPLE: Red
		- If only 1 blue meeple, BUILD BAG using the following procedure:
			- place 1 yellow cube with pawn
			- place 1 blue cube on each space which intersects with both pawn and blue meeple *(in other words, if the blue meeple and pawn share a column, place a blue cube on each empty space in that column. if the blue meeple and pawn share a row, place 1 blue cube on the empty space in that row)*
			- place 1 red cube on remaining empty spaces which intersect with the blue meeple
			- for each red meeple on the chart, if it intersects with any cube, remove that cube from the chart

✦ Does the pawn intersect with 0 meeples?

- is there 1 blue meeple on the chart?
	- build bag. use the following procedure to fill the bag:
		- place 1 blue cube at each empty space intersecting with the pawn and the blue meeple *(2 blue cubes total)*
		- place 1 red cube at each remaining empty space intersecting with the blue meeple
		- for each red meeple on the chart, if it intersects with any cube, remove that cube from the chart



When placing a meeple, follow these procedures according to the color of the new meeple. These steps may instruct you to place additional meeples, but simply place those as instructed.
*(in other words, do not recursively apply this procedure)*

✦ Blue?

- if there are no other blue meeples, place this one and continue
- if there is 1 other blue meeple, where is it?
	- same row as the new one?
		- place a yellow meeple in the other space in this row
	- same column as the new one?
		- find spaces in this column which intersect red meeples, and fill with blue meeples
		- fill remaining spaces in this column or row with yellow meeples
	- different column and different row?
		- place a yellow meeple in each "corner" space
- if there are 2 existing blue meeples check if they uniquely identify the Portal planet:
	- if all of them are on the same column, the Portal cannot be identified yet.
	- if all of them are on the same row -- BUG
	- if one of them is on a different column, the Portal can be uniquely identified:
		- remove all yellow meeples
		- place a yellow meeple intersecting with all 3 blue meeples

**Clue token:** place a Clue token with the "check" side face up on the corresponding planet.

<!-- 
✦ Yellow?

Is already a yellow meeple in the space?

- the Portal was FOUND: place the Portal token on the corresponding planet
-->

✦ Red?

- Does the new meeple intersect with a blue meeple?
	- if new meeple is in the same column as the blue meeple, place yellow meeples in the empty spaces in the row with the blue meeple
	- if new meeple is in the same row as the blue meeple, place yellow meeples in the empty spaces in the column with the blue meeple
	
- Check each space the new meeple intersects:
	- if a yellow meeple is in the space:
		- if it is a "corner" space, replace it with a red meeple
		- otherwise replace it with a blue meeple

**Clue token:** place a Clue token with the "x" side face up on the corresponding planet
