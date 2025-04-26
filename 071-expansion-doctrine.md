# Expansion Doctrine

When getting new <ins>claims</ins> and building new cities the bot will follow these guidelines. Note that the bot will still use the guidance in the "Movement Doctrine" to move ships. This page aims to clarify **when** the bot will expand by staking new <ins>claims</ins> and building new cities, not explain **how** the bot will move. Use "Movement Doctrine" to determine how the moves are carried out.

## Staking New Claims

A <ins>claim</ins> is an open building slot on a planet where the bot has one or more pieces, i.e. it is a building slot where the bot could legally build a city or starport. Count each slot separately: if the bot has a ship at a planet with two open slots, count the bot as having two <ins>claims</ins>. *(Note that in previous versions of SUPERCAT, a <ins>claim</ins> was an open building slot **controlled** by the bot. This has since been relaxed to deprioritize expansion. If a bot has a ship or other building enabling it to build in an open slot, that counts as a <ins>claim</ins>, regardless of control of the system)* 

The procedures evaluate the number of <ins>claims</ins> the bot has in relation to the number of <ins>unbuilt cities</ins> (cities on the bot's board which it could build, not any cities held by rivals as trophies). The bot will seek to gain new <ins>claims</ins> if it has fewer <ins>claims</ins> than <#ifdef base><ins>unbuilt cities</ins><#endif><#ifdef campaign>half the number of <ins>unbuilt cities</ins>, rounded down<#endif>.
*(Note that this differs between the campaign game and the base game: in the campaign game the bot is satisfied with fewer <ins>claims</ins> than in the base game)*

## Limit on Building New Cities

The procedures prioritize building new cities somewhat highly relative to other actions. However there is a limit to this which is building a second city on the same planet where the bot already has a city. The bot will only build one of these <ins>double cities</ins> if it is winning a declared ambition (not tied for first place) and placing the city would uncover a power bonus.

*Note that a <ins>claim</ins> counts for the purpose of the expansion priorities described above even if the bot would not build a city there due to this limit. For instance, if a bot has 4 <ins>unbuilt cities</ins>, and has a ship at a plant with 2 slots, it is considered to have 2 <ins>claims</ins> even though when it comes time to build a city, the bot would only build 1 city there.*

<div class="pagebreak"> </div>
