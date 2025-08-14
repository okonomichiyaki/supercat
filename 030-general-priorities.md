# General Priorities
<#ifdef campaign>
✦ Check bot's Fate for initial priorities. If no card selected, return to this page.
<#endif>
✦ <!-- priority=1 --> Can bot Secure or Tax to contend declared ambition? → Administration/Aggression

✦ <!-- priority=1.5 --> Can bot Secure an effective Vox card<#ifdef campaign>, the Imperial Council, or Secure a card with an attached Faithful or Guild card<#endif>? → Aggression

✦ <!-- priority=2 --> Can bot favorable combat to contend declared ambition? → Combat card

✦ Does bot have no starport? <#ifdef campaign>*(if Flagship, none on Flagship board, else none on map)*<#endif>

- Can bot build a starport?
	- <!-- Build starport priority=3 --> Yes: → Construction
	- <!-- Expand for starport priority=3 --> No: → Mobilization/Aggression

✦ Are any loyal buildings in a system controlled by a rival?

- <!-- priority=4 --> Can bot Move to change control? → Mobilization/Aggression
- <!-- priority=4 --> Can bot Build or Repair to change control? → Construction/Administration
- <!-- priority=4 --> Can bot favorable combat to change control? → Combat card

✦ Does bot have unbuilt cities?
<#ifdef campaign>
- Does bot have a Flagship?
	- Can bot Build an upgrade/armor at the current planet? → Construction
	- Can bot Move to a planet matching an unbuilt upgrade/armor? → Mobilization/Aggression
- Does bot have fewer claims than half the number of unbuilt cities, rounded down?
	- Yes: <!-- Expand for city priority=5 --> Can bot move to get a new claim? → Mobilization/Aggression
	- No: <!-- Build city priority=5 --> Does bot have at least one claim? → Construction
<#endif>
<#ifdef base>
- Does bot have fewer claims than unbuilt cities?
	- Yes: <!-- Expand for city priority=5 --> Can bot move to get a new claim? → Mobilization/Aggression
	- No: <!-- Build city priority=5 --> Does bot have at least one claim? → Construction
<#endif>

✦ Can bot use an ability on a ready Guild or lore card? → Select suit matching ability, then exhaust card. Use ability, then go to page for card's suit if actions remaining.

✦ <!-- priority=6 --><!-- priority=7 --> Can bot Tax or Secure to contend undeclared ambition, take captives, or grow a lead in a declared ambition? <br>→ Administration/Aggression

✦ <!-- priority=8 --><!-- priority=9 --> Can bot Influence a card with more agents than rivals? → Mobilization/Administration
<#ifdef campaign>
✦ <!-- priority=9.5 --> Would bot contend a declared ambition with the Imperial Trust, and can bot Influence the Imperial Council with more agents than rivals? → Mobilization/Administration
<#endif>
✦ <!-- priority=10 --> Can bot Move or favorable combat to take control of rival city <#ifdef campaign>or Free city<#endif>?<br/> → Mobilization/Aggression

✦ <!-- priority=11 --><!-- priority=12 --> Can bot Build or Repair ships? → Construction/Administration

<div class="pagebreak"> </div>
