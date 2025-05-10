# Pathfinder

## Act II

✦ Has the Portal not been found yet?

- Does bot have a resource matching a planet without a Clue token which meets the Clue Guidelines?
	- Yes:
		- Can bot Move the Flagship to that planet?
	- No:
		- Can bot Tax or favorable battle to gain a resource matching a planet without a Clue token which meets the Clue Guidelines?

### Clue Guidelines

Bot will follow these guidelines when selecting planets to target for Clue tokens.
If it's not possible for bot to take actions above which meet these guidelines, then bot will continue to prioritize other actions. *(in other words, these are not preferences and do not select random planets if there is no planet meeting the guidelines)*

- If there are no Clue tokens on the map:
	- any planet
- If the Portal's symbol and cluster has been deduced:
	- *(in other words, the Clue tokens on the map indicate there is only one possibility, but the Portal token has not been placed yet)*
	- identified planet
- If the Portal's symbol has not been deduced yet:
	- Prefer:
		- planet with a symbol not matching a planet with a Clue token
		- planet in a cluster with no Clue tokens in that cluster
- If the Portal's cluster has not been deduced yet:
	- Prefer:
		- planet in a cluster with no Clue tokens in that cluster
		- planet with a symbol matching 

Uncovering Clues
: Use Prelude ability when current planet meets Clue Priorities
