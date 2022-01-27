# History, Purpose, and Intended Use
_Documentation Clark Nichols with Help from Dara Dadachanji_
## History
This project sprung out of a mutual desire for a tool that could assist in creation of well-tuned Magic:The Gathering decks. Both contributors (Dara and myself) began playing in a time before [scryfall.com](httsp://scryfall.com) existed. Both of us have wasted countless Wizard of the Coast's not-so-stellar [gatherer tool](https://gatherer.wizards.com). The user-interface for gatherer is clunky, unintuitive, and in-general a poor way of finding any useful cards.  

One example of gatherer's frustrating operation is its abysmal advanced search tool in which user error often requires inputting all previous information because an "and" should have been an "or." The function of the conditional statements is unclear, and to this day I cannot tell you if conditional statement order matters when using gatherer.  

*Take the following block of gatherer code, for example*
>OR Black  
AND Red  

It is actually very unclear what this search does. Do all of the listed cards have to be "**Red**" and does the "**OR** Black" statement mean that the only additional color is Black? Can this return cards without the color identity "Red" in them, such as [Pack Rat](https://scryfall.com/card/rtr/73/pack-rat)?
> <img src="https://c1.scryfall.com/file/scryfall-cards/large/front/1/7/170693f5-13db-4191-99b1-e527ffb5b88e.jpg?1562783180" width="200">
>
>~~_Delicious tea or deadly poison?_~~  
>_Result of: [**OR** Black],[**AND** Red] or result of: [**AND** Black],[**OR** Red]?_

Needless to say, scryfall's user interface and search conditions are a big improvement on Wizard's gatherer tool. But there could still be some ways to save time for players interested in making a serious deck that they intend to win with. I have dubbed this problem the Storm Crow Problem.

To translate the Storm Crow Problem into simple English without mathematical hieroglyphics is difficult, but I'll give it a shot. _(Warning, terrible satire ahead)_

Essentially, the problem is as follows: [Storm Crow](https://scryfall.com/card/9ed/100/storm-crow) is one of the greatest cards ever printed. However, players want to play with casual and fun cards such as [Brainstorm](https://scryfall.com/card/afc/79/brainstorm), [Ragavan, Nimble Pilferer](https://scryfall.com/card/mh2/138/ragavan-nimble-pilferer), [Swords to Plowshares](https://scryfall.com/card/voc/99/swords-to-plowshares), [Demonic Tutor](https://scryfall.com/card/uma/93/demonic-tutor), and [Primeval Titan](https://scryfall.com/card/ima/183/primeval-titan).

In other words: how can we remove [Storm Crow](https://scryfall.com/card/9ed/100/storm-crow) from results when searching for new cards to play with?

> <img src="https://c1.scryfall.com/file/scryfall-cards/large/front/a/5/a5bb2fa5-8f88-4d08-badb-3e52358d21d6.jpg?1561757760" width="200">
>
>_I dream of a day where storm crow is banned and my children can windmill-slam [Primeval Titan](https://scryfall.com/card/ima/183/primeval-titan) on turn ten like God intended._

This tool, then, is part of a long history of MTG Spikes trying to build decks and find interesting cards quickly and easily, and get rid of the "chaff."

##Technical Aspects of this Solution
It is due almost entirely to scryfall.com's amazing API documentation that we were able to create Python scripts that could interact with an unimagineable wealth of Magic:The Gathering knowledge. The largest part of the project, however, was figuring out what consituted "chaff" and what constituted "good."

Gosh I really want to make an ASP-less chaff joke.