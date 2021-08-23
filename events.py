import requests
import lxml.html
import json


def main():
    events = fetch_events()
    with open('data/events.json', 'w') as file:
        json.dump(obj=events, fp=file, indent=4)


def fetch_events ():
    with open('data/links.html', mode='r', encoding='UTF-8') as file:
        text = file.read()

    page: lxml.html.HtmlElement = lxml.html.fromstring(text)
    events = page.xpath(
        '//div[@id="mtgo-decklists"]'
        '/div[@class="articles-listing"]'
        '/div'
        '/a'
        '/@href'
    )
    return events


if __name__ == '__main__':
    main()
    