# Construction - Build | Repair

<#ifdef base>
✦ Does bot have no starport?

- Can bot Build a starport? <span style="font-size: 12px;">[5]</span> Prefer system with:
	- bot control
	- most Loyal ships
	- neutral control
	- least Rival ships
<#endif>

<#ifdef campaign>
✦ Does bot have no starport?

- Can bot Build a starport? <span style="font-size: 12px;">[6]</span> Prefer system with (ignore if Flagship):
	- bot control
	- most Loyal ships
	- neutral control
	- least Rival ships
<#endif>

✦ Are any Loyal buildings controlled by a Rival?

- Can bot Build or Repair to change control? <span style="font-size: 12px;">[9,10]</span>

<#ifdef campaign>
✦ Is it the last Chapter of Act I or Act II?

- Can bot Repair any buildings or ships? <span style="font-size: 12px;">[14]</span> Prefer:
	- starport (if bot has only one on map)
	- cities
	- ships
	- other starports
<#endif>

<#ifdef campaign>
✦ Can bot Build cities? <span style="font-size: 12px;">[17]</span> Prefer:

- (ignore if Flagship) only Build double city if winning a declared ambition and uncovering power bonus
- (Flagship only) do not build more cities than starports on Flagship board
<#endif>

<#ifdef base>
✦ Can bot Build cities? <span style="font-size: 12px;">[18]</span> Prefer:

- system with control
- only Build double city if winning a declared ambition and uncovering power bonus
<#endif>

✦ Can bot use an ability on a ready Guild or lore card?

✦ Does bot have more unbuilt ships than any Rival?

- Can bot Build ships? <span style="font-size: 12px;">[23]</span>

✦ Can bot Build or Repair to take control of a Rival building? <span style="font-size: 12px;">[26,27]</span>

✦ Can bot Build to defend an undefended building? <span style="font-size: 12px;">[32]</span>

✦ Can bot Build any ships? <span style="font-size: 12px;">[33]</span> Prefer:

- ships in task force
- fresh ships

<#ifdef base>
✦ Can bot Build any other starports? <span style="font-size: 12px;">[34]</span> Prefer system with:

- task force
- bot control
<#endif>

<#ifdef campaign>
✦ Can bot Build any other starports? <span style="font-size: 12px;">[35]</span> Prefer system with (ignore if Flagship):

- task force
- bot control
<#endif>

✦ Can bot Repair any ships or buildings? <span style="font-size: 12px;">[40]</span> Prefer:

- ships in task force
- other ships
- starport, if only one on map
- cities

<div class="pagebreak"> </div>
