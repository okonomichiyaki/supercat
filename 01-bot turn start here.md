# Bot turn (START HERE)

Draw 2 cards. Use the following procedure to select one card, then discard the other card.

- Does bot have initiative?
	- Yes:
		- Is bot contending for an undeclared ambition?
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
			- If counter is on bot board, increment. otherwise place counter with 1 face up
			- If counter is on 4, AND this is not the 5th or 6th card in the round, then seize:
				- Decrement hand counter
				- Remove seize counter
		- Then use General Priorities to select card

Go to the flowchart for the suit of selected card and execute the bot's turn.
Finally, decrement the bot's hand counter.
