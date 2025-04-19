<#ifdef campaign>
## Event Cards

After an Event card is played, do not add it to the discard pile. Instead, set played Event cards aside and only shuffle them with the action cards prior to dealing at the start of the next chapter.

(Since the bot may reshuffle the action card deck this is to limit Event cards from occurring more often than in multiplayer games)


## Grievances (Optional)

This should be considered an optional but recommended rule. It will add a little bit of extra friction for the solo player as well as some texture to the negotiation mini game.

Each bot has a grievance counter matching the colors of all other bots and players. For instance, in a game with 1 player and 3 bots, a bot using the red pieces will track grievances in white, blue, and yellow. At the beginning of the game, the value of these is all zero (in other words, there should be no counter on the bot's board)

Any time a player or bot harms or taxes another bot, this will result in a grievance. The target will gain one or more grievance matching the source, according to the actions below. Each of these results in a single grievance, but a single action might result in more than one grievance.

* target bot with a Battle action
* destroy one or more bot pieces (limit 1 per action)
* steal a resource or guild card from the bot (limit 1 per action)
* target bot city with a Tax action
* take one or more bot agents captive (limit 1 per action)

For example, red bot has zero grievances associated with the blue player. The blue player battles red bot in a system with ships and buildings, and uses a mix of assault and raid dice. The blue player rolls, destroying 2 ships with the assault results, and getting enough keys on the raid dice to steal 1 resource. The red bot will gain 3 grievances matching the blue player (one for the battle action, one for destroying one or more ships, and 1 for stealing resources)


## Negotiations

During a Summit's Negotiations phase, the player will have an opportunity offer the bots negotiation actions, and each bot may do the same with other bots. This takes the form of a minigame. This does not attempt to approximate the full scope of human interaction that can occur in a multiplayer game, but it offers an alternative which allows the solo player to see all of the mechanics of the campaign. This is also what makes it possible for the Magnate to be played by a player or bot.


<div class="pagebreak"> </div>


## sequence of play

- determine number of rounds (1d6 +1 per bot)
- player(s) may settle grievances with favors:
	- if a player returns a favor to a bot, remove one grievance matching the player
- starting with the bot or player with the initiative, conduct negotiation rounds
- on a player's round, that player may attempt a trade with a bot
	- if successful, must pass to next player or bot in turn order
	- if 3 consecutive failures, must pass to next player or bot in turn order
- during a bot's negotiation round, it will attempt one negotiation with another bot, then pass
- if multiple players, after all negotiation rounds have been completed, players may freely negotiate as per the rules

each negotiation round is a single trade attempt:

- player or bot will offer to exchange one or more negotiation actions with a target bot
- player or bot will commit to an offer, then roll 1d6 to determine if the target bot accepts
- the target bot will accept on a modified roll of a 5 or 6
note: bots do not offer trades to the player, only to other bots.

apply the following DRMs to this roll:

<ul>
<li>-1 for each successive failed attempt</li>
<li>-1 for each grievance</li>
<li>-1 if trade would cause target to contend a declared ambition</li>
<li>-X if bot is contending a declared ambition. X=power bot would gain from the ambition if it was scored right now</li>
<li>+1 for each negotiation action offered above an even trade</li>
<li>+1 if trade would cause bot to contend a declared ambition</li>
<li>+1 if trade would cause bot to advance objective</li>
</ul>

<div class="pagebreak"> </div>
<#endif>