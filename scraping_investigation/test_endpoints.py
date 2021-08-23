import requests


ENDPOINT = 'https://wizards.magic.com/en/section-articles-see-more-ajax?dateoff=&l=en&f=9041&search-result-theme=&limit=4&fromDate=&toDate=&sort=DESC&word=&offset=6'

def main():
    response = requests.get(ENDPOINT)
    print(response.text)


if __name__ == '__main__':
    main()