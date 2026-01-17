<#ifdef campaign>
# Magnate

## Act I

✦ Can bot Tax for any resource?

- Prefer:
	- resource matching any declared ambition
	- new resource

✦ Can bot Secure or Influence the Imperial Council?

- If Secured, call a Summit

Events
: If objective marker is greater than zero, events are urgent.

Summit Negotiations
: During the negotiation minigame, on the bot's turn it will use 2 negotiation rounds instead of only 1, and the bot will use this second round even if the first round succeeds. The bot will offer according to procedures described in the minigame, however the bot will only accept resources or favors.

Export to the Galactic Core
: If the bot has 3 or more resources at the end of the negotiation minigame, then discard 3 resources to advance objective, unless bot is currently contending a declared ambition matching those resources.

Prelude
: Do not spend resources for any Prelude actions if bot has 3 or fewer resources.

Merchant League
: When gaining resources prefer resources to contend ambitions. When conducting negotiations, prefer these resources for **Transfer Asset**.

<div class="pagebreak"> </div>

## Act II and III

(in Act II use the following procedures. in Act III, use the Act III only procedures first, then use these procedures)

✦ Can bot Tax or favorable battle for resources, resulting in the bot having more than half of the total resources of its type in play? *(get resources such that if the Gain Monopolies Edict were resolved, the bot take the matching Monopoly)*

- Prefer:
	- Resource matching Monopoly in the supply
	- Resource matching Monopoly held by a Rival
	- Resource matching Monopoly held by bot

✦ Is bot a Regent but not First Regent?

- If bot were First Regent, would bot have more than half of the total resources of a type in play via the Imperial Trust?

- Can bot Secure or Influence the Imperial Council?

✦ Would bot gain a Monopoly if the Edicts were resolved?

- Can bot Secure or Influence the Imperial Council?

Events
: If bot has more than half of any type of resource, and does not have the matching Monopoly, then Events are considered urgent.

Imperial Council Decided
: If bot would gain a Monopoly, bot will resolve Edicts.

Monopoly
: Bots holding a Monopoly will never consent to the matching resource type being given.
*(but can still be forced to consent by returning a favor)*

Prelude
: If bot has a matching Monopoly, or the matching Monopoly is in the supply, do not spend resources for Prelude actions.

## Act III only

✦ Is the Magnate a Regent? *(Is Closed Economy face up?)*

- Yes:
	- Can bot Move or Repair to get Imperial control of a Rival city?
		- Prefer: City matching Monopoly bot does not have
- No: *(Is Open Economy face up?)*
	- Can bot Build, Move, Repair or favorable combat to get control of a Rival city?

<div class="pagebreak"> </div>
<#endif>
