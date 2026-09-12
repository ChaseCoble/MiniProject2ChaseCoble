# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 2

import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


def plot_ticker(symbol, dates, prices):
    fig, ax = plt.subplots()
    ax.plot(dates, prices, marker="o")
    ax.set_title(f"Last 10 Trading Days: {symbol}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Close")
    ax.yaxis.set_major_formatter(StrMethodFormatter("${x:,.2f}"))
    fig.autofmt_xdate()
    fig.subplots_adjust(left=0.15)
    return fig, ax
