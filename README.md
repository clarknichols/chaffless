# decklist_aggregator
scrapes recent MTGO tournament results from WotC's website

I'm not sure if it's worth setting up selenium to scrape more than 6 events at a time. Easier to manually click 'expand' a bunch of times and just save down the html file then parse it.

Then I'll have this running once a day with just the requests package.

note, you can edit the "data-see-more-limit" attribute in //*[@id="mtgo-decklists"]/div[3] to whatever you want to make expanding faster
