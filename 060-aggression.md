# Aggression - Move | Battle | Secure

✦ <!-- priority=1 --> Can bot Secure to <ins>contend</ins> a declared ambition?

<#ifdef base>
✦ <!-- priority=2 --> Can bot Secure an <ins>effective</ins> Vox card?
<#endif>

<#ifdef campaign>
✦ <!-- priority=2 --> Can bot Secure an <ins>effective</ins> Vox card or the Imperial Council?
<#endif>

<#ifdef campaign>
✦ <!-- priority=2.5 --> Can bot Secure a Faithful card or an attached Guild card?
<#endif>

✦ <!-- priority=2 --> Can bot <ins>favorable combat</ins> to <ins>contend</ins> a declared ambition?

✦ Does bot have no starport and no <ins>claims</ins>?

- <!-- priority=3 --> Can bot Move to get new <ins>claims</ins>?

✦ Are any loyal buildings controlled by a rival?

- <!-- priority=4 --> Can bot Move or <ins>favorable combat</ins> to change control?

✦ Does bot have <ins>unbuilt cities</ins> and fewer <ins>claims</ins> than <#ifdef base><ins>unbuilt cities</ins><#endif><#ifdef campaign>half number of <ins>unbuilt cities</ins><#endif>?

- <!-- priority=5 --> Can bot Move to get at least one new <ins>claim</ins>? Prefer:
	- <ins>new resources</ins>
	- <ins>unclaimed</ins>
	- two slot planets

✦ <!-- priority=6 --> Can bot Secure to <ins>contend</ins> an <ins>undeclared ambition</ins> or to grow lead in declared ambition?

<#ifdef campaign>
✦ <!-- priority=10 --> Can bot Move to take control of rival city or Free city?
<#endif>

<#ifdef base>
✦ <!-- priority=10 --> Can bot Move to take control of rival city?
<#endif>

<#ifdef campaign>
✦ Can bot <ins>favorable combat</ins> to destroy Blight in systems with loyal buildings?
<#endif>

✦ Are there any ambition markers available?

- Can bot <ins>favorable combat</ins> to take trophies?

✦ Can bot Secure to grow lead in an <ins>undeclared ambition</ins> or to take any other cards?

✦ Can bot Move to change control of a rival-controlled gate? Prefer:

- take control adjacent to rival starport
- take or neutralize control adjacent to loyal starport

✦ Are there any ships not controlling gates or <ins>claims</ins> or rival buildings?

- Can bot Move to unassigned ships to <ins>task force</ins> (use <ins>partial move</ins>)?

<div class="pagebreak"> </div>
