# Bot turn (START HERE)

✦ If bot has no cards left *(check hand counter)* then bot will pass.

✦ Is bot's hand counter greater than number of bonus cards in the bot's play area?

- Draw 2 cards.

✦ Decrement hand counter.

✦ Does bot have initiative?

- Remove seize counter, if present.
<#ifdef campaign>- Is one or more card an Event?
	- Draw until there are 2 non-Event cards to choose from, or no more cards.
	- Shuffle drawn Event cards back into stack and select from drawn non-Event cards.
<#endif>- Is bot winning or tied for first place for a matching ambition?
	- Is there an ambition marker available?
		- Select matching card and declare, if bot is winning OR ambition not yet declared.
		- Prefer: ambition that bot is winning
- Use General Priorities to select card.

✦ Can bot surpass with any card?

- Yes:
	- Select card which surpasses. Prefer: higher number
- No:
	- If seize counter is on bot's board, increment it, else place seize counter, with a value of 1.
	- If hand counter is 2 or greater and initiative was not already seized this round, check for seize:
		- Roll 1d6, and subtract 1 for each undeclared ambition that bot is winning<#ifdef campaign>, subtract 1 again if holding Event or one played earlier, and if Event is effective<#endif>. Seize initiative if result is less than seize counter. Decrement hand counter to represent bot discarding an extra card.
	- <#ifdef campaign>If one of the cards is an Event, and an Event has not been played this round, play it. Otherwise:<#endif> Use General Priorities to select card.

✦ Once a card is selected, discard other drawn cards. Check for Prelude actions, then go to page for selected card's suit.

<div class="pagebreak"> </div>
