# Aggression - Move | Battle | Secure

✦ Can bot Secure to contend a declared ambition? <span style="font-size: 12px;">[2]</span>

<#ifdef base>
✦ Can bot Secure an effective Vox card? <span style="font-size: 12px;">[3]</span>
<#endif>

<#ifdef campaign>
✦ Can bot Secure an effective Vox card or the Imperial Council? <span style="font-size: 12px;">[4,5]</span>
<#endif>

<#ifdef campaign>
✦ Can bot Secure a Faithful card or an attached Guild card? <span style="font-size: 12px;">[6,7]</span>
<#endif>

✦ Can bot favorable combat to contend a declared ambition? <span style="font-size: 12px;">[8]</span>

✦ Does bot have no starport and no claims?

- Can bot Move to get new claims? <span style="font-size: 12px;">[10]</span>

<#ifdef campaign>
✦ Does bot have no starport and cannot Build upgrades or armor at the Flagship planet?

- Can bot Move Flagship to planet matching unbuilt upgrades or armor? <span style="font-size: 12px;">[11]</span>
<#endif>

✦ Are any loyal buildings controlled by a rival?

- Can bot Move or favorable combat to change control? <span style="font-size: 12px;">[14,15]</span>

✦ Does bot have unbuilt cities and fewer claims than <#ifdef base>unbuilt cities<#endif><#ifdef campaign>half number of unbuilt cities<#endif>?

- Can bot Move to get at least one new claim? <span style="font-size: 12px;">[18]</span> Prefer:
	- new resources
	- unclaimed
	- two slot planets

<#ifdef campaign>
✦ Does bot have unbuilt cities and cannot Build upgrades or armor at the Flagship planet?

- Can bot Move Flagship to planet matching unbuilt upgrades or armor? <span style="font-size: 12px;">[19]</span>
<#endif>

✦ Can bot use an ability on a ready Guild or lore card?

✦ Can bot Secure to contend an undeclared ambition or to take captives? <span style="font-size: 12px;">[21,22]</span>

✦ Can bot Secure to grow lead in declared ambition? <span style="font-size: 12px;">[25]</span>

<#ifdef campaign>
✦ Can bot Move to take control of rival city or Free city? <span style="font-size: 12px;">[31]</span>
<#endif>

<#ifdef base>
✦ Can bot Move to take control of rival city? <span style="font-size: 12px;">[32]</span>
<#endif>

<#ifdef campaign>
✦ Can bot favorable combat to destroy Blight in systems with loyal buildings? <span style="font-size: 12px;">[99]</span>
<#endif>

✦ Are there any ambition markers available?

- Can bot favorable combat to take trophies? <span style="font-size: 12px;">[99]</span>

✦ Can bot Secure to grow lead in an undeclared ambition or to take any other cards? <span style="font-size: 12px;">[99]</span>

✦ Can bot Move to change control of a rival-controlled gate? <span style="font-size: 12px;">[99]</span> Prefer:

- take control adjacent to rival starport
- take or neutralize control adjacent to loyal starport

✦ Are there any ships not controlling gates or claims or rival buildings?

- Can bot Move to unassigned ships to task force (use partial move)? <span style="font-size: 12px;">[99]</span>

<div class="pagebreak"> </div>
