# Influence Principles

When Influencing cards in the court, the bot will follow these guidelines. An uncontested card is a card in the court with no agents *(no Loyal agents and no Rival agents)*. A contested card is a card in the court which a Rival could Secure *(a Rival has more agents than each other Rival)*. A safe card is a card in the court which the bot could Secure *(more Loyal agents than each other Rival)*.

If possible, influence uncontested cards with 2 agents.
Otherwise, influence uncontested cards with 1 agent.
Never influence safe cards.

<!--
*(if the bot has 2 actions and 2 available agents, and procedures direct the bot to Influence an uncontested card, bot will spend 2 actions to place 2 agents)*
-->

If possible, Influence contested cards with 1 more agent than Rival with most agents.
*(Influence such that bot could Secure the card, but do not Influence more than the minimum needed to Secure)*

Defending Loyal agents on a contested card means preventing their capture by a Rival who can Secure the card. When defending Loyal agents bot will carry out one of three possible choices:

- Outbid: Influence with one more agent than Rival with most agents *(potentially allowing bot to Secure)*
- Block: Influence with agents up to Rival with most agents *(preventing the Rival from Securing and taking captives)*
- Abandon: do not Influence at all

Roll 1d6 and compare the result to the most Rival agents currently on the card.
If the die roll is greater than most Rival agents, bot will Outbid.
If die roll is equal to most Rival agents, bot will Block.
If die roll is less than most Rival agents, bot will Abandon.

Additionally, before Blocking, check if any agents would remain in bot's supply. If the bot cannot Influence with agents up to Rival with most agents and still have at least one agent in its supply left over, then Abandon instead.

## Critical cards

Critical cards are cards in the Court which the bot is more interested in Influencing and Securing than others. When procedures direct bot to Influence or Secure a Critical card, select cards from the priority list below.

- an adverse Vox card (Vox card with a Crisis which negatively impacts bot)
- a card which would result in bot contending a declared ambition, if Secured
	- *(this includes the Imperial Council, if bot could contend a declared via the Imperial Trust, by becoming First Regent OR by stealing from the Trust as an Outlaw)*
- an effective Vox card
- a card granting any bonus action card
	- *(for example any Faithful card, Union card, or "Call to Action" Vox card)*
- any non-Vox card with any other non-Vox card attached to it
	- *(for example, a Guild card with an attached Faithful card, or a Guild card with an attached lore card. but NOT a Vox card with an attached Faithful card, etc.)*

## non-Critical cards

When procedures direct bot to Influence or Secure any other Court card, select cards from the priority list below.

- captives
- contend an undeclared ambition
- grow a lead in a declared ambition
- Weapon icon
- grow a lead in an undeclared ambition

## Tie-breaking

When choosing between two or more cards (either Critical or non-Critical) which are otherwise equal in priority, use the following priorities to select a card to influence.

- uncontested card
	- only if bot is Influencing with 2 agents
- card with attached Faithful, Guild, or lore card
- card which would take most captives
- "Loyal" card matching an Outrage type *(for example, "Loyal Marines" if bot has Weapon Outrage)*
- card with more keys

<div class="pagebreak"> </div>
