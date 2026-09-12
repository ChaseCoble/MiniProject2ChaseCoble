# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 2

import pandas as pd
from unittest.mock import patch
from src.orchestrator import run_all_fetches
from src.fetcher import TickerFetchError
import pytest

TICKERS = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]

def test_run_all_fetches_returns_all_five_on_success():
    fake_series = pd.Series(range(10))

    with patch("src.orchestrator.fetch_ticker", return_value=fake_series) as mock_fetch:
        results = run_all_fetches(TICKERS)

    assert mock_fetch.call_count == 5
    assert len(results) == 5
    assert all(len(s) == 10 for s in results.values())

def test_run_all_fetches_aborts_on_any_failure():
    def side_effect(ticker):
        if ticker == "GOOG":
            raise TickerFetchError("rate limited")
        return pd.Series(range(10))

    with patch("src.orchestrator.fetch_ticker", side_effect=side_effect) as mock_fetch:
        with pytest.raises(TickerFetchError):
            run_all_fetches(TICKERS)

    assert mock_fetch.call_count == 3
