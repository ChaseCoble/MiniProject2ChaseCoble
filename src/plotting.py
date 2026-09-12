# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 2

import matplotlib.pyplot as plt


def plot_ticker(symbol, dates, prices):
    fig, ax = plt.subplots()
    ax.plot(dates, prices, marker="o")
    ax.set_title(f"Last 10 Trading Days: {symbol}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Close")
    return fig, ax
