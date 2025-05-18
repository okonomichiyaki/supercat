# Mobilization - Move | Influence

✦ Does bot have no starport and no claims?

- <!-- priority=3 --> Can bot Move to get new claims? <span style="font-size: 12px;">(10)</span>

<#ifdef campaign>
✦ Does bot have no starport and cannot Build upgrades or armor at the Flagship planet?

- <!-- priority=3 --> Can bot Move Flagship to planet matching unbuilt upgrades or armor? <span style="font-size: 12px;">(11)</span>
<#endif>

✦ Are any loyal buildings controlled by a rival?

- <!-- priority=4 --> Can bot Move to change control? <span style="font-size: 12px;">(14)</span>

✦ Does bot have unbuilt cities and fewer claims than <#ifdef base>unbuilt cities<#endif><#ifdef campaign>half number of unbuilt cities<#endif>?

- <!-- priority=5 --> Can bot Move to get at least one new claim? <span style="font-size: 12px;">(18)</span> Prefer:
	- new resources
	- unclaimed
	- two slot planets

<#ifdef campaign>
✦ Does bot have unbuilt cities and cannot Build upgrades or armor at the Flagship planet?

- <!-- priority=5 --> Can bot Move Flagship to planet matching unbuilt upgrades or armor? <span style="font-size: 12px;">(19)</span>
<#endif>

✦ Can bot use an ability on a ready Guild or lore card?

✦ <!-- priority=8 --> Can bot Influence an uncontested card which would contend a declared ambition, if Secured? <span style="font-size: 12px;">(26)</span>

✦ <!-- priority=9 --> Can bot Influence a contested card? <span style="font-size: 12px;">(27)</span>

<#ifdef campaign>
✦ Would bot contend a declared ambition with the Imperial Trust?

- <!-- priority=9.5 --> Can bot Influence the Imperial Council? <span style="font-size: 12px;">(28)</span>
<#endif>

<#ifdef campaign>
✦ <!-- priority=10 --> Can bot Move to take control of rival city or Free city? <span style="font-size: 12px;">(31)</span>
<#endif>

<#ifdef base>
✦ <!-- priority=10 --> Can bot Move to take control of rival city? <span style="font-size: 12px;">(32)</span>
<#endif>

✦ Can bot Move to change control of a rival-controlled gate? <span style="font-size: 12px;">(44)</span> Prefer:

- take control adjacent to rival starport
- take or neutralize control adjacent to loyal starport

✦ Are there any ships not controlling gates or claims or rival buildings?

- Can bot Move to unassigned ships to task force (use partial move)? <span style="font-size: 12px;">(45)</span>

✦ Can bot Influence any other cards? <span style="font-size: 12px;">(47)</span>

<div class="pagebreak"> </div>
