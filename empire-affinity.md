# Empire Affinity

## Strong

bot always wants to stay a Regent or become a Regent

- if Regent and not First Regent:
	- check if exposed to "Govern the Imperial Reach"
		- does bot have piece for Demand or at least 1 agent in supply?
		- if not:
			- get a piece for Demand
			- get agent back (Secure)
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

## Neutral

randomly determine if bot will stay a Regent or become an Outlaw
TODO:
- track grievances vs the empire
- contend declared by stealing from the Trust

## Weak/Anti-Empire

bot always wants to become an Outlaw and rejects invitations to become a Regent

- if Regent:
	- play Event -> get Initiative -> call Summit
	- Influence & Secure Imperial Council -> call Summit
	- call Summit -> Leave the Empire
