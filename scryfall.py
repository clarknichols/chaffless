"""calls scryfall API for initial card list"""

import requests
import pandas as pd

ENCODINGS = {
    "!": "%21",
    "#": "%23",
    "$": "%24",
    "%": "%25",
    "&": "%26",
    "'": "%27",
    "(": "%28",
    ")": "%29",
    "*": "%2A",
    "+": "%2B",
    ",": "%2C",
    "/": "%2F",
    ":": "%3A",
    ";": "%3B",
    "=": "%3D",
    "?": "%3F",
    "@": "%40",
    "[": "%5B",
    "]": "%5D",
}

def search(query: str):
    domain = "https://api.scryfall.com"
    endpoint = "cards/search"
    parameters = "order=cmc&unique=cards"
    request = f"{domain}/{endpoint}?{parameters}&q={_encode(query)}"
    response = requests.get(request)
    with open("data/response.json", "w", encoding="UTF-8") as f:
        f.write(response.text)

def _encode(raw: str) -> str:
    encoded = _percent_encoding(raw)
    encoded = encoded.replace(" ", "+")
    return encoded

def _percent_encoding(raw: str) -> str:
    encoded = raw
    for char, encoding in ENCODINGS.items():
        encoded = encoded.replace(char, encoding)
    return encoded

if __name__ == "__main__":
    search("banned:historic")
