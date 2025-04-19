<#ifdef campaign>
## Event Cards

After an Event card is played, do not add it to the discard pile. Instead, set played Event cards aside and only shuffle them with the action cards prior to dealing at the start of the next chapter.

*(Since the bot may reshuffle the action card deck this is to ensure Event cards do not occur more frequently than in multiplayer games)*

## Summits

If bot is given the opportunity to call a Summit, via Event card or the Imperial Council, roll 1d6 and apply DRMs below. Bot will call a Summit on a result of 5-6.

<ul>
<li>+1 for each favor the bot has</li>
</ul>

If bot calls a Summit and has one or more favors, during the "Call to Order" phase, follow these procedures:

- **Return Favors**: Follow these priorities to select negotiation actions. Return as many as possible, using favors as efficiently as possible.
	- <ins>contend</ins> a declared or undeclared ambition
	- <ins>contend</ins> advance objective directly or indirectly
	- cause rival to stop <ins>contending</ins> for a declared ambition
- **Petition the Council:** Check Fate
- **Leave the Empire:** Check Fate
- **Revive the Empire:** Check Fate

## Negotiations

During a Summit, the player will have an opportunity offer the bots negotiation actions, and each bot may do the same with other bots. This takes the form of a minigame. Of course this cannot approximate the scope of human interaction which occurs in a multiplayer game, but it is an alternative enabling a solo player to see all of the mechanics of the campaign. This also makes it possible for the Magnate to be played by a player or bot.

<div class="pagebreak"> </div>

## Negotiation Mini Game

- determine the number of rounds (1d6 +1 per bot)
- player(s) may settle grievances with favors:
	- if a player returns a favor to a bot, or gives one of their agents as a favor, reduce the bot's grievances matching the player by one
- starting with the bot or player with the initiative, conduct negotiation rounds
- on a player's round, that player may attempt a trade with a bot
	- if successful, must pass to next player or bot in turn order
	- if 3 consecutive failures, must pass to next player or bot in turn order
- during a bot's negotiation round, it will attempt one negotiation with another bot, then pass
- after each player and bot as had a turn, end mini game *(even if rounds remain)*

Each negotiation round is a single trade attempt:

- player or bot will offer to exchange one or more negotiation actions with a target bot
- player or bot will commit to an offer, then roll 1d6 to determine if the target bot accepts
- the target bot will accept on a modified roll of a 5 or 6

*(Note: bots do not offer trades to the player, only to other bots.)*

Apply the following DRMs to the roll:

<ul>
<li>-1 for each successive failed attempt</li>
<li>-1 for each matching grievance</li>
<li>-1 if trade would cause target to <ins>contend</ins> a declared ambition</li>
<li>-X if bot is <ins>contending</ins> a declared ambition. X=power bot would gain from the ambition</li>
<li>+1 for each negotiation action offered above an even trade</li>
<li>+1 if trade would cause bot to contend a declared ambition</li>
<li>+1 if trade would cause bot to advance objective</li>
</ul>

To determine bot-bot offers, examine each rival bot in turn order, and identify what the current bot "wants" from the other bot. use these priorities, and if none apply, skip the exchange but still count the round as having occurred:

- resource, trophy, or captive which would cause bot to <ins>contend</ins> a declared ambition
- exchanges which would directly or indirectly advance bot's objective

The active bot will offer the target resources and favors such that the final DRM is +2. Bot will not offer resources matching declared ambition bot is currently <ins>contend</ins>.

## Faithful Cards

Since Faithful cards enable any type of action, they are not selected normally via "General Priorities". If the bot needs to use "General Priorities" to select between a Faithful card and any other card, read down the procedures as normal until identifying the bot's priority. If the bot can take the prioritized action using the Faithful card, select that card and turn to the page for the Faithful suit.

## Fates

Each Fate has its own special procedures and priorities on the following pages. When directed to refer to "General Priorities" note that the first line on that page instructs you to check the bot's Fate for initial priorities. Consult the page for the Fate, which will examine the board state and may direct the bot to a line of play. If the procedures apply, select the card indicated.

By default, the bot will take a number of actions from its Fate page **equal to half the number of available actions, rounded up.** It will then proceed to the page for the selected suit and spend the remaining actions, if any. Note that some Fates may spend more or fewer actions from their specific procedures if possible.

<div class="pagebreak"> </div>
<#endif>
