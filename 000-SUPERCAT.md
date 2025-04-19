## a procedural non-player system for solo Arcs

*version 0.4-DRAFT<!-- TODO -->*

This is a non-player system, or "bot", for playing the board game Arcs. It is intended for solo play, i.e. one player versus one or more bots. It can also work as the 3rd or 4th opponent in a multiplayer game. There are two versions of the this document; this is the <#ifdef base>base game<#endif><#ifdef campaign>campaign<#endif> version. <#ifdef campaign>*(Note: it currently only supports "A" Fates through Act I)*<#endif>

## Components

You will need some way to track <#ifdef base>two<#endif><#ifdef campaign>several<#endif> numbers per bot, for instance dice of different colors rotated to show a different numbered face. <#ifdef campaign>For a solo game vs 3 bots, you will need 3 dice each of red, blue, yellow, and white, and 3 dice each of two other colors.<#endif><#ifdef base>You will also separately need one six sided die.<#endif>

<#ifdef base>
## Setup

Choose a difficulty mode (see next page) which will determine turn order. For options to play with Leaders and Lore, see the related page at the end of the rules. Then setup the game according to the Arcs rulebook.
<#endif>
<#ifdef campaign>
## Setup (Act I)

Choose a difficulty mode (see page 3) which will determine turn order. Set up the game according to the Blighted Reach rulebook, but make changes at the steps listed below.

**1.B.** If playing on "normal" or "harder" difficulty, give the initiative marker to a bot, and seat the player(s) last in turn order.

**2.B.** Assign "A" Fates using any method you like. Suggestion: Each player draws 2 "A" Fate cards and chooses one secretly as in a multiplayer game, then assign each bot an "A" Fate card selected randomly from the remaining cards.

**2.G-H.** When the bot places a building, randomly select an empty building slot from among those eligible. The first building each bot places will be a city and the second will be a starport. *If a bot is the Believer, check that Fate's procedures for special instructions.*

**2.J.** Deal 6 action cards to each player, but do not deal action cards to the bot(s), instead place a counter on each bot board, showing a value of 6.

**2.K.** All action cards not in player hands form a single face down stack near the board.
<#endif>

## Playing a chapter

<#ifdef base>Shuffle all actions cards and deal the player 6 cards. Place the remaining cards in a single face down stack. Place a counter on each bot's board, with a value of 6. <#endif>The counter on the bot board represents the number of cards in the bot's hand. On the bot's turn, reveal two cards from the face down stack, and decrement the counter. The bot will play one of these cards, and discard the other. The procedures on the following pages will instruct you on how to select a card, and how to execute the bot's turn.

If at any time the stack runs out, shuffle the discard pile <#ifdef campaign>(excluding Event cards)<#endif> before revealing 2 cards. If at any time the bot gains an action card, place the card near the bot's board, and increment the hand counter. Include any extra card(s) with those drawn on each bot turn when considering its options. When the bot seizes initiative, decrement the counter to represent the bot discarding an extra card. Continue until the player has no cards and each bot's hand counter is at zero.
<#ifdef campaign>
At the end of the chapter, shuffle all action cards from the discard pile, any remaining in the stack, and any set aside Event cards before dealing cards to the player(s).
<#endif>
<#ifdef base><div class="pagebreak"> </div><#endif>

## How to follow the procedures

Start with "Bot Turn" and follow the instructions, executing statements if possible. When posed with a question, evaluate the situation and follow the nested steps. For more detailed explanation of interpreting nested procedures, see "Questions" at the end of the rules.

When directed, use "General Priorities" to select a card: Lead, Pivot, or Copy with the indicated suit from bot's options. If suit is not available, proceed to next question. Once a card has been selected, go to the page for the selected card's suit.

When multiple actions are available, first spend actions according to highest priority, then if actions remaining, restart the procedure from the top of the page.

The procedures use some special vocabulary that is specific to SUPERCAT. See the "Terminology" page for explanations of words like <ins>contend</ins>. When rounding fractions, round down unless otherwise specified.

Aside from the changes to card play described above, <#ifdef campaign>the negotiation mini game, some special handling of certain Fate abilities,<#endif> and the additional advantages below, the bot will follow every rule in the game.

<#ifdef campaign><div class="pagebreak"> </div><#endif>

## Difficulty mode (Optional but recommended)

For a more challenging game, start each game with the player last in turn order, and give the bot some additional advantages when it does not have more power than the player:

- **Efficient Logistics**: bot performs 1 extra action per card
- **Elite Pilots**: bot collects 1 extra die during Battle

*Note: If the bot is tied with the player, it does not have more power, and will gain these advantages, including at the start of the game when all power markers are tied at zero.*

Relative power should be evaluated per bot, so in a game with 2 bots, if one bot is ahead of the player, and the other is behind, apply these only to the losing bot. In a multiplayer game, check power between bots and players: grant the bot advantages when it is behind all players.

For an even harder game:

- Apply the above advantages even if the bot is ahead in power.
- The bot with the most power starts every chapter with initiative.

<#ifdef campaign>
## Grievances (Optional but recommended)

This should be considered an optional but recommended rule. It will add a little bit of extra friction for the solo player as well as some texture to the negotiation mini game.

Each bot will have a grievance counter matching the colors of all other bots and players. For instance, in a game with 1 player and 3 bots, a bot using the red pieces will track grievances in white, blue, and yellow. At the beginning of the game, the value of these is all zero.

Certain actions taken against a bot, by a player or other bot, will result in a grievance. The target of the action will gain one or more grievance matching the source. Each of the following results in the target gaining one grievance:

* Battle action with bot as the defender
* destroy one or more bot pieces (limit 1 per action)
* steal a resource or guild card from the bot (limit 1 per action)
* target bot city with a Tax action
* take one or more bot agents captive (limit 1 per action)
<div class="pagebreak"> </div>
