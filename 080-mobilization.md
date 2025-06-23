# Mobilization - Move | Influence

✦ (ignore for Flagship) Does bot have no starport and no claims?

- Can bot Move to get new claims? <span style="font-size: 12px;">[10]</span>

<#ifdef campaign>
✦ (Flagship only) Does bot have no starport and cannot Build upgrades or armor at the Flagship planet?

- Can bot Move Flagship to planet matching unbuilt upgrades or armor? <span style="font-size: 12px;">[11]</span>
<#endif>

✦ Are any loyal buildings controlled by a rival?

- Can bot Move to change control? <span style="font-size: 12px;">[14]</span>

✦ (ignore for Flagship) Does bot have unbuilt cities and fewer claims than <#ifdef base>unbuilt cities<#endif><#ifdef campaign>half number of unbuilt cities<#endif>?

- Can bot Move to get at least one new claim? <span style="font-size: 12px;">[18]</span> Prefer:
	- new resources
	- unclaimed
	- two slot planets

<#ifdef campaign>
✦ (Flagship only) Does bot have unbuilt cities and cannot Build upgrades or armor at the Flagship planet?

- Can bot Move Flagship to planet matching unbuilt upgrades or armor? <span style="font-size: 12px;">[19]</span>
<#endif>

✦ Can bot use an ability on a ready Guild or lore card?

<#ifdef base>
✦ Can bot Influence a card? <span style="font-size: 12px;">[26]</span> Prefer:

- defend Loyal agents on contested card
- icon to contend a declared ambition, if Secured
- icon to contend an undeclared ambition, if Secured
- effective Vox
- Weapon icon
- icon to grow a lead in a declared ambition
<#endif>

<#ifdef campaign>
✦ Can bot Influence a card? <span style="font-size: 12px;">[27]</span>
<#endif>

<#ifdef campaign>
✦ Would bot contend a declared ambition with the Imperial Trust?

- Can bot Influence the Imperial Council? <span style="font-size: 12px;">[28]</span>
<#endif>

<#ifdef campaign>
✦ Can bot Move to take control of rival city or Free city? <span style="font-size: 12px;">[31]</span>
<#endif>

<#ifdef base>
✦ Can bot Move to take control of rival city? <span style="font-size: 12px;">[32]</span>
<#endif>

✦ Can bot Move to change control of a rival-controlled gate? <span style="font-size: 12px;">[44]</span> Prefer:

- take control adjacent to rival starport
- take or neutralize control adjacent to loyal starport

✦ Are there any ships not controlling gates or claims or rival buildings?

- Can bot Move to unassigned ships to task force (use partial move)? <span style="font-size: 12px;">[45]</span>

<div class="pagebreak"> </div>
