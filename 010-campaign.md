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
- after all negotiation rounds have been completed, players may freely negotiate as normal

Each negotiation round is a single trade attempt:

- player or bot will offer to exchange one or more negotiation actions with a target bot
- player or bot will commit to an offer, then roll 1d6 to determine if the target bot accepts
- the target bot will accept on a modified roll of a 5 or 6
note: bots do not offer trades to the player, only to other bots.

To determine bot-bot offers, examine each rival bot in turn order, and identify what the current bot "wants" from the other bot. use these priorities, and if none apply, skip the exchange but still count the round as having occurred:

- resource, trophy, or captive which would cause bot to <ins>contend</ins> a declared ambition
- exchanges which would directly or indirectly advance bot's objective

Apply the following DRMs to the roll:

<ul>
<li>-1 for each successive failed attempt</li>
<li>-1 for each matching grievance</li>
<li>-1 if trade would cause target to <ins>contend</ins> a declared ambition</li>
<li>-X if bot is contending a declared ambition. X=power bot would gain from the ambition if it was scored right now</li>
<li>+1 for each negotiation action offered above an even trade</li>
<li>+1 if trade would cause bot to contend a declared ambition</li>
<li>+1 if trade would cause bot to advance objective</li>
</ul>

<div class="pagebreak"> </div>
<#endif>
