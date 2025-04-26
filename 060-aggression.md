# Aggression - Move | Battle | Secure

✦ <!-- priority=1 --> Can bot Secure to <ins>contend</ins> a declared ambition?

✦ <!-- priority=1.5 --> Can bot Secure an <ins>effective</ins> Vox card?

<#ifdef campaign>
✦ <!-- priority=2 --> Can bot Secure the Imperial Council, a Faithful card, or an attached Guild card?
<#endif>

✦ <!-- priority=2 --> Can bot <ins>favorable combat</ins> to <ins>contend</ins> a declared ambition?

✦ Does bot have no starport and no <ins>claims</ins>?

- <!-- priority=3 --> Can bot Move to get new <ins>claims</ins>?

✦ Are any loyal buildings controlled by a rival?

- <!-- priority=4 --> Can bot Move or <ins>favorable combat</ins> to change control?

✦ Does bot have <ins>unbuilt cities</ins> and fewer <ins>claims</ins> than <#ifdef base><ins>unbuilt cities</ins><#endif><#ifdef campaign>half number of <ins>unbuilt cities</ins><#endif>?

- <!-- priority=5 --> Can bot Move to get at least one new <ins>claim</ins>?
- Prefer:
	- <ins>new resources</ins>
	- <ins>unclaimed</ins>
	- two slot planets

✦ <!-- priority=6 --> Can bot Secure to <ins>contend</ins> an <ins>undeclared ambition</ins> or to grow lead in declared ambition?

✦ <!-- priority=10 --> Can bot Move or <ins>favorable combat</ins> to take control of rival city <#ifdef campaign>or Free city<#endif>?

✦ Can bot <ins>favorable combat</ins> for control in a system with any loyal buildings?

<#ifdef campaign>
✦ Can bot <ins>favorable combat</ins> to destroy Blight?
<#endif>

✦ Are there any ambition markers available?

- Can bot <ins>favorable combat</ins> to take trophies?

✦ Can bot take control of a gate adjacent to a loyal starport or rival starport?

✦ Are there ships not controlling gates or <ins>claims</ins> or rival buildings?

- Concentrate ships towards <ins>task force</ins> (use <ins>partial move</ins>)
- If <ins>task force</ins> not at loyal starport, move towards loyal starport (use <ins>partial move</ins>)

<div class="pagebreak"> </div>
