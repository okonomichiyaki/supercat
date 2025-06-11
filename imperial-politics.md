## Imperial Politics

Depending on which Fate the bot is playing it will behave differently with regard to Regent and Outlaw status. When playing some Fates, the bot will prioritize leaving the Empire to become an Outlaw and in other cases the bot will prioritize staying a Regent. This is called "Empire Affinity" and has three possible values: Strong, Neutral, and Weak/Anti-Empire. Fates will indicate their Empire Affinity; by default if this is absent the bot will adopt the Neutral stance. When indicated, check the procedures below and follow them during the bot's turn.

### Strong

A bot playing a Fate with Strong Empire Affinity always wants to stay a Regent or become a Regent (if it is an Outlaw).

Leave the Empire
: Never

Revive the Empire
: Always

- if Regent and not First Regent:
	- check if exposed to "Govern the Imperial Reach" or "Govern with Authority":
		- does bot have piece for Demand OR at least 1 agent in supply?
		- if not:
			- get a piece for Demand (Prefer: Tax, Secure, then favorable combat)
			- or get agent back (Secure any card to return agents in the Court to supply)
- if Outlaw:
	- either:
		- get a Favor from First Regent
		- call Summit
		- return Favor to force invite to Empire
	- or:
		- call Summit
		- negotiate with First Regent to invite
		- bot-bot negotiation is covered
		- if player is the First Regent:
			- TODO: need a special case for bot-human negotiation here

### Neutral

A bot playing a Fate with Neutral Empire Affinity will randomly determine if it will stay a Regent, become an Outlaw, or accept invitations to become a Regent.

TODO:
- track grievances vs the empire
- contend declared by stealing from the Trust

Leave the Empire
: TODO

Revive the Empire
: TODO

### Weak/Anti-Empire

A bot playing a Fate with Weak Empire Affinity always wants to become an Outlaw and will always reject invitations to become a Regent.

Leave the Empire
: Always

Revive the Empire
: Never

- if Regent:
	- play Event -> get Initiative -> call Summit
	- Influence & Secure Imperial Council -> call Summit
	- call Summit -> Leave the Empire

