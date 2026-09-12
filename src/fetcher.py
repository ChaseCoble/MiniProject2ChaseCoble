# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 2

import yfinance as yf
from yfinance.exceptions import YFRateLimitError


class TickerFetchError(Exception):
    pass


def fetch_ticker(symbol):
    ticker = yf.Ticker(symbol)
    try:
        history = ticker.history(period="1mo")
    except YFRateLimitError as e:
        raise TickerFetchError(e)
    return history["Close"].tail(10)
