
## Act II

### Find the Portal Minigame

When using the Prelude ability on Uncovering Clues, use the following sequence:

1. Place the pawn on the chart in the space corresponding to the target planet. *(the planet with the Pathfinder's Flagship)*
2. Follow the first set of procedures below, which will ask you to consult the state of the chart.
3. If the procedures lead to "PORTAL FOUND" then skip to "Portal Found" section
4. If the procedures instruct you to place a meeple, skip to the "Placing meeples" section
5. Otherwise, the procedures will build a bag of cubes. Place cubes in the bag, following the instructions for which color cubes and what quantity of each.
6. Draw one cube from the bag at random.
7. If the cube was yellow, the portal was found. Skip to "Portal Found" section
8. Otherwise, skip to "Placing meeples" section to place a meeple matching the color of the drawn cube.

✦ Are there no meeples on the chart? *(first guess)*

- build bag with the following cubes:
	- 1 yellow
	- 7 blue
	- 10 red

✦ Are there any yellow meeples?

- 1 yellow meeple:
	- if pawn is with the yellow meeple: PORTAL FOUND
	- if pawn is not with a yellow meeple but intersects the yellow meeple, place a blue meeple
	- otherwise place a red meeple
- 2 yellow meeples, not on the same column or row:
	- if pawn is with a yellow meeple: build bag with 2 cubes: 1 yellow, 1 red
- 2 or more yellow meeples all on the same column or row:
	- if pawn is with a yellow meeple: build bag with cubes equals to number of yellow meeples: 1 yellow, the rest blue
	- if pawn intersects a yellow meeple: build bag with cubes equal to number of yellow meeples, 1 blue, the rest red
	- if pawn not with yellow meeple and not intersecting yellow meeple, place red meeple

✦ Does the pawn intersect with 2 or more meeples? What color are they?

- All red
	- different column and different row? -> place red meeple
	- 2 red on the same row as pawn? -> place blue meeple
	- 2 or more red on the same column as pawn? -> build bag with cubes equal to number of spaces without meeples in the column: 1 blue, the rest red
- All blue
	- different column and different row?
		- check the opposite "corner"
			- if empty: build bag with 1 red and 1 yellow
			- if red meeple: PORTAL FOUND
	- 2 blue on the same row as pawn? -> place yellow meeple
	- 2 or more blue on the same column as pawn? -> build bag with cubes equal to number of spaces without meeples in the column: 1 yellow, the rest blue
- Mix of red and blue
	- 1+ red and 1+ blue on the same row or column as pawn? -> place red meeple

✦ Does the pawn intersect with 1 meeple only? What color is it?

- Blue
	- How many blue meeples are there on the chart?
		- if 2+ blue meeples -> place red meeple
		- if only 1 blue meeple *(the one the pawn intersects with)* ->
			- build bag. use the following procedure to fill the bag:
				- place 1 yellow cube with pawn
				- place 1 blue cube on each space which intersects with both pawn and blue meeple *(in other words, if the blue meeple and pawn share a column, place a blue cube on each empty space in that column. if the blue meeple and pawn share a row, place 1 blue cube on the empty space in that row)*
				- place 1 red cube on remaining empty spaces which intersect with the blue meeple
				- for each red meeple on the chart, if it intersects with any cube, remove that cube from the chart

✦ Does the pawn intersect with 0 meeples?

- is there 1 blue meeple on the chart?
	- build bag. use the following procedure to fill the bag:
		- place 1 blue cube at each empty space intersecting with the pawn and the blue meeple *(2 blue cubes total)*
		- place 1 red cube at each remaining empty space intersecting with the blue cube
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
