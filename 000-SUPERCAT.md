## a procedural non-player system for solo Arcs

*version 0.6-draft*

This is a non-player system, or "bot", for playing the board game Arcs. It is intended for solitaire play, i.e. one player versus one or more bots. It can also work as the 3rd or 4th opponent in a multiplayer game. There are two versions of the this document; this is the <#ifdef base>base game<#endif><#ifdef campaign>Blighted Reach campaign<#endif> version. <#ifdef campaign>*(note: it currently only supports "A" and "B" Fates through Act II)*<#endif>

This is not an "automa", but instead a simulation-style bot which attempts to interact with all of the rules of the original game. The bot breaks the rules only in the following ways:

- the bot's hand of cards is abstracted to retain some uncertainty and "fog of war"
- there are optional difficulty modifiers to make the solo experience more challenging
<#ifdef campaign>- some Fates use special rules for mechanics which are awkward in a solo context<#ifdef campaign>

<#ifdef campaign>
*If this is your first time playing Arcs using SUPERCAT, consider playing at least one chapter of the base game using this system before using it to play the campaign.*
<#endif>

## Components

You will need some way to track <#ifdef base>two<#endif><#ifdef campaign>several<#endif> values per bot, for instance dice of different colors rotated to show a different number faceup. These can be six sided dice (only in rare situations will the values exceed six) but could also be eight or ten sided dice (they are never rolled). These are referred to as "counters" in the rules that follow.
<#ifdef base>
You will separately need one six sided die which will be rolled for a random number.
<#endif>
<#ifdef campaign>
You will need at least two counters per bot, and if playing with the optional Grievances mechanic, you will need red, blue, yellow, and white counters for each bot.
*(some Fates require additional components: see Pathfinder for details)*
<#endif>

<div class="pagebreak"> </div>

<#ifdef base>
## Setup

Choose difficulty modifiers (below) which will determine turn order. For options to play with Leaders and Lore, see the related page at the end of the rules. Then setup the game according to the Arcs rulebook, but deal cards according to "Playing a chapter" on the next page.
<#endif>

<#ifdef campaign>
## Act I Setup

Choose difficulty modifiers (below) which will determine turn order. Set up the game according to the Blighted Reach rulebook, but make changes at the steps listed below.

**1.B.** If playing on "normal" or "harder" difficulty, give the initiative marker to a bot, and seat the player(s) last in turn order.

**2.B.** Assign "A" Fates using any method you like. *(suggestion: the player draws 2 "A" Fate cards and chooses one, then randomly assign each bot an "A" Fate card)*

**2.G-H.** When the bot places a building, randomly select an empty building slot from among those eligible. The first building each bot places will be a city and the second will be a starport. *If a bot is the Believer, check that Fate's procedures for special instructions.*

**2.J.** Deal 6 action cards to each player, but do not deal action cards to the bots, instead place a counter on each bot board, showing a value of 6.

**2.K.** All action cards not in player hands form a single face down stack near the board.
<#endif>

## Difficulty modifiers (Optional but recommended)

For a more challenging game, start each game with the player last in turn order, and give the bot some additional advantages when it does not have more power than the player:

- **Efficient Logistics**: bot performs 1 extra action per card
- **Elite Pilots**: bot collects 1 extra die during Battle

*Note: If the bot is tied with the player, it does not have more power, and will gain these advantages, including at the start of the game when all power markers are tied at zero.*

Relative power should be evaluated per bot, so in a game with 2 bots, if one bot is ahead of the player, and the other is behind, apply these only to the losing bot. In a multiplayer game, check power between bots and players: grant the bot advantages when it is behind all players.

For an even harder game:

- Apply the above advantages even if the bot is ahead in power.
- The bot with the most power starts every chapter with initiative.

<div class="pagebreak"> </div>

## Playing a chapter

<#ifdef base>Shuffle all actions cards and deal the player 6 cards. Place the remaining cards in a single face down stack. Place a counter on each bot's board, with a value of 6. <#endif>The counter on the bot board represents the number of cards in the bot's hand. On the bot's turn, reveal two cards from the face down stack, and decrement the counter. The bot will play one of these cards, and discard the other. The procedures on the following pages will instruct you on how to select a card, and how to execute the bot's turn.

If at any time the stack runs out, shuffle the discard pile <#ifdef campaign>(excluding Event cards)<#endif> before revealing 2 cards. If at any time the bot gains an action card, place the card near the bot's board, and increment the hand counter. Include any extra card(s) with those drawn on each bot turn when considering its options. When the bot seizes initiative, decrement the counter to represent the bot discarding an extra card. Continue until the player has no cards and each bot's hand counter is at zero.
<#ifdef campaign>
At the end of the chapter, shuffle all action cards from the discard pile, any remaining in the stack, and any set aside Event cards before dealing cards to the player(s).
<#endif>

## How to follow the procedures

Start with "Bot Turn" and follow the instructions, executing statements if possible. When posed with a question, evaluate the situation and follow the nested steps. For more detailed explanation of interpreting nested procedures, see "Questions" at the end of the rules.

When directed, use "General Priorities" to select a card: Lead, Pivot, or Copy with the indicated suit from bot's options. If suit is not available, proceed to next question. Once a card has been selected, go to the page for the selected card's suit.

When multiple actions are available, first spend actions according to highest priority, then if actions remaining, restart the procedure from the top of the page.

The procedures use some special vocabulary that is specific to SUPERCAT. See the "Terminology" page for explanations of words like contend. When rounding fractions, round down unless otherwise specified.

Aside from the changes to card play described above, <#ifdef campaign>the negotiation minigame, some special handling of certain Fate abilities,<#endif> and the additional advantages below, the bot will follow every rule in the game.

## Decision making for the bot

When the bot needs to make a decision but there are multiple options, the solo player may need to make some decisions. Follow these rules to resolve multiple options for the bot.

Actions
: When selecting an action from multiple options to achieve the same goal, actions will be listed in priority order. For example, in the procedure "Can bot Secure or Tax to contend declared ambition", the bot will prefer to Secure rather than Tax if both are an option.

Goals
: Similarly, there are multiple goals, they are also listed in priority order. For example, in the procedure "Can bot Secure to contend an undeclared ambition, to take captives, or to grow lead in declared ambition", the bot will prefer to contend an undeclared ambition before growing a lead in a declared ambition.

Prefer
: Some actions have extra guidance in the form of "preferences", indicated with the word "Prefer" and a list of priorities. Use these priorities to decide between multiple options. Narrow the possibilities to only those which meet the first priority, then the second priority, and so on, until only one option remains.

Random
: If the bot has multiple options and the procedures do not give explicit preferences, or those priorities fail to differentiate between the options, pick randomly.

## Clarifications

The concept of contending ambitions is important. This is a special keyword: to contend an ambition means take any action which improves the bot's position for that ambition AND the bot is in second or first place, including ties.

There is a difference between contending an ambition and "winning or tied for first place", which is that contending also includes second place and tied for second place. The bot will only declare an undeclared ambition if it is winning or tied for first place; it will not declare an ambition if it is in second place.

Furthermore, the bot will only declare an ambition which has already been declared (double or triple declare to add second or third marker to the ambition box) if it is **winning** the ambition. It will not double or triple declare if it is tied for first place.

<div class="pagebreak"> </div>
