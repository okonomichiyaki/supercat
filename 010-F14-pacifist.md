<#ifdef campaign>
# Pacifist

## All Acts

Battle and Trophies
: Bot will avoid Battle actions if there is any chance of taking trophies. *(in other words, will avoid most battles except in some rare cases may raid, if target has 1 key and defender has 2 buildings present)* Bot will reject Transfer Asset offers which give the bot Trophies, except for Loyal pieces.

Secure and Tax and Captives
: Bot will avoid Secure and Tax actions that would take captives. Bot will reject Transfer Asset offers which give the bot Captives, except for Loyal pieces.

Influence
: Bot will avoid Influencing contested cards with more agents than Rivals. Bot will only Influence contested cards to defend own agents up to number of Rival agents.

## Act II

✦ Can bot Move a Witness token to a Psionic planet?

- Prefer: Psionic planet where bot will have control at the end of the move.

✦ Can bot Build, Repair, or Move to take control of a Witness token?

- Prefer: Witness token at a Psionic planet

Witnesses
: Bot will always use the Prelude ability to take a Witness if possible, but only declare Empath if not already declared and only if bot is contending for Empath.

Well of Empathy
: Bot will place Psionic resources first in 3 key slots, then place them on this card.

Prelude
: If Empathy is declared, bot will spend Psionic resources if doing so will advance its objective and will not change the bot's place for Empath. Additionally, bot will spend resources to enable it to use the Prelude ability above on the same turn. Limit one resource per Witness token. *(e.g. spend a Fuel to Move a Witness to a Psionic planet under bot control, or spend a Material to Build and get control of a Witness already at a Psionic planet)*

Govern the Imperial Reach
: Bot will change if current Policy is A Policy of War.

## Act III

Empath and Psionic resources
: If bot is winning Empath, and A > G, then keep Psionic resources. Otherwise, spend Psionics until Rivals have more Psionic resources than you.
<!-- TODO: Otherwise? -->

Govern the Imperial Reach
: Bot will enforce or change to A Policy of Escalation.

<div class="pagebreak"> </div>
<#endif>
