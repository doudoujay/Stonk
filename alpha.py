import requests
import random

API_KEYS = ["EPYK5HZP5TBKRQ33", "4WK4K1VSJJP35G3X", "V0AF5474PBO74L14", "EPYK5HZP5TBKRQ33", "KPRAZJ48JTRUJEJW",
            "6M970W7SHGVKG0P3", "M2TEZ2AY2ASYVG2F", "J5QTBVMKFJLPH78M", "VRNR2V62QUEH1Y58", "UXVVD1BXIYUHWMOZ"]

def search_ticker(ticker):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ticker}&apikey={random.choice(API_KEYS)}'
    r = requests.get(url)
    data = r.json()
    return data

def check_ticker(ticker):
    data = search_ticker(ticker)
    if "bestMatches" in data:
        valid_symbols = [d["1. symbol"] for d in data["bestMatches"]]
        if ticker in valid_symbols:
            return True
    else:
        raise AssertionError("bestMatches not found")
    return False

print(check_ticker("INPX"))