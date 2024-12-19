# Bot turn (START HERE)

✦ Does bot have no cards left? (check hand counter)

- Pass initiative

✦ Draw 2 cards. Decrement hand counter. Use the following procedures to select one card, then discard the other card.

✦ Does bot have initiative?

- Is bot winning or tied for first place for an <ins>undeclared ambition</ins> matching a card option?
	- Yes:
		- Declare the ambition. If more than one option, select card with more pips.
		- Go to page for selected card's suit.
	- No:
		- Is bot winning a declared ambition matching a card option?
			- Declare the ambition. If more than one option, select card with more pips.
			- Go to page for selected card's suit
		- Go to General Priorities.

✦ Can bot surpass with either card?

- Yes:
	- Surpass. If more than one option, select card with high number.
	- Remove seize counter.
	- Go to page for selected card's suit.
- No:
	- If seize counter is on bot's board, increment it, else place seize counter, with a value of 1.
	- If seize counter is on 4 and bot has 2 or more cards left and able to seize, then seize:
		- Decrement hand counter.
		- Remove seize counter.
	- Go to General Priorities

<div class="pagebreak"> </div>
