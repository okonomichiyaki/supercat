## a procedural non-player system for solo Arcs

*version 0.8*

This is a non-player system, or "bot", for playing the board game Arcs. It's intended for solitaire play, i.e. one human playing against one or more bots. Although it can also work as the 3rd or 4th opponent in a multiplayer game, using it in this way has not been tested thoroughly.

SUPERCAT is not an "automa" but is instead a simulation-style bot. Rather than streamline any mechanics, it attempts to interact with all of the rules of the original game using conditional procedures which mimic a human opponent. The bot deviates from the rules in a few important ways, but will follow every other rule in the game apart from these changes:

- the bot's hand of cards is abstracted to retain some uncertainty and "fog of war"
- there are optional difficulty modifiers to make the solo experience more challenging
<#ifdef campaign>- some Fates use special rules for mechanics which are awkward in a solo context<#endif>

These rules will always refer to the human player as the "player", and will refer to the non-player system exclusively as the "bot". The word "player" never refers to a bot.

There are two versions of this document; this is the <#ifdef base>base game<#endif><#ifdef campaign>Blighted Reach campaign<#endif> version. <#ifdef campaign>*(note: it currently only supports "A" and "B" Fates through Act II)*<#endif>

<#ifdef campaign>If this is your first time playing Arcs using SUPERCAT, consider playing at least one chapter of the base game with the bot before using it to play the campaign.<#endif>

*Arcs was designed by Cole Wehrle and published by Leder Games.* <br>
*SUPERCAT is an unofficial fan project, and is not affiliated with Leder Games.*

## Components

You will need some way to track <#ifdef base>two<#endif><#ifdef campaign>several<#endif> values per bot, for instance dice of different colors rotated to show a different number faceup. These can be six sided dice (only in rare situations will the values exceed six) but could also be eight or ten sided dice (they are never rolled). These are referred to as "counters" in the rules that follow. <#ifdef base>You will separately need one six sided die which will be rolled for a random number.<#endif>
<#ifdef campaign>
You will need at least two counters per bot, and if playing with the optional Grievances rule (a new mechanic introduced by this solo mode), you will also need extra counters for each bot, which depend on the number of bots in the game. At most you will need one red, blue, yellow, and white counter for each bot.
*(some Fates require additional components: see Pathfinder for details)*
<#endif>

<#ifdef base>
<div class="pagebreak"></div>
<#endif>

<#ifdef base>
## Setup

Set up the game according to the Arcs rulebook, but make changes at the steps listed below. See "Difficulty Modifiers" section for more details on optional steps.

**1.B.** (optional) Give the initiative marker to a bot, and seat the player last in turn order.

**2.N.** (optional) Place an extra ship in each system with bot pieces.

**2.O.** (optional) Give each bot a random resource.

**2.P.** Deal 6 cards to each player, but do not deal cards to the bot(s). Place a counter on each bot's board showing a value of 6 faceup.

**2.Q.** Place all action cards not in player hands in a single face down stack next to the board.
<#endif>

<#ifdef campaign>
## Act I Setup

Set up the game according to the Blighted Reach rulebook, but make changes at the steps listed below. See "Difficulty Modifiers" section for more details on optional steps.

**1.B.** (optional) Give the initiative marker to a bot, and seat the player last in turn order.

**2.B.** Assign "A" Fates using any method you like. *(suggestion: the player draws 2 "A" Fate cards and chooses one, then randomly assign each bot an "A" Fate card)*

**2.G-H.** When the bot places a building, randomly select an empty building slot from among those eligible. The first building each bot places will be a city and the second will be a starport. *If a bot is the Believer, check that Fate's procedures for special instructions.* (optional) Place an extra ship in each system with bot pieces and give each bot one random resource.

**2.J.** Deal 6 cards to each player, but do not deal cards to the bot(s). Place a counter on each bot's board showing a value of 6 faceup.

**2.K.** Place all action cards not in player hands in a single face down stack next to the board.
<#endif>

## Playing a chapter

The bot does not hold a hand of action cards. Instead, the bot's cards are abstracted by a counter and a facedown stack of all remaining action cards. This stack is shared by all bots, but each bot has its own counter, representing that bot's hand.

Each bot's counter starts the chapter at 6 and will be decremented when the bot plays a card. If the bot seizes initiative, the counter will be decremented a second time, to represent the bot playing an extra card facedown. If the bot receives a "bonus" card the counter will be incremented (for example, from the "Call to Action" Vox card). This way, the counter will always show the number of cards remaining in the bot's "virtual" hand. *(when the counter is on 1, decrement by removing the counter)*

If at any time the stack runs out, shuffle the discard pile <#ifdef campaign>(excluding Event cards)<#endif> before drawing cards for the bot. Continue until the player has no cards and each bot's hand counter is at zero, at which point the chapter ends.
<#ifdef campaign>
At the end of the chapter, shuffle all action cards from the discard pile, any remaining in the stack, and any set aside Event cards before dealing cards to the player(s).
<#endif>

<#ifdef base>
<div class="pagebreak"></div>
<#endif>

## Playing a bot turn

At the start of a bot's turn, check the hand counter. If it is showing 1 or greater, the bot has cards remaining and will play one. Draw 2 action cards from the facedown stack and decrement the counter. The procedures on the "Bot Turn" page will select one of the cards for the bot to play, and also determine whether the bot declares an ambition or seizes the initiative. At that point, discard the other card, and continue with the procedures to execute the bot's turn.

### Bonus cards

