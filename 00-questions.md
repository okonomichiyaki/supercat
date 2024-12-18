# Questions

Every question should have a yes or no answer. There are four types of questions. Use the following guide if you are confused how to follow the procedures.

**Type 1**: This type of question will be a single line like this:

*Can bot take some action to achieve some goal?*

If the bot is able to take the action, following all the rules of the game, to achieve the stated goal, then take the action. If the answer is "no", continue reading to the next section.

**Type 2**: This type of question will have one nested subsection that is not marked.

*Question about the game state?*

- *Action to take, or other question to evaluate, if answer to first question was "yes"*

If the answer is "yes", follow the nested procedures. If the answer is "no", then continue reading to the next section.

**Type 3**: This type of question will have two nested subsections, one marked "yes" and the other marked "no".

*Question about the game state?*

- *Yes:*
	- *Action to take, or other question to evaluate, if answer to first question was "yes"*
- *No:*
	- *Action to take, or other question to evaluate, if answer to first question was "no"*

If the answer is "yes", continue with subsection marked "yes", otherwise continue with the subsection marked "no".

**Type 4**: This type of question is only used on the General Priorities page.

*Can bot take some action? → Card suit*

In this case, if the answer is "yes" AND the bot has a card of the indicated suit available (either one of 2 cards draw, or the lead card to copy), then select that card. Proceed to the page for the selected suit.

<div class="pagebreak"> </div>