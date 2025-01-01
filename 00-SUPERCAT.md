## a procedural non-player system for solo Arcs

*version 0.1.1*

This is a non-player system, or "bot", for playing the board game Arcs. It's intended for solo, i.e. one player versus one or more bots. It could be used as the 3rd or 4th player in a multiplayer game, but that was not the goal and has not been seriously tested.

## Components

You will need some way to track two numbers per bot, for instance two dice of different colors rotated to show a specific number face up. These are referred to as "counters" in the rules. You will also separately need one six sided die.

## Setup

Follow the instructions in the Arcs rulebook for your desired player count. If using the optional difficulty mode (see next page), the player will be last in turn order and one bot will start with the initiative; if playing with other bots, they will take the remaining positions in turn order.

## Playing a chapter

Shuffle the action deck and deal the player 6 cards. Place the remaining cards in a face down stack. Place a counter on each bot's board, with a value of 6. This represents the number of cards in the bot's hand. On the bot's turn, reveal two cards from this stack, and decrement the counter. The bot will play one of these cards, and discard the other. The procedures on the following pages will instruct you on how to select a card, and how to execute the bot's turn.

If at any time the stack runs out, shuffle the discard pile before revealing 2 cards. If at any time the bot gains an action card, place the card near the bot's player board, and increment the hand counter. Play card(s) gained as the last card(s) of the round. When the bot seizes initiative, decrement the counter to represent the bot discarding an extra card. Continue until the player has no cards and each bot's hand counter is at zero.

<div class="pagebreak"> </div>

## How to follow the procedures

The procedures use some special vocabulary that is specific to SUPERCAT. See the "Terminology" page for explanations of words which appear like this: <ins>contend</ins>.

Start with the "Bot Turn" page and read from top to bottom. Follow the instructions, executing statements if possible. When posed with a yes or no question, evaluate the situation, and follow the nested steps.

When taking actions using multiple pips from a card, follow the procedures to take as many actions as indicated. If action pips remain, restart the procedure from the top, re-evaluating questions from top to bottom.

Aside from the changes to card play described above, and the additional advantages below, the bot will follow every rule in the game.

## Difficulty mode (Optional but recommended)

The procedures attempt to simulate good play, but the bot cannot plan multiple cards ahead nor execute combos using guild abilities. To compensate and make for a more challenging game, give the bot additional advantages when the bot does not have more power than the player:

- **Efficient Logistics**: bot performs 1 extra action per card
- **Elite Pilots**: bot collects 1 extra die during Battle

When the bot is tied for first place it does not have more power than the player, so these advantages apply at the start of a game to all bots.

For an even harder game:

- Apply the above advantages even if the bot is ahead in power.
- The bot with the most power starts every chapter with initiative.

<div class="pagebreak"> </div>
