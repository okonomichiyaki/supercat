<#ifdef campaign>
## Fates

Each Fate has its own set of procedures and priorities which will drive the bot's behavior. Some Fates have instructions for specific cards, and some Fates have additional rules for handling mechanics which pose a complication for solo play. Others will have general information for how other bots will interact with the mechanics introduced by the Fate (e.g. Faithful cards).

Each Fate's procedures are arranged by Act. When consulting the page corresponding to the active bot's Fate, refer to the section for the current Act only. Check the bot's Fate **once** each turn when explicitly directed to, depending on how the bot's card is selected:

- After a card is automatically selected to declare an ambition or surpass, check the page corresponding to the bot's Fate, and follow procedures if applicable.
- When using "General Priorities" to select a card, note that the first line on that page checks the bot's Fate. Consult the page for the Fate, and if the procedures apply select the card with the suit matching the actions listed.

By default, the bot will not take more actions from its Fate page than **half the number of available actions, rounded up.** Once it takes that many actions, or is unable to take further actions from this page, turn to the page for the selected suit and spend the remaining actions.

## Event Cards

After a round ends in which an Event card was played and resolved, do not add it to the discard pile. Instead, set played Event cards aside and only shuffle them with the action cards prior to dealing at the start of the next chapter. *(since the action card deck will be reshuffled mid-round when there are 2 or more bots, this is to ensure Event cards do not occur more frequently than in multiplayer games)*

## Govern the Imperial Reach

If the bot is the First Regent, check the bot's Fate to determine if it will change the policy. If Fate does not dictate a policy change, check if enforcing the current policy would cause bot to contend an ambition. If so, enforce the policy. Otherwise, change the policy and select policy which, if enforced, would cause bot to contend an ambition.

While enforcing the current policy, if a rival has no pieces for Imperial Demand and has no agent, roll 1d6 and make the rival an Outlaw on 5 or 6.

## Summits

If bot is given the opportunity to call a Summit, via Event card or the Imperial Council, check the bot's Fate. If Fate does not dictate behavior for Summits, roll 1d6, +1 for each favor the bot has, and call a Summit on a result of 5 or 6.

If bot calls a Summit and has one or more favors, during the "Call to Order" phase, follow these procedures:

- **Return Favors**: Follow these priorities to select negotiation actions. Return as many as possible, using favors as efficiently as possible.
	- contend a declared or undeclared ambition
	- advance objective directly or indirectly
	- cause rival to stop contending for a declared ambition
- **Petition the Council, Leave the Empire, Revive the Empire:** Check Fate

## Grievances (Optional but recommended)

This should be considered an optional but recommended rule. It will add a little bit of extra friction for the solo player as well as some texture to the negotiation minigame.

Each bot will have a grievance counter matching the colors of all other bots and players. For instance, in a game with 1 player and 3 bots, a bot using the red pieces will track grievances in white, blue, and yellow. At the beginning of the game, the value of these is all zero.

Certain actions taken against a bot, by a player or other bot, will result in a grievance. The target of the action will gain one or more grievance matching the source. Each of the following results in the target gaining one grievance:

* Battle action with bot as the defender
* destroy one or more bot pieces (limit 1 per action)
* steal a resource or guild card from the bot (limit 1 per action)
* target bot city with a Tax action
* take one or more bot agents captive (limit 1 per action)

<div class="pagebreak"> </div>

## Negotiation Minigame

During the Negotiations phase of a Summit, the player has an opportunity to offer bots negotiation actions, and each bot may do the same with other bots. This takes the form of a new, solo-specific minigame. This alternative enables a solo player to engage with all of the mechanics of the campaign, and makes it possible for certain Fates which rely on the Negotiation mechanics (Magnate, Caretaker) to be piloted by a player or a bot.

When a Summit occurs, after the "Call to Order" phase, follow this sequence of play for the minigame:

- Determine the number of rounds: roll 1d6 and add 1 per bot
- Player(s) may settle Grievances with favors:
	- if a player returns a favor to a bot *(without forcing any negotiation actions)* or gives one of their agents to a bot as a favor, reduce the bot's Grievances matching the player by one
- Starting with the bot or player with initiative, conduct negotiation rounds
- On a player's round, they may attempt a trade with a bot.
	- If the trade is successful, they must pass to next player or bot in turn order
	- After 3 consecutive failures, they must pass to next player or bot in turn order
- During a bot's negotiation round, it will attempt one negotiation with another bot, then pass
- After each player and bot as had a turn, end minigame *(even if rounds remain)*

Each negotiation round is a single trade attempt:

- Player or bot will offer to exchange one or more negotiation actions with a target bot
- Player or bot will commit to an offer, then roll 1d6 to determine if the target bot accepts
- The target bot will accept on a modified roll of a 5 or 6

Apply the following DRMs to the roll:

<ul>
<li>-1 for each successive failed attempt</li>
<li>-1 for each matching Grievance</li>
<li>-1 if trade would cause rival of target to contend a declared ambition</li>
<li>-X if bot is contending a declared ambition. X=power bot would gain from the ambition</li>
<li>+1 for each negotiation action offered above an even trade</li>
<li>+1 if trade would cause target to contend a declared ambition</li>
<li>+1 if trade would cause bot to directly or indirectly advance objective</li>
</ul>

To determine bot-bot offers, examine each rival bot in turn order, and identify what the active bot "wants" from the other bot. Use these priorities, and if none apply, pass next player or bot, but still count the round as having occurred:

- resource, trophy, or captive which would cause bot to contend a declared ambition
- negotiation actions which would directly or indirectly advance bot's objective

The active bot will offer the target resources and favors such that the final DRM is +2. Bot will not offer resources matching declared ambition bot is currently contending.
<div class="pagebreak"> </div>
<#endif>
