
i'll be using the setup card "3 Players - Mix Up", and will use "normal difficulty", so the solo player will be last and the bots ahead in turn order: red bot will be player 1, yellow bot will be player 2, and blue (solo player) will be player 3. here is the initial board state:

[example 01]

the initial court is: Mass Uprising, Shipping Interest, Admin Union, and Sworn Guardians

[example 02]

i shuffle and deal 6 cards to the blue player, and place a counter on each bot board, showing 6 to represent the number of cards left in each bot's hand. the rest of the action cards form a facedown draw deck for the bots. it's red bot's turn, so starting with the page titled "Bot turn (START HERE)", and read the procedures from top to bottom:

[q][i]✦ If bot has no cards left *(check hand counter)* then bot will pass.[/i][/q]

red bot has cards left, so keep reading:

[q][i]
✦ Is bot's hand counter greater than number of bonus cards in the bot's play area?
- Draw 2 cards.

✦ Decrement hand counter.
[/q][/i]

red bot has zero bonus cards (cards gained from the "Call to Action" Vox card or the "Union" Guild cards) and the hand counter is on 6, so this condition is true. we follow the nested procedure and draw 2 cards. the next procedure tells us to decrement the hand counter

These are the 2 cards drawn:

[example 03]

(note that the hand counter is on 5 now)

Continuing reading down the page, and arrive at this question:

[q][i]
✦ Does bot have initiative?
- Remove seize counter, if present.
[/q][/i]

Red bot has initiative, so follow the nested procedures again, in this case resetting the seize counter. This will be explained later in the example, but for now skip over as the seize counter is not present, and keep reading:

[q][i]- Is bot winning or tied for first place for a matching ambition?[/i][/q]

red bot is not winning or tied for first place in either ambition on the two cards draw, so the answer is "no". skip the nested procedures and read the next step at the same level:

[q][i]
- Use General Priorities to select card.
[/q][/i]

This instructs us to turn the page and consult the "General Priorities" to select the card. Reading this page from top to bottom, we can skip over the following procedures, because the answers are "no" for each of them:

[q][i]
✦ Can bot Secure or Tax to contend declared ambition? → Administration/Aggression
✦ Can bot Secure an effective Vox card? → Aggression
✦ Can bot favorable combat to contend declared ambition? → Combat card
✦ Does bot have no starport?
✦ Are any loyal buildings in a system controlled by a rival?
[/q][/i]

i'll get into what "contend" and "favorable combat" mean in the next example, but the answer to these are obviously "no" because there are no declared ambitions yet. the bot starts with a starport so skip that question as well, and get to:

[q][i]✦ Does bot have unbuilt cities?[/i][/q]

the bot has cities on its player board, so the answer is "yes" and we look at the nested procedures under this question.

[q][i]• Does bot have fewer claims than unbuilt cities?[/i][/q]

The word "claim" is a special keyword for SUPERCAT and refers to an open building slot where the bot could build a building.

*(Note that in previous versions of SUPERCAT, a claim was an open building slot **controlled** by the bot. This has since been relaxed to deprioritize expansion. If a bot has a ship or other building enabling it to build in an open slot, that counts as a claim, regardless of control of the system)* 

The bot starts with ships and a building at a planet with one open slot (the starting Weapon planet) and has 4 unbuilt cities. So with 1 claim and 4 unbuilt cities, the answer is "yes". that branch has a new question:

[q][i]
- Yes: Can bot move to get a new claim? → Mobilization/Aggression
[/i][/q]

