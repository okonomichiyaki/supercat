# General Priorities
<#ifdef campaign>
✦ Check bot's Fate for initial priorities. If no card selected, return to this page.
<#endif>
✦ Can bot Secure or Tax to contend declared ambition? → Administration/Aggression

✦ Can bot Secure an effective Vox card<#ifdef campaign>, the Imperial Council, or Secure a card with an attached Faithful or Guild card<#endif>? → Aggression

✦ Can bot favorable combat to contend declared ambition? → Combat card

✦ Does bot have no starport? <#ifdef campaign>*(if Flagship, none on Flagship board, else none on map)*<#endif>

- Can bot build a starport?
	- Yes: → Construction
	- No: → Mobilization/Aggression

✦ Are any loyal buildings in a system controlled by a rival?

- Can bot Move to change control? → Mobilization/Aggression
- Can bot Build or Repair to change control? → Construction/Administration
- Can bot favorable combat to change control? → Combat card

✦ Can bot favorable combat vs fresh Blight at Loyal building or claim? → Combat card

✦ Does bot have unbuilt cities?
<#ifdef campaign>
- Does bot have a Flagship?
	- Can bot Build an upgrade/armor at the current planet? → Construction
	- Can bot Move to a planet matching an unbuilt upgrade/armor? → Mobilization/Aggression
- Does bot have fewer claims than half the number of unbuilt cities, rounded down?
	- Yes: Can bot move to get a new claim? → Mobilization/Aggression
	- No: Does bot have at least one claim? → Construction
<#endif>
<#ifdef base>
- Does bot have fewer claims than unbuilt cities?
	- Yes: Can bot move to get a new claim? → Mobilization/Aggression
	- No: Does bot have at least one claim? → Construction
<#endif>

✦ Can bot use an ability on a ready Guild or lore card? → Select suit matching ability, then exhaust card. Use ability, then go to page for card's suit if actions remaining.

✦ Can bot Tax or Secure to contend undeclared ambition, take captives, or grow a lead in a declared ambition? <br>→ Administration/Aggression

✦ Can bot Influence a card with more agents than rivals? → Mobilization/Administration
<#ifdef campaign>
✦ Would bot contend a declared ambition with the Imperial Trust, and can bot Influence the Imperial Council with more agents than rivals? → Mobilization/Administration
<#endif>
✦ Can bot Move or favorable combat to take control of rival city <#ifdef campaign>or Free city<#endif>?<br/> → Mobilization/Aggression

✦ Can bot Build or Repair ships? → Construction/Administration

<div class="pagebreak"> </div>
