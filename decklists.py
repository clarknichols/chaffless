import requests
import lxml.html
import json

def main():
    with open('data/events.json', 'r', encoding='UTF-8') as file:
        events = json.load(file)
    event = events[0]
    decklists = fetch_decklists(event)
    with open('data/decklists.json', 'w', encoding='UTF-8') as file:
        json.dump(decklists, file, indent=2)

def fetch_decklists(event_url: str):
    event = after_last_slash(event_url)
    response = requests.get(event_url)
    article: lxml.html.HtmlElement = lxml.html.fromstring(response.text)
    decks = article.xpath(
        '//div[@class="deck-list-text"]'
    )
    print(len(decks))
    decklists = [extract_decklist(deck) for deck in decks]
    for decklist in decklists:
        decklist['event'] = event
    return decklists


def after_last_slash(url: str):
    return url[url.rfind('/')+1:]


def extract_decklist(deck: lxml.html.HtmlElement):
    maindeck = extract_maindeck(deck)
    sideboard = extract_sideboard(deck)
    return {
        'maindeck': maindeck,
        'sideboard': sideboard
    }


def extract_maindeck(deck: lxml.html.HtmlElement):
    rows = deck.xpath(
        'div[@class="sorted-by-overview-container sortedContainer"]'
        '/div'
        '/span[@class="row"]'
        )
    print(len(rows))
    return [get_card(row) for row in rows]


def extract_sideboard(deck: lxml.html.HtmlElement):
    rows = deck.xpath(
        'div[@class="sorted-by-sideboard-container  clearfix element"]'
        '/span[@class="row"]'
        )
    return [get_card(row) for row in rows]


def get_card(row: lxml.html.HtmlElement):
    count = row.xpath('span[@class="card-count"]/text()')
    name = row.xpath('span[@class="card-name"]/a/text()')
    if not name: 
        #sometimes there is no metadata included with the card
        #and  the name is in the card-name <span> instead of a child <a>
        name = row.xpath('span[@class="card-name"]/text()')
    return {
        'name': name[0],
        'count': count[0]
    }


if __name__ == '__main__':
    main()

