# Influence Principles

When influencing cards in the court, the bot will follow these guidelines.

If possible, influence uncontested cards with 2 agents. Otherwise, influence uncontested cards with 1 agent. *(in other words, if the bot has 2 actions and 2 available agents, and procedures direct the bot to influence an uncontested card, bot will spend 2 actions to place 2 agents)*

If possible, influence a contested card with one more agent than the most rival agents. Otherwise, check if the bot has enough agents: if the bot could influence with agents up to the most rival agents, and still have agents in its supply left over, then influence the card to match rival agents. Otherwise, do not influence the card.

## Priorities

When choosing between options which are otherwise equal in priority, use the following priorities to select a card to influence.

<#ifdef campaign>- Lore card
- adverse Vox card (Crisis negatively impacts bot)
- card with attached Faithful card
- card with attached Guild card
<#endif>- uncontested card
- card granting a bonus action card (for example Union card or "Call to Action" Vox card)
- card which would take most captives
- Loyal card for outraged resource

If further tie breaking is necessary, prefer the card with more keys.

<div class="pagebreak"> </div>
