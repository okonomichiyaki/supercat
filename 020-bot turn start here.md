# Bot turn (START HERE)

✦ Does bot have no cards left? (check hand counter)

- Pass

✦ Draw 2 cards. Decrement hand counter. Use procedures below to select a card. Then go to the page for selected card's suit and discard the other card.

✦ Does bot have initiative?

- Remove seize counter, if present.
<#ifdef campaign>- Is one or more card an Event?
	- Draw until there are 2 non-Event cards to choose from, or no more cards.
	- Shuffle drawn Event cards back into stack and select from drawn non-Event cards.
<#endif>- Is bot winning or tied for first place for a matching ambition, and is an ambition marker available?
	- Select matching card. Prefer: more pips
	- Declare the ambition (if ambition already declared, only declare if winning)
	- If both cards are the same suit, select card with higher number.
	- Otherwise, use General Priorities to select card.

✦ Can bot surpass with either card?

- Yes:
	- Select card to surpass.
	- If more than one option, select card with high number.
- No:
	- If seize counter is on bot's board, increment it, else place seize counter, with a value of 1.
	- If hand counter is 2 or greater and initiative was not already seized this round, check for seize:
		- Roll 1d6, and subtract 1 for each <ins>undeclared ambition</ins> that bot is winning<#ifdef campaign>, subtract 1 again if holding Event or one played earlier, and if Event is <ins>effective</ins><#endif>. Seize initiative if result is less than seize counter. Decrement hand counter to represent bot discarding an extra card.
	- <#ifdef campaign>If one of the cards is an Event, and an Event has not been played this round, play it. Otherwise:<#endif> Use General Priorities to select card.

<div class="pagebreak"> </div>
