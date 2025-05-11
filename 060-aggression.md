# Aggression - Move | Battle | Secure

✦ <!-- priority=1 --> Can bot Secure to contend a declared ambition? <span style="font-size: 12px;">(2)</span>

<#ifdef base>
✦ <!-- priority=2 --> Can bot Secure an effective Vox card? <span style="font-size: 12px;">(3)</span>
<#endif>

<#ifdef campaign>
✦ <!-- priority=2 --> Can bot Secure an effective Vox card or the Imperial Council? <span style="font-size: 12px;">(4,5)</span>
<#endif>

<#ifdef campaign>
✦ <!-- priority=2.1 --> Can bot Secure a Faithful card or an attached Guild card? <span style="font-size: 12px;">(6,7)</span>
<#endif>

✦ <!-- priority=2.2 --> Can bot favorable combat to contend a declared ambition? <span style="font-size: 12px;">(8)</span>

✦ Does bot have no starport and no claims?

- <!-- priority=3 --> Can bot Move to get new claims? <span style="font-size: 12px;">(10)</span>

✦ Are any loyal buildings controlled by a rival?

- <!-- priority=4 --> Can bot Move or favorable combat to change control? <span style="font-size: 12px;">(13,14)</span>

✦ Does bot have unbuilt cities and fewer claims than <#ifdef base>unbuilt cities<#endif><#ifdef campaign>half number of unbuilt cities<#endif>?

- <!-- priority=5 --> Can bot Move to get at least one new claim? <span style="font-size: 12px;">(16)</span> Prefer:
	- new resources
	- unclaimed
	- two slot planets

✦ <!-- priority=6 --> Can bot Secure to contend an undeclared ambition, to take captives, or to grow lead in declared ambition? <span style="font-size: 12px;">(17,18,21)</span>

<#ifdef campaign>
✦ <!-- priority=10 --> Can bot Move to take control of rival city or Free city? <span style="font-size: 12px;">(27)</span>
<#endif>

<#ifdef base>
✦ <!-- priority=10 --> Can bot Move to take control of rival city? <span style="font-size: 12px;">(28)</span>
<#endif>

<#ifdef campaign>
✦ Can bot favorable combat to destroy Blight in systems with loyal buildings? <span style="font-size: 12px;">(36)</span>
<#endif>

✦ Are there any ambition markers available?

- Can bot favorable combat to take trophies? <span style="font-size: 12px;">(37)</span>

✦ Can bot Secure to grow lead in an undeclared ambition or to take any other cards? <span style="font-size: 12px;">(38,39)</span>

✦ Can bot Move to change control of a rival-controlled gate? <span style="font-size: 12px;">(40)</span> Prefer:

- take control adjacent to rival starport
- take or neutralize control adjacent to loyal starport

✦ Are there any ships not controlling gates or claims or rival buildings?

- Can bot Move to unassigned ships to task force (use partial move)? <span style="font-size: 12px;">(41)</span>

<div class="pagebreak"> </div>
