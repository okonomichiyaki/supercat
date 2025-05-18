# Construction - Build | Repair

✦ Does bot have no starport?

- <!-- priority=3 --> Can bot Build a starport? <span style="font-size: 12px;">(9)</span> Prefer system with<#ifdef campaign>(ignore if Flagship)<#endif>:
	- bot control
	- most loyal ships
	- neutral control
	- least rival ships

✦ Are any loyal buildings controlled by a rival?

- <!-- priority=4 --> Can bot Build or Repair to change control? <span style="font-size: 12px;">(12,13)</span>

<#ifdef campaign>
✦ <!-- priority=5 --> Can bot Build cities? <span style="font-size: 12px;">(16)</span> Prefer:

- (ignore if Flagship) only Build double city if winning a declared ambition and uncovering power bonus
- (Flagship only) do not build more cities than starports on Flagship board
<#endif>

<#ifdef base>
✦ <!-- priority=5 --> Can bot Build cities? <span style="font-size: 12px;">(17)</span> Prefer:

- only Build double city if winning a declared ambition and uncovering power bonus
<#endif>

✦ Can bot use an ability on a ready Guild or lore card?

✦ <!-- priority=10 --> Can bot Build or Repair to take control of a rival building? <span style="font-size: 12px;">(29,30)</span>

✦ <!-- priority=10.5 --> Can bot Build to defend an undefended building? <span style="font-size: 12px;">(35)</span>

✦ <!-- priority=11 --> Can bot Build any ships? <span style="font-size: 12px;">(36)</span> Prefer:

- ships in task force
- fresh ships

✦ <!-- priority=11 --> Can bot Build any other starports? <span style="font-size: 12px;">(37)</span> Prefer system with<#ifdef campaign> (ignore if Flagship)<#endif>:

- task force
- bot control

✦ <!-- priority=12 --> Can bot Repair any other ships or buildings? <span style="font-size: 12px;">(38)</span> Prefer:

- ships in task force
- other ships
- starport, if only one on map
- cities

<div class="pagebreak"> </div>
