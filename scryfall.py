"""calls scryfall API for initial card list"""

import requests

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
    pass

def encode(raw: str):
    encoded = percent_encoding(raw)
    encoded = encoded.replace(" ", "+")
    return encoded

def percent_encoding(raw: str):
    encoded = raw
    for char, encoding in ENCODINGS.items():
        encoded = encoded.replace(char, encoding)
    return encoded

if __name__ == "__main__":
    print(encode("c=red pow:3"))
