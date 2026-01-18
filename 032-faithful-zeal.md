<#ifdef campaign>
# Faithful Zeal - Move | Influence | Battle | Tax

✦ Can bot Tax or favorable combat to contend a declared ambition? <span style="font-size: 12px;">[1,4]</span>

<#ifdef base>
✦ Does bot have no starport and no claims?

- Can bot Move to get new claims? <span style="font-size: 12px;">[7]</span>
<#endif>

<#ifdef campaign>
✦ Does bot have no starport and either no claims or cannot Build upgrades/armor at the Flagship planet?

- Can bot Move to get new claims, or get Flagship to a planet matching unbuilt upgrades/armor? <span style="font-size: 12px;">[8]</span>
<#endif>

✦ Are any Loyal buildings controlled by a Rival?

- Can bot Move or favorable combat to change control? <span style="font-size: 12px;">[11,12]</span>

✦ Can bot Influence to defend Loyal agents on a contested card? <span style="font-size: 12px;">[13]</span>

<#ifdef campaign>
✦ Is it the last Chapter of Act I or Act II?

- Can bot Move fresh ships to Loyal buildings where Blight and no fresh ships? <span style="font-size: 12px;">[15]</span>
<#endif>

<#ifdef campaign>
✦ Can bot favorable combat vs fresh Blight at Loyal building or claim? <span style="font-size: 12px;">[16]</span>
<#endif>

<#ifdef base>
✦ Does bot have unbuilt cities and fewer claims than unbuilt cities?

- Can bot Move to get at least one new claim? <span style="font-size: 12px;">[19]</span> Prefer:
	- new resources
	- unclaimed
	- two slot planets
<#endif>

<#ifdef campaign>
✦ Does bot have unbuilt cities and either fewer claims than half the number of unbuilt cities or cannot Build upgrades/armor at the Flagship planet?

- Can bot Move to get at least one new claim or get Flagship to planet matching unbuilt upgrades/armor
? <span style="font-size: 12px;">[20]</span> Prefer:
	- new resources
	- unclaimed
	- two slot planets
<#endif>

✦ Can bot use an ability on a ready Guild or lore card?

✦ Can bot Influence a critical card? <span style="font-size: 12px;">[24]</span>

<#ifdef campaign>
✦ Could bot contend a declared ambition via the Imperial Trust?

- Can bot Influence the Imperial Council? <span style="font-size: 12px;">[25]</span>
<#endif>

<#ifdef campaign>
✦ Can bot Move to take control of Rival city or Free city? <span style="font-size: 12px;">[28]</span>
<#endif>

<#ifdef base>
✦ Can bot Move to take control of Rival city? <span style="font-size: 12px;">[29]</span>
<#endif>

✦ Can bot Tax to contend an undeclared ambition, to take captives, or to grow a lead in a declared ambition? <span style="font-size: 12px;">[37,38,39]</span>

✦ Can bot favorable combat to contend an undeclared ambition? <span style="font-size: 12px;">[42]</span>

✦ Can bot Influence any other card? <span style="font-size: 12px;">[43]</span>

✦ Can bot Move to change control of a Rival-controlled gate? <span style="font-size: 12px;">[44]</span> Prefer:

- take control adjacent to Rival starport
- take or neutralize control adjacent to Loyal starport

✦ Are there any ships not controlling gates or claims or Rival buildings?

- Can bot Move unassigned ships to task force (use partial move)? <span style="font-size: 12px;">[45]</span>

✦ Can bot Tax to gain any other resources? <span style="font-size: 12px;">[46]</span> Prefer:

- new resources
- grow a lead in an undeclared ambition

<div class="pagebreak"> </div>
<#endif>
