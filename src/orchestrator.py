# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 2

from src.fetcher import fetch_ticker


def run_all_fetches(tickers):
    results = {}
    for ticker in tickers:
        results[ticker] = fetch_ticker(ticker)
    return results
