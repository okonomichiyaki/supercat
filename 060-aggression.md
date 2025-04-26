# Aggression - Move | Battle | Secure

✦ <!-- priority=1 --> Can bot Secure to <ins>contend</ins> a declared ambition? <span style="font-size: 12px;">(2)</span>

<#ifdef base>
✦ <!-- priority=2 --> Can bot Secure an <ins>effective</ins> Vox card? <span style="font-size: 12px;">(3)</span>
<#endif>

<#ifdef campaign>
✦ <!-- priority=2 --> Can bot Secure an <ins>effective</ins> Vox card or the Imperial Council? <span style="font-size: 12px;">(3,4)</span>
<#endif>

<#ifdef campaign>
✦ <!-- priority=2.1 --> Can bot Secure a Faithful card or an attached Guild card? <span style="font-size: 12px;">(5,6)</span>
<#endif>

✦ <!-- priority=2.2 --> Can bot <ins>favorable combat</ins> to <ins>contend</ins> a declared ambition? <span style="font-size: 12px;">(7)</span>

✦ Does bot have no starport and no <ins>claims</ins>?

- <!-- priority=3 --> Can bot Move to get new <ins>claims</ins>? <span style="font-size: 12px;">(9)</span>

✦ Are any loyal buildings controlled by a rival?

- <!-- priority=4 --> Can bot Move or <ins>favorable combat</ins> to change control? <span style="font-size: 12px;">(12,13)</span>

✦ Does bot have <ins>unbuilt cities</ins> and fewer <ins>claims</ins> than <#ifdef base><ins>unbuilt cities</ins><#endif><#ifdef campaign>half number of <ins>unbuilt cities</ins><#endif>?

- <!-- priority=5 --> Can bot Move to get at least one new <ins>claim</ins>? <span style="font-size: 12px;">(15)</span> Prefer:
	- <ins>new resources</ins>
	- <ins>unclaimed</ins>
	- two slot planets

✦ <!-- priority=6 --> Can bot Secure to <ins>contend</ins> an <ins>undeclared ambition</ins> or to grow lead in declared ambition? <span style="font-size: 12px;">(16,19)</span>

<#ifdef campaign>
✦ <!-- priority=10 --> Can bot Move to take control of rival city or Free city? <span style="font-size: 12px;">(26)</span>
<#endif>

<#ifdef base>
✦ <!-- priority=10 --> Can bot Move to take control of rival city? <span style="font-size: 12px;">(26)</span>
<#endif>

<#ifdef campaign>
✦ Can bot <ins>favorable combat</ins> to destroy Blight in systems with loyal buildings? <span style="font-size: 12px;">(32)</span>
<#endif>

✦ Are there any ambition markers available?

- Can bot <ins>favorable combat</ins> to take trophies? <span style="font-size: 12px;">(33)</span>

✦ Can bot Secure to grow lead in an <ins>undeclared ambition</ins> or to take any other cards? <span style="font-size: 12px;">(34,35)</span>

✦ Can bot Move to change control of a rival-controlled gate? <span style="font-size: 12px;">(36)</span> Prefer:

- take control adjacent to rival starport
- take or neutralize control adjacent to loyal starport

✦ Are there any ships not controlling gates or <ins>claims</ins> or rival buildings?

- Can bot Move to unassigned ships to <ins>task force</ins> (use <ins>partial move</ins>)? <span style="font-size: 12px;">(37)</span>

<div class="pagebreak"> </div>
