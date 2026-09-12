import pandas as pd
from unittest.mock import patch, MagicMock
from src.fetcher import fetch_ticker, TickerFetchError
from yfinance.exceptions import YFRateLimitError
import pytest

def make_fake_history_df(n=20):
    """Mirrors real yfinance shape: tz-aware DatetimeIndex, Close column, no Adj Close."""
    idx = pd.date_range("2026-08-01", periods=n, freq="B", tz="America/New_York")
    return pd.DataFrame({
        "Open": range(n),
        "High": range(n),
        "Low": range(n),
        "Close": range(100, 100 + n),
        "Volume": range(n),
        "Dividends": [0.0] * n,
        "Stock Splits": [0.0] * n,
    }, index=idx)

def test_fetch_ticker_returns_last_10_closes():
    fake_df = make_fake_history_df(20)
    mock_ticker_instance = MagicMock()
    mock_ticker_instance.history.return_value = fake_df

    with patch("src.fetcher.yf.Ticker", return_value=mock_ticker_instance) as mock_ticker_cls:
        result = fetch_ticker("AAPL")

    mock_ticker_cls.assert_called_once_with("AAPL")
    assert len(result) == 10
    assert result.iloc[-1] == 119

def test_fetch_ticker_raises_on_rate_limit():
    mock_ticker_instance = MagicMock()
    mock_ticker_instance.history.side_effect = YFRateLimitError()

    with patch("src.fetcher.yf.Ticker", return_value=mock_ticker_instance):
        with pytest.raises(TickerFetchError):
            fetch_ticker("AAPL")
