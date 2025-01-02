## a procedural non-player system for solo Arcs

*version 0.2*

This is a non-player system, or "bot", for playing the board game Arcs. It's intended for solo play, i.e. one human player versus one or more bots. It should also work as the 3rd or 4th player in a multiplayer game, but that was not the goal and has not been rigorously tested.

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

Start with the "Bot Turn" page and read from top to bottom. Follow the instructions, executing statements if possible. When posed with a yes or no question, evaluate the situation, and follow the nested steps. For more detailed explanation of interpreting nested procedures, see Questions.

When taking actions using multiple pips from a card, follow the procedures to take as many actions as indicated. If action pips remain, restart the procedure from the top, re-evaluating questions from top to bottom.

Aside from the changes to card play described above, and the additional advantages below, the bot will follow every rule in the game.

## Difficulty mode (Optional but recommended)

The procedures attempt to simulate good play, but the bot cannot plan multiple cards ahead nor execute combos using guild abilities. To compensate and make for a more challenging game, start each game with the player last in turn order, and give the bot some additional advantages when it does not have more power than the player:

- **Efficient Logistics**: bot performs 1 extra action per card
- **Elite Pilots**: bot collects 1 extra die during Battle

If the bot is tied with the player, it does not have more power, and will gain these advantages. It's intended that this applies at the start of the game when all players have zero power.

Relative power should be evaluated per bot, so in a game with 2 bots, if one bot is ahead of the player, and the other is behind, apply these only to the losing bot. In a multiplayer game, check power between bots and humans: grant the bot advantages when it is behind all human players.

For an even harder game:

- Apply the above advantages even if the bot is ahead in power.
- The bot with the most power starts every chapter with initiative.

<div class="pagebreak"> </div>
