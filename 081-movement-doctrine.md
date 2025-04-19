# Movement Doctrine

When moving ships, the bot will follow these guidelines.

Each movement has an origin, a destination, and a goal. The procedures will define a specific goal, for example changing control of a system with loyal buildings. The goal will define one or more destinations. The specific destination and origin should be selected according to the priorities below.

In rare cases, the bot will not reach its destination on a single card. These are called <ins>partial moves</ins> and the bot will only make moves like this if explicitly instructed to. In these circumstances, evaluate destinations and goals independently each time the bot plays a card, as the priorities may change on a future movement.

## Priorities:

Use <ins>task force</ins> for any moves, if possible. Otherwise, move as many ships as possible while following other priorities, including damaged ships.

When possible, retain control of the origin system. If it's not possible to reach the destination and achieve the goal while retaining control of the origin, check for other origins. If it's not possible to retain control of any origin, abandon control.

If multiple origins and destinations meet above criteria, use these priorities:

- shortest path (i.e. spend fewest action)
- if goal is not new <ins>claims</ins>, prefer destinations which result in new <ins>claims</ins>
- if goal is not control, prefer destinations which result in bot control of Rival<#ifdef campaign> or Free <#endif>city.

<#ifdef campaign>
When destination contains Blight and Imperial ships not present at destination, bring Imperial ships if possible. Otherwise, leave Imperial ships to retain Empire control if including them in the move would give Rival control of Loyal building.
<#endif>

<div class="pagebreak"> </div>