the answer to this is also yes, for two reasons: first, the bot has Move available as an action among the cards draw (recall the suits were TODO) and second, there are a series of Move actions the bot could take which would result in at least one new claim (there are more than one option, but for now it's enough to determine that it is at least possible to get a new claim, the details are worked out later)

This directs us to pick either Mobilization or Aggression, if one of them is an option. The bot drew Aggression and Construction, so it will play Aggression, and discard the Construction.

Next, we turn to the page for the Prelude. the bot has a Weapon and a Relic, and the Prelude rules for the bot tells us that

[q][i]
**Fuel and Weapon**: spend for Combat card
**Relic**: Secure for captives, contend a declared ambition, or effective Vox card.
[/i][/q]

Nothing so far as pointed us in the direction of conducting a Combat, and the bot can't Secure anything as there's no agents in the Court. so we move on and turn to the page for Aggression. Reading from top to bottom, we can evaluate the following are all false, because the bot can't Secure anything, and nothing has been declared yet:

[q][i]
✦ Can bot Secure to contend a declared ambition?
✦ Can bot Secure an effective Vox card?
✦ Can bot favorable combat to contend a declared ambition?
✦ Does bot have no starport and no claims?
✦ Are any loyal buildings controlled by a rival?
[/i][/q]

The next question is true, along with its nested question, and matches what lead to the selection of Aggression:

[q][i]
✦ Does bot have unbuilt cities and fewer claims than unbuilt cities?
- Can bot Move to get at least one new claim?
[/i][/q]

The nested instruction lists the bot's preferences:

[q][i]
- Prefer:
	- new resources
	- unclaimed
	- two slot planets
[/i][/q]

The bot has 3 actions available (it's leading so it gets 2 actions from 2 pips on the card, and it gets a bonus action from the difficulty modifier "Efficient Logistics")

There are several planets which meet the first criteria. Narrowing them down using the second and third criteria leads to only one planet: the Fuel in the upper left (6-Moon)

The bot has two different ways to get ships to this planet:

- Move from Gate 2 to Gate 6
- Then from Gate 6 to destination Fuel planet

or 

- Move 2 ships from Relic planet 5-Moon (starting starport) to Psionic planet 5-Hex
- Then to Material planet 6-Arrow
- Finally to Fuel planet destination

When the bot has multiple options, the non-player system provides several tools to pick for the bot. See "Decision making for the bot" for more details, but we start with any "Preferences" marked with "Prefer". We have already done that and it won't help resolve this decision. The next step is to refer to the bot's "Priniciples". These are a collection of guidelines for specific actions, and includes a page about movement.

*(Note that in previous versions of SUPERCAT, these were called "Doctrines" but i changed the name to avoid any overloading with the campaign, which uses that word in the Believer's Act II mechanics)*

Referring to that page, we find the following:

[q][i]
Select origin and destination which takes the shortest path (i.e. spend fewest action).
[/i][/q]

The first choice is shorter than the second, so the bot will execute that move which takes 2 actions, leaving 1 action remaining for the turn. Generally, the bot will spend as many actions as necessary to achieve whatever goal the procedures prioritize. Any remaining actions will use the same list of priorities, and strictly speaking the player should start over at the top of the page for the suit and check each priority again. In practice, this is only rarely necessary, because there are only a few situations where actions will change the board state to open up possible higher priority actions which were skipped earlier. This situation is typical: red bot has one remaining action, and none of the procedures we skipped apply, so we end up re-evaluating the current procedure ([i]Does bot have unbuilt cities and fewer claims than unbuilt cities?[/q]) which results in the bot seeking another claim. After checking the preferences again, there are two equal options: Psionic planet 6-Hex and Material planet 6-Arrow. None of the principles help resolve these options, so we pick randomly, and the result is the Psionic planet. The bot moves one ship to the destination, in order to comply with the Movement principles ("When possible, retain control of the origin system").

Finally, red bot passes the turn to yellow bot. Here's the board state after red bot's first turn:

[example 04]

Yellow bot starts its turn with the same process, reading from the "Bot turn (START HERE)" page, checking hand size and bonus cards, then drawing 2 cards and decrementing the hand counter:

[example 05]

This time, since Yellow does not have initiative, but has drawn a 6 of Aggression, we follow a slightly different path:

[q][i]✦ Does bot have initiative?[/i][/q]

the answer is "no" but the answer to the next question is "yes"

[q][i]
✦ Can bot surpass with any card?
- Yes:
	- Select card which surpasses. Prefer: higher number
[/i][/q]

Yellow bot selects the 6 of Aggression. Before turning to that page, we check the Prelude. Yellow bot has two Psionic resources, and the Prelude page instructs us:

[q][i]
**Psionic**: Tax/Secure to contend a declared ambition, or spend for Combat card
[/i][/q]

Nothing has been declared yet and we're not in a combat situation. Turning to the page for Aggression, yellow bot executes a similar turn to red bot: Yellow gets 3 actions as well, and Moves to get control of new planets, following the preferences listed with the procedure and Movement Principles.

- Move 2 ships from Psionic planet 5-Hex to Material planet 6-Arrow
- Move 1 ship from Gate 3 to Fuel planet 3-Crescent
- Move 2 ship from Psionic planet 2-Arrow to Weapon planet 2-Crescent

(The preferences result in yellow bot picking unclaimed planets and the Movement Principles dictate how many ships move and are left behind)

Blue solo player pivots to Construction and builds one ship at the starting starport (Material planet 3-Arrow). Since yellow bot had the highest card of the lead suit, it gains initiative.

here's the board state after the first round:

[example 06]

