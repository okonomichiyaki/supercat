# General Priorities
<#ifdef campaign>
✦ Check bot's Fate for initial priorities. If no card selected, return to this page.
<#endif>
✦ Can bot Tax or Secure to contend declared ambition? → Administration/Aggression

✦ Can bot Secure an effective Vox card<#ifdef campaign>, the Imperial Council, or Secure a card with an attached Faithful or Guild card<#endif>? → Aggression

✦ Can bot favorable combat to contend declared ambition? → Combat card

✦ Does bot have no starport? <#ifdef campaign>*(if Flagship, none on Flagship board, else none on map)*<#endif>

- Can bot Build a starport? → Construction

✦ Does bot have no starport and no claims? <#ifdef campaign>*(ignore if Flagship)*<#endif>

- Can bot Move to get new claims? → Aggression/Mobilization

✦ Are any loyal buildings in a system controlled by a rival?

- Can bot Build or Repair to change control? → Construction/Administration
- Can bot Move to change control? → Mobilization/Aggression
- Can bot favorable combat to change control? → Combat card

<#ifdef campaign>
✦ Can bot favorable combat vs fresh Blight at Loyal building or claim? → Combat card
<#endif>

<#ifdef campaign>
✦ Does bot have unbuilt cities?

- Does bot have a Flagship?
	- Can bot Build an upgrade/armor at the current planet? → Construction
	- Can bot Move to a planet matching an unbuilt upgrade/armor? → Mobilization/Aggression
- Does bot have fewer claims than half the number of unbuilt cities, rounded down?
	- Yes: Can bot move to get a new claim? → Mobilization/Aggression
	- No: Does bot have at least one claim? → Construction
<#endif>
<#ifdef base>
✦ Can bot Build cities? → Construction

✦ Does bot have unbuilt cities and fewer claims than unbuilt cities?

- Can bot Move to get at least one new claim? → Mobilization/Aggression
<#endif>

✦ Can bot use an ability on a ready Guild or lore card?

- Select suit matching ability, then exhaust card.
- Use ability, then go to page for card's suit if actions remaining.

✦ Can bot Tax or Secure to contend undeclared ambition, take captives, or grow a lead in a declared ambition? → Administration/Aggression

✦ Can bot Influence a card with more agents than rivals? → Mobilization/Administration
<#ifdef campaign>
✦ Would bot contend a declared ambition with the Imperial Trust, and can bot Influence the Imperial Council with more agents than rivals? → Mobilization/Administration
<#endif>

✦ Can bot Build or Repair to take control of rival city <#ifdef campaign>or Free city<#endif>? → Construction/Administration

✦ Can bot Move or favorable combat to take control of rival city <#ifdef campaign>or Free city<#endif>? → Mobilization/Aggression

✦ Can bot Build or Repair any other ships? → Construction/Administration

<div class="pagebreak"> </div>
