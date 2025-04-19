# General Priorities
<#ifdef campaign>
✦ Check bot's Fate for initial priorities. If no card selected, return to this page.
<#endif>
✦ <!-- priority=1 --> Can bot Tax/Secure to <ins>contend</ins> declared ambition? → Administration/Aggression

✦ <!-- priority=1.5 --> Can bot Secure an <ins>effective</ins> Vox card<#ifdef campaign>, the Imperial Council, or Secure a card with an attached Faithful or Guild card<#endif>? → Aggression

✦ <!-- priority=2 --> Can bot <ins>favorable combat</ins> to <ins>contend</ins> declared ambition? → <ins>Combat card</ins>

✦ Does bot have no starport?

- Does bot have a <ins>claim</ins>?
	- <!-- Build starport priority=3 --> Yes: → Construction
	- <!-- Expand for starport priority=3 --> No: → Mobilization/Aggression

✦ Are any loyal buildings in a system controlled by a rival?

- <!-- priority=4 --> Can bot Move or <ins>favorable combat</ins> to change control? → Mobilization/Aggression
- <!-- priority=4 --> Can bot Build or Repair to change control? → Construction/Administration

✦ Does bot have <ins>unbuilt cities</ins>?

- Does bot have fewer <ins>claims</ins> than <#ifdef base><ins>unbuilt cities</ins><#endif><#ifdef campaign>half number of <ins>unbuilt cities</ins>, rounded down<#endif>?
	- Yes: <!-- Expand for city priority=5 --> Can bot move to get a new <ins>claim</ins>? → Mobilization/Aggression
	- No: <!-- Build city priority=5 --> Does bot have at least one <ins>claim</ins>? → Construction

✦ <!-- priority=6 --><!-- priority=7 --> Can bot Tax/Secure to <ins>contend</ins> <ins>undeclared ambition</ins>, take captives, or grow a lead in a declared ambition? <br>→ Administration/Aggression

✦ <!-- priority=8 --><!-- priority=9 --> Can bot Influence a card with more agents than rivals? → Mobilization/Administration
<#ifdef campaign>
✦ <!-- priority=9.5 --> Would bot <ins>contend</ins> a declared ambition with the Imperial Trust, and can bot Influence the Imperial Council with more agents than rivals? → Mobilization/Administration
<#endif>
✦ <!-- priority=10 --> Can bot Move to take control of rival building → Mobilization/Aggression

✦ <!-- priority=11 --><!-- priority=12 --> Can bot Build or Repair ships? → Construction/Administration

<div class="pagebreak"> </div>
