# Mobilization - Move | Influence

✦ Does bot have no starport and no claims?

- Can bot Move to get new claims? <span style="font-size: 12px;">[5]</span>

<#ifdef campaign>
✦ Does bot have no starport and cannot Build upgrades or armor at the Flagship planet?

- Can bot Move Flagship to planet matching unbuilt upgrades or armor? <span style="font-size: 12px;">[6]</span>
<#endif>

✦ Are any Loyal buildings controlled by a Rival?

- Can bot Move to change control? <span style="font-size: 12px;">[9]</span>

✦ Can bot Influence to defend Loyal agents on a contested card? <span style="font-size: 12px;">[11]</span>

<#ifdef campaign>
✦ Is it the last Chapter of Act I or Act II?

- Can bot Move ships to Loyal buildings in systems with Blight and no ships? <span style="font-size: 12px;">[13]</span>
<#endif>

✦ Does bot have unbuilt cities and fewer claims than <#ifdef base>unbuilt cities<#endif><#ifdef campaign>half number of unbuilt cities<#endif>?

- Can bot Move to get at least one new claim? <span style="font-size: 12px;">[17]</span> Prefer:
	- new resources
	- unclaimed
	- two slot planets

<#ifdef campaign>
✦ Does bot have unbuilt cities and cannot Build upgrades or armor at the Flagship planet?

- Can bot Move Flagship to planet matching unbuilt upgrades or armor? <span style="font-size: 12px;">[18]</span>
<#endif>

✦ Can bot use an ability on a ready Guild or lore card?

✦ Can bot Influence a critical card? <span style="font-size: 12px;">[21]</span>

<#ifdef campaign>
✦ Would bot contend a declared ambition with the Imperial Trust?

- Can bot Influence the Imperial Council? <span style="font-size: 12px;">[22]</span>
<#endif>

<#ifdef campaign>
✦ Can bot Move to take control of Rival city or Free city? <span style="font-size: 12px;">[25]</span>
<#endif>

<#ifdef base>
✦ Can bot Move to take control of Rival city? <span style="font-size: 12px;">[26]</span>
<#endif>

✦ Can bot Influence any other card? <span style="font-size: 12px;">[39]</span>

✦ Can bot Move to change control of a Rival-controlled gate? <span style="font-size: 12px;">[40]</span> Prefer:

- take control adjacent to Rival starport
- take or neutralize control adjacent to Loyal starport

✦ Are there any ships not controlling gates or claims or Rival buildings?

- Can bot Move to unassigned ships to task force (use partial move)? <span style="font-size: 12px;">[41]</span>

<div class="pagebreak"> </div>
