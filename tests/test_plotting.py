# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 2

import numpy as np
import pandas as pd
from src.plotting import plot_ticker

def test_plot_ticker_returns_fig_and_ax_with_10_points():
    dates = np.arange(10)
    prices = np.array([100.0, 101.0, 102.0, 103.0, 104.0,
                        105.0, 106.0, 107.0, 108.0, 109.0])

    fig, ax = plot_ticker("AAPL", dates, prices)

    line = ax.lines[0]
    assert len(line.get_xdata()) == 10
    assert len(line.get_ydata()) == 10
    assert list(line.get_ydata()) == list(prices)

def test_plot_ticker_with_real_datetime_index():
    dates = pd.date_range("2026-08-28", periods=10, freq="B", tz="America/New_York")
    prices = np.array([100.0, 101.0, 102.0, 103.0, 104.0,
                        105.0, 106.0, 107.0, 108.0, 109.0])

    fig, ax = plot_ticker("AAPL", dates, prices)

    line = ax.lines[0]
    assert len(line.get_xdata()) == 10
    assert len(line.get_ydata()) == 10
    assert list(line.get_ydata()) == list(prices)
