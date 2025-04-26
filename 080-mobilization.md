# Mobilization - Move | Influence

✦ Does bot have no starport and no <ins>claims</ins>?

- <!-- priority=3 --> Can bot Move to get new <ins>claims</ins>? <span style="font-size: 12px;">(9)</span>

✦ Are any loyal buildings controlled by a rival?

- <!-- priority=4 --> Can bot Move to change control? <span style="font-size: 12px;">(12)</span>

✦ Does bot have <ins>unbuilt cities</ins> and fewer <ins>claims</ins> than <#ifdef base><ins>unbuilt cities</ins><#endif><#ifdef campaign>half number of <ins>unbuilt cities</ins><#endif>?

- <!-- priority=5 --> Can bot Move to get at least one new <ins>claim</ins>? <span style="font-size: 12px;">(15)</span> Prefer:
	- <ins>new resources</ins>
	- <ins>unclaimed</ins>
	- two slot planets

✦ <!-- priority=8 --> Can bot Influence an <ins>uncontested card</ins> which would <ins>contend</ins> a declared ambition, if Secured? <span style="font-size: 12px;">(20)</span>

✦ <!-- priority=9 --> Can bot Influence a <ins>contested card</ins>? <span style="font-size: 12px;">(21)</span>

<#ifdef campaign>
✦ Would bot <ins>contend</ins> a declared ambition with the Imperial Trust?

- <!-- priority=9.5 --> Can bot Influence the Imperial Council? <span style="font-size: 12px;">(22)</span>
<#endif>

<#ifdef campaign>
✦ <!-- priority=10 --> Can bot Move to take control of rival city or Free city? <span style="font-size: 12px;">(26)</span>
<#endif>

<#ifdef base>
✦ <!-- priority=10 --> Can bot Move to take control of rival city? <span style="font-size: 12px;">(26)</span>
<#endif>

✦ Can bot Move to change control of a rival-controlled gate? <span style="font-size: 12px;">(36)</span> Prefer:

- take control adjacent to rival starport
- take or neutralize control adjacent to loyal starport

✦ Are there any ships not controlling gates or <ins>claims</ins> or rival buildings?

- Can bot Move to unassigned ships to <ins>task force</ins> (use <ins>partial move</ins>)? <span style="font-size: 12px;">(37)</span>

✦ Can bot Influence any other cards? <span style="font-size: 12px;">(39)</span>

<div class="pagebreak"> </div>