When the bot receives a bonus action card, place the new card in the bot's play area and increment the bot's hand counter. On subsequent turns, prior to drawing 2 cards from the facedown stack, compare how many bonus cards the bot has to the hand counter's current value. If the counter is showing a value greater than the number of bonus cards, the bot will draw 2 cards from the facedown stack. If the counter is equal to the number of bonus cards, the bot will not draw 2 cards. Either way, decrement the hand counter.

Then the bot will then select a card to play from among all available cards: any bonus cards in the bot's play area plus any drawn cards. Evaluate all cards equally according to the procedures. After a card is selected, discard any drawn cards which were not selected. Do not discard bonus cards from the bot's play area until they have been selected and played.

### Prelude

After the bot has selected a card, consult the guidelines for Prelude actions, and spend any resources or Guild cards for their effect now. After the bot completes the Prelude, go to the page for the selected card's suit, and execute the bot's actions using the procedures on that page.

### Guild and Lore Cards

The bot will use **new actions** on Guild and lore cards, like **Manufacture (Build)**, at most once per chapter. When using "General Priorities" to select a card to play, there is a check to see if the bot can use any abilities on ready Guild cards. A Guild card is ready if it has not been used this chapter. If the bot selects a card due to this procedure, mark the Guild card as exhausted (rotate the card or place a marker on the card). At the end of the chapter, all cards become ready again (turn the card upright or remove the marker).

<#ifdef base>
<div class="pagebreak"></div>
<#endif>

## How to follow the procedures

Follow each bulleted instruction explicitly, executing statements if possible. When posed with a question, evaluate the situation and follow the nested steps. For more detailed explanation of interpreting nested procedures, see "Questions".

When directed to use "General Priorities", select a card from among the bot's options and Lead, Pivot, or Copy with the indicated suit. If the indicated suit is not available, proceed to the next question.

When multiple actions are available to the bot *(for example Leading with a low number card)*, first spend actions according to the highest priority, then if actions remaining, restart the procedures from the top of that suit's page.

The procedures use some special vocabulary that is specific to SUPERCAT. See the "Terminology" page for explanations of words like contend. When rounding any fractions, always round down, unless otherwise specified.

Aside from the changes to card play described above, <#ifdef campaign>the negotiation minigame, some special handling of certain Fate abilities,<#endif> and the additional advantages granted by difficulty modifiers, the bot will follow every rule in the game.

<#ifdef base>
<div class="pagebreak"></div>
<#endif>

## Decision making for the bot

When evaluating the bots options for its turn, there may be some ambiguity as to which action to take or how to execute a specific action. The player should only need to make limited decisions on behalf of the bot. The following rules attempt to resolve multiple options for the bot as much as possible.

Actions
: When different actions can achieve the same goal, select the first eligible option. For example, in the procedure "Can bot Secure or Tax to contend declared ambition", the bot will prefer to Secure rather than Tax if both actions contend a declared ambition.

Goals
: Similarly, if there are multiple goals, they are also listed in priority order. For example, in the procedure "Can bot Secure to contend an undeclared ambition, to take captives, or to grow lead in declared ambition", the bot will prefer to contend an undeclared ambition before growing a lead in a declared ambition.

Prefer
: Some actions have extra guidance in the form of "preferences", indicated with the word "Prefer" and a list of priorities. Use these priorities to decide between multiple options. Narrow the possibilities to only those which meet the first priority, then the second priority, and so on, until only one option remains.

Principles
: There are a set of four "Principles" which the bot will follow when taking certain actions. Use these to guide the specific actions the bot will take when Influencing, Moving, engaging in combat, and expanding the bot's territory.

Random
: If the bot has multiple options and the procedures do not give explicit preferences, or those priorities fail to differentiate between the options, pick randomly.

<#ifdef base>
<div class="pagebreak"></div>
<#endif>

## Difficulty modifiers (Optional but recommended)

The procedures try to emulate competent play, but the bot doesn't plan multiple cards ahead and makes limited use of Guild and lore cards. For a more challenging game, start each game with the player last in turn order, and give the bot some additional advantages when it does not have more power than the player:

- **Efficient Logistics**: bot performs 1 extra action per card
- **Elite Pilots**: bot collects 1 extra die during Battle

*Note: If the bot is tied with the player, it does not have more power, and will gain these advantages, including at the start of the game when all power markers are tied at zero.*

Relative power should be evaluated per bot, so in a game with 2 bots, if one bot is ahead of the player, and the other is behind, apply these only to the losing bot. In a multiplayer game, check power between bots and players: grant the bot advantages when it is behind all players.

This setting should be considered "normal mode", because without these advantages you may find the bot unsatisfying, especially in games with only 1 bot.

For a harder game:

- Apply the above advantages even if the bot is ahead in power.
- The bot with the most power starts every chapter with initiative.

For extra challenge, mix and match any of the following modifiers:

- **Fleet Readiness**: during setup, place 1 extra ship in each system with bot pieces
- **Strategic Reserves**: during setup, give bot 1 extra random resource
- **Armored Hulls**\*: bot's fresh ships are Tough. they take 2 hits to damage (but damaged ships only take 1 hit to destroy)
- **Energy Shields**\*: all bot's ships are Tough
- **Carrier Tactics**\*: attacker must damage all ships before destroying any of them
- **Fortress Vaults**\*: treat bot's 1 key resource slots as having 2 keys for all purposes
- **Warp Blockades**: bot controls gates with a single fresh ship (regardless of number of fresh player ships). if more than one bot in play, bot with more fresh ships controls the gate

\*apply only if player is the attacker

<#ifdef base>
<div class="pagebreak"></div>
<#endif>
