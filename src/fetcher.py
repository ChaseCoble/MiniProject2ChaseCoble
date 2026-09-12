# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 2

import yfinance as yf


def fetch_ticker(symbol):
    ticker = yf.Ticker(symbol)
    history = ticker.history(period="1mo")
    return history["Close"].tail(10)
