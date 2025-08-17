# Combat Principles

When asked if bot can favorable combat, first identify the goal <#ifdef base>(Trophies, Raid, or Control)<#endif><#ifdef campaign>(Trophies, Raid, Control, or Defense vs Fresh Blight)<#endif> and then refer to the corresponding section below. Bot will spend Weapons to enable Battle and will spend Fuel or Psionics to enable more than one Battle action at target (up to two Battle actions).

A combat which risks outrage is favorable only if bot can ransack the court AND if bot is not contending a matching declared ambition<#ifdef campaign> AND bot has no matching protected cards<#endif>. Ransack card which results in the most trophies. If bot is able to re-roll, first re-roll intercepts, then re-roll blanks.

## Trophies

A Battle for trophies is considered favorable if bot has at least 1:1 ratio of fresh ships<#ifdef campaign> OR can roll 2 dice per Blight step<#endif>.

If bot has multiple actions, first roll all skirmish dice until ratio of fresh ships is better than 1:1, or only 1 action left. Then roll assault dice up to 2x defending fresh ships (up to 2x Blight steps), and the rest skirmish dice. Allocate hits prioritizing trophies *(hits to defender to maximize trophies taken, hits to self to minimize them)*.

## Raid

A raid is considered favorable if bot can roll raid dice equal to 2x keys on the target AND bot has better than 1:1 ratio of fresh ships to defender OR has 1:1 ratio AND more than one Battle action available after moving to the target.

If favorable, the bot will first spend actions to roll all skirmish dice, up to the last action available, when it will roll raid dice. Allocate hits like control.

## Control

A Battle for control is favorable is bot can roll at least 1 die per fresh defending ship. If favorable, bot will select dice like a trophies Battle. Bot will allocate hits to take or neutralize control, then allocate remaining hits to take trophies.

<#ifdef campaign>
## Defense vs Fresh Blight

A Battle to defend against fresh Blight is favorable if bot can roll at least 2 dice. If favorable, bot will select dice like a trophies Battle. Bot will allocate hits to damage fresh Blight first, then destroy damaged Blight.
<#endif>
<div class="pagebreak"> </div>
