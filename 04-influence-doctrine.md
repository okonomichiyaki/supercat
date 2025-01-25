
When influencing cards in the court, the bot will follow these guidelines.

If possible, influence an <ins>uncontested</ins> card with 2 agents. Otherwise, influence with 1 agent. In other words, if the bot has 2 actions and 2 available agents, and procedures direct the bot to influence an <ins>uncontested</ins> card, bot will spend 2 actions to place 2 agents.

If possible, influence a <ins>contested</ins> card with one more agent than the most rival agents. Otherwise, check if the bot has enough agents: if the bot could influence with agents up to the most rival agents, and still have agents in its supply left over, then influence the card to match rival agents. Otherwise, do not influence the card.

When choosing between cards in the court, use the following priorities to select a card.

- Weapon
- Union card or "Call to Action" (Vox card)
- <ins>Effective</ins> Vox card
- Captives
	- i.e. any card where bot could influence with more agents than rival
- Other Vox card
- Icon to grow a lead in a declared ambition
- Loyal card matching outraged resource

If necessary, break ties based on number of keys (choose card with more keys).
If same number of keys, choose randomly.
