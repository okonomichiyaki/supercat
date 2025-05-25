# Movement Principles

When moving ships, the bot will follow these guidelines. Note that this page covers movement generally; for specific guidance on bot behavior around when the bot will seek to get new claims and build cities, see the "Expansion Principles". That page explains **when** the bot will expand while this one describes **how** movement is carried out.

Each movement has an origin, a destination, and a goal. The procedures will define a specific goal, for example changing control of a system with loyal buildings. The goal will define one or more destinations. The specific destination and origin should be selected according to the priorities below.

In rare cases, the bot will not reach its destination on a single card. These are called partial moves and the bot will only make moves like this if explicitly instructed to. In these circumstances, evaluate destinations and goals independently each time the bot plays a card, as the priorities may change on a future movement.

## Priorities:

Select origin and destination which takes the shortest path (i.e. spend fewest action). Move as many ships from the origin while following the priorities below, including damaged ships.

When possible, retain control of the origin system. If it's not possible to reach the destination and achieve the goal while retaining control of the origin, check for other origins. If it's not possible to retain control of any origin, abandon control of origin.

If multiple origins and destinations meet above criteria, use these priorities:

- if goal is not new claims, prefer destinations which result in new claims
- if goal is not control, prefer destinations which result in bot control of rival <#ifdef campaign> or Free <#endif> city.
- if otherwise equal options, select task force as the origin system

<#ifdef campaign>
When destination contains Blight and Imperial ships not present at destination, bring Imperial ships if possible. Otherwise, leave Imperial ships to retain Empire control if including them in the move would give rival control of loyal building.
<#endif>

<div class="pagebreak"> </div>
