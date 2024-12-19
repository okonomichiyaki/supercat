## a procedural non-player system for Arcs

*version 0.1*

This is a non-player system, or "bot", for playing the board game Arcs. It's intended for playing solo (one player versus one or more bots), but it can also be used in a multiplayer game.

## Components

You will need a way to track two numbers per bot, for instance two dice of different colors rotated to show a specific number face up. They are referred to as "counters" in the rules.

## Setup

Follow the instructions in the Arcs rulebook for your desired player count. If playing on "normal" difficulty, the player(s) will always be last in turn order with the bot(s) starting with the initiative.

## Playing a chapter

Shuffle the action deck and deal each player(s) 6 cards. Place the remaining cards in a face down stack. Place a counter on each bot's board, with a value of 6. This represents the number of cards in the bot's hand. On the bot's turn, reveal two cards from this stack, and decrement the counter. The bot will play one of these cards, and discard the other. The procedures on the following pages will instruct you on how to select a card, and how to execute the bot's turn.

If at any time the stack runs out, shuffle the discard pile before revealing 2 cards. If at any time the bot gains an action card, place the card near the bot's player board, and increment the hand counter. Play card(s) gained as the last card(s) of the round. When the bot seizes initiative, decrement the counter to represent the bot discarding an extra card. Continue until the player has no cards and each bot's hand counter is at zero.

<div class="pagebreak"> </div>

## Additional advantages

At the beginning of a chapter, check the relative power of the bot(s) and player. If a bot is not ahead of the player, during this chapter the bot will gain the following advantages:

- Efficient Logistics: bot has 1 extra action per card
	- if lead card: number of pips plus 1
	- if pivot or copy: 2 actions
- Elite Pilots: bot collects 1 extra die during Battle

In this context, tied for first place does not count as ahead, so these advantages apply at the start of a game to all bots.

For a harder game:

- Apply the above advantages even if the bot is ahead in power.
- The bot with the most power starts every chapter with initiative.

For an easier game:

- Do not apply the above advantages even if the bot is behind in power.
- Randomly assign initiative at the start of the game.

## How to follow the procedures

The procedures use some special vocabulary that is specific to SUPERCAT. See the "Terminology" page for explanations of words like <ins>contend</ins>.

Start with the "Bot Turn" page and read from top to bottom. Follow the instructions, executing statements if possible. When posed with a yes or no question, evaluate the situation, and follow the nested steps.

When taking actions using multiple pips from a card, follow the procedures to take as many actions as indicated. If action pips remain, restart the procedure from the top, re-evaluating questions from top to bottom.

Aside from the changes described above, the bot will follow every rule in the game.

<div class="pagebreak"> </div>
