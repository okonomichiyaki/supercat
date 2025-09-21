# Construction - Build | Repair

✦ Does bot have no starport?

- Can bot Build a starport? <span style="font-size: 12px;">[4]</span> Prefer system with<#ifdef campaign> (ignore if Flagship)<#endif>:
	- bot control
	- most Loyal ships
	- neutral control
	- least Rival ships

✦ Are any Loyal buildings controlled by a Rival?

- Can bot Build or Repair to change control? <span style="font-size: 12px;">[7,8]</span>

<#ifdef campaign>
✦ Is it the last Chapter of Act I or Act II?

- Can bot Repair any buildings or ships? <span style="font-size: 12px;">[12]</span> Prefer:
	- cities
	- only starport on map
	- ships
	- other starports
<#endif>

<#ifdef campaign>
✦ Can bot Build cities? <span style="font-size: 12px;">[15]</span> Prefer:

- (ignore if Flagship) only Build double city if winning a declared ambition and uncovering power bonus
- (Flagship only) do not build more cities than starports on Flagship board
<#endif>

<#ifdef base>
✦ Can bot Build cities? <span style="font-size: 12px;">[16]</span> Prefer:

- system with control
- only Build double city if winning a declared ambition and uncovering power bonus
<#endif>

✦ Can bot use an ability on a ready Guild or lore card?

✦ Does bot have more unbuilt ships than any Rival?

- Can bot Build ships? <span style="font-size: 12px;">[20]</span>

✦ Can bot Build or Repair to take control of a Rival building? <span style="font-size: 12px;">[23,24]</span>

✦ Can bot Build to defend an undefended building? <span style="font-size: 12px;">[29]</span>

✦ Can bot Build any ships? <span style="font-size: 12px;">[30]</span> Prefer:

- ships in task force
- fresh ships

✦ Can bot Build any other starports? <span style="font-size: 12px;">[31]</span> Prefer system with<#ifdef campaign> (ignore if Flagship)<#endif>:

- task force
- bot control

✦ Can bot Repair any ships or buildings? <span style="font-size: 12px;">[36]</span> Prefer:

- ships in task force
- other ships
- starport, if only one on map
- cities

<div class="pagebreak"> </div>
