# Aggression - Move | Battle | Secure

✦ <!-- priority=1 --> Can bot Secure a card to <ins>contend</ins> a declared ambition?

✦ <!-- priority=1.5 --> Can bot Secure an <ins>effective</ins> Vox card<#ifdef campaign>, Imperial Council, or an attached Faithful or Guild card<#endif>?

✦ <!-- priority=2 --> Can bot <ins>favorable combat</ins> to <ins>contend</ins> a declared ambition? (Check "Combat Doctrine")

✦ <!-- Expand for starport priority=3 -->If bot have no starport and no <ins>claims</ins>, can bot Move to get at least one new <ins>claim</ins>?

✦ Are any systems with a loyal building controlled by a rival?

- <!-- priority=4 --> Can bot Move or <ins>favorable combat</ins> to change control?

✦ Does bot have <ins>unbuilt cities</ins> and fewer <ins>claims</ins> than <#ifdef base><ins>unbuilt cities</ins><#endif><#ifdef campaign>half number of <ins>unbuilt cities</ins><#endif>?

- Can bot Move to get at least one new <ins>claim</ins>?
	- <!-- Expand for city priority=5 --> Move to get new <ins>claims</ins>, until bot has as many <ins>claims</ins> as <#ifdef base><ins>unbuilt cities</ins><#endif><#ifdef campaign>half number of <ins>unbuilt cities</ins>, rounded down<#endif>. Prefer:
		- <ins>new resources</ins>
		- <ins>unclaimed</ins>
		- two slot planets

✦ <!-- priority=6 --> Can bot Secure card to <ins>contend</ins> an <ins>undeclared ambition</ins>?

✦ <!-- priority=7 --> Can bot Secure a card to grow a lead in a declared ambition?

<#ifdef campaign>
✦ <!-- priority=9.5 --> Can bot Secure the Imperial Council?
	- Would bot <ins>contend</ins> a declared ambition with the Imperial Trust?
<#endif>

✦ <!-- priority=10 --> Can bot take control of rival building?

✦ Can bot <ins>favorable combat</ins> for control in a system with any loyal buildings?

- Check Combat Doctrine

✦ Are there any <ins>undeclared ambition</ins>s and can bot <ins>favorable combat</ins> for trophies?

- Check Combat Doctrine

✦ Can bot Secure a card to grow a lead in an <ins>undeclared ambition</ins> or Secure another card?

✦ Can bot take control of a gate adjacent to a loyal starport or rival starport?

✦ Are there ships not controlling gates or <ins>claims</ins> or rival buildings?

- Concentrate ships towards <ins>task force</ins> (use <ins>partial move</ins>)
- If <ins>task force</ins> not at loyal starport, move towards loyal starport (use <ins>partial move</ins>)

<div class="pagebreak"> </div>
