# Mobilization - Move | Influence

✦ <!-- priority=4 --> Are any loyal buildings controlled by a rival?

- Can bot change control by moving?
	- Move to change control (Check "Movement Doctrine")
	- Prefer:
		- Take control if possible
		- Neutralize control

✦ <!-- Expand for city priority=5 --> Does bot have <ins>unbuilt cities</ins> and fewer <ins>claims</ins> than <#ifdef base><ins>unbuilt cities</ins><#endif><#ifdef campaign>half number of <ins>unbuilt cities</ins><#endif>?

- Could bot Move to control any open slots?
	- Move until bot has as many <ins>claims</ins> as <#ifdef base><ins>unbuilt cities</ins><#endif><#ifdef campaign>half number of <ins>unbuilt cities</ins><#endif>. Prefer:
		- <ins>new resources</ins>
		- <ins>unclaimed</ins>
		- two slot planets

✦ Can bot Influence a card?

- Prefer:
	- <!-- priority=8 --> <ins>uncontested card</ins> to <ins>contend</ins> declared ambition
	- <!-- priority=9 --> <ins>contested card</ins><#ifdef campaign>
	- <!-- priority=9.5 --> Imperial Council, if bot would <ins>contend</ins> a declared ambition with the Imperial Trust
<#endif>	- <ins>uncontested card</ins> to <ins>contend</ins> undeclared ambition
	- other cards (Check "Influence Doctrine" for priorities)

✦ Can bot change control of a gate?

- Prefer:
	- Take control if possible
	- Adjacent to loyal starport
	- Adjacent to rival starport

✦ <!-- priority=10 --> Can bot take control of rival building?

✦ Are there any ships which are not in the <ins>task force</ins>, and not controlling gates or <ins>claims</ins> or rival cities?

- Concentrate ships towards <ins>task force</ins> (use <ins>partial move</ins>)
- Move <ins>task force</ins> towards loyal starport if not already at a starport (use <ins>partial move</ins>)

<div class="pagebreak"> </div>
