<#ifdef campaign>
# Steward

## All Acts

✦ Can bot use Dealmakers' **Bargain (Secure)** ability?

- Use **Bargain (Secure)**. Use these priorities to select a card for rival to Secure and subsequent Influence and Secure actions:
	- Imperial Council and Council Intrigue *(Select target which allows bot to Influence and Secure either of these cards, or prevent rival from Securing)*
	- Protect loyal agents
	- Check "Influence Principles" for additional priorities

✦ Is the Imperial Council "In Session"?

- Yes: Can bot Secure or Influence the Imperial Council? (check "Influence Principles")
- No: Is bot no longer the First Regent?
	- Can bot Influence or Secure Council Intrigue?

Events
: If bot is not First Regent and Imperial Council is "Decided" or there are no Regents

Petition the Council
: If bot is not the First Regent and the Imperial Council is "Decided"

Leave the Empire
: Never

Revive the Empire
: Always

<div class="pagebreak"> </div>

## Act II

✦ Are there any clusters where the Empire does not control any systems?

- Can bot Move to get Empire control in a system in one of these clusters?

✦ Does a rival have more cities than bot?

- Can bot Build a city?
- If bot would have most cities by building a double city, ignore usual restriction on double cities. *(build even if not winning a declared ambition and not uncovering bonus power)*

✦ Does a rival have more starports than bot?

- Can bot Build a starport to have the most starports built (including ties)?

Govern the Imperial Reach
: Prefer Policy of Peace or Policy of Escalation

Imperial Quorum
: When the Regent with the most starports is a bot, it will always take the Imperial action, except if the policy is Policy of Peace and the bot would gain less power than any other rival. When the Regent with the most cities is a bot, check the Fate to see if it will change the policy.

<!-- 
## Act III

TODO: Grand Ambitions

✦ Can bot Build, Repair, or Move to take control of an Outlaw city?

✦ Can bot favorable battle to take control of an Outlaw city?

TODO:
If bot is not the First Regent -> actions to become First Regent
If bot IS the First Regent -> actions to stay First Regent


Imperial Sponsor
: If the Steward is the First Regent, select an undeclared ambition which an Outlaw is winning or contending.
-->
<div class="pagebreak"> </div>
<#endif>