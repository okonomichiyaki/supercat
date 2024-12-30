# Bot turn (START HERE)

✦ Does bot have no cards left? (check hand counter)

- Pass initiative

✦ Draw 2 cards. Decrement hand counter. Use the following procedures to select one card, then discard the other card. Once a card has been selected, go to the page corresponding to the selected card's suit.

✦ Does bot have initiative?

- Remove seize counter, if present.
- Is bot winning or tied for first place for an <ins>undeclared ambition</ins> matching one of these two cards?
	- Yes:
		- Select matching card (if multiple options, select card with more pips).
		- Declare the ambition.
	- No:
		- Is bot winning a declared ambition matching one of these two cards, and is there an available ambition marker?
			- Select matching card (if multiple options, select card with more pips).
			- Declare the ambition.
		- If both cards are the same suit, select card with higher number.
		- Otherwise, use General Priorities (next page) to select card.

✦ Can bot surpass with either card?

- Yes:
	- Select card to surpass.
	- If more than one option, select card with high number.
- No:
	- If seize counter is on bot's board, increment it, else place seize counter, with a value of 1.
	- If hand counter is 2 or greater and initiative was not already seized this round, check for seize:
		- Roll 1d6, and subtract 1 for each <ins>undeclared ambition</ins> that bot is winning. Seize initiative if result is less than seize counter. Decrement hand counter to represent bot discarding an extra card.
	- Use General Priorities (next page) to select card.

<div class="pagebreak"> </div>
