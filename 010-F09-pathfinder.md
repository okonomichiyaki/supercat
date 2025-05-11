# Pathfinder

## Act II

✦ Has the Portal been found? *(is the Portal token on the map?)*

- Yes:
	- Can bot Build, Repair, or Move to control the Portal?
- No:
	- Select planets meeting the Clue guidelines below. Does bot have a resource eligible for Uncovering Clues on one of the planets? *(a resource different from all planets in the cluster)*
		- Yes:
			- Can bot Move the Flagship to that planet? (use partial move)
		- No:
			- Can bot Tax or favorable battle to gain a resource eligible for Uncovering Clues on one of the planets?

Uncovering Clues
: Use Prelude ability if current planet meets Clue Guidelines


## Clue Guidelines

✦ Use these guidelines to select planets for Uncovering Clues, according to the number of Clue tokens already on the map.

✦ How many Clue tokens are on the map?

- None: select any planet
- One: select planets with different symbols and in a different clusters from Clue token
- Two or more:
	- Has the Portal's symbol and cluster been deduced?
		- select identified planet
	- Has the Portal's symbol been deduced?
		- select planet in a cluster with no Clue token
	- Otherwise:
		- select planet which is a possible Portal location
