# Movement Doctrine

When moving ships, the bot will follow these guidelines.

Each movement has an origin, a destination, and a goal. The procedures will define a specific goal, for example changing control of a system with loyal buildings. The goal will define one or more destinations. The specific destination and origin should be selected according to the priorities below.

In rare cases, the bot will not reach its destination on a single card. These are called <ins>partial moves</ins> and the bot will only make moves like this if explicitly instructed to. In these circumstances, evaluate destinations and goals independently each time the bot plays a card, as the priorities may change on a future movement.

## Priorities:

Use <ins>task force</ins> for any moves, if possible. Otherwise, move as many ships as possible, including damaged ships.

When possible, retain control of the origin system. If it's not possible to reach the destination and achieve the goal while retaining control of the origin, check for other origins. If it's not possible to retain control of any origin, abandon control.

If multiple origins and destinations meet above criteria, first choose the shortest path (i.e. spend fewest action). Then, if multiple origins and destinations still eligible, choose randomly.

<div class="pagebreak"> </div>
