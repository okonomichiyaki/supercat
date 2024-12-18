# Bot turn (START HERE)

Draw 2 cards. Use the following procedure to select one card, then discard the other card.

- Does bot have initiative?
	- Yes:
		- Is bot currently winning or tied for first place for an undeclared ambition?
			- Yes:
				- Declare (place zero marker)
				- If multiple options: use General Priorities or select card with more pips
			- No:
				- Use General Priorities or select card with higher number
- Can bot surpass with either card?
	- Yes:
		- Surpass
		- If multiple options, select card with more pips
		- Remove seize counter
	- No:
		- Check for seize:
			- If seize counter is on bot board, increment. otherwise place seize counter, with a value of 1
			- If seize counter is on 4 and bot's hand counter is on 3 or greater, then seize:
				- Decrement hand counter
				- Remove seize counter
		- Then use General Priorities to select card

Go to the flowchart for the suit of selected card and execute the bot's turn.
<br> Finally, decrement the bot's hand counter (remove from board to indicate zero)

<div class="pagebreak"> </div>
