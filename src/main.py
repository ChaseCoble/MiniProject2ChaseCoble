# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 2

from orchestrator import run_all_fetches
from transform import to_price_array
from plotting import plot_ticker
from saving import save_chart
from fetcher import TickerFetchError

TICKERS = ["ORCL", "AAPL", "NVDA", "AMZN", "GOOGL"]

def main():
    try:
        results = run_all_fetches(TICKERS)
    except TickerFetchError as e:
        print(f"Failed to fetch data: {e}")
        raise SystemExit(1)

    for ticker, series in results.items():
        prices = to_price_array(series)
        dates = series.index
        fig, ax = plot_ticker(ticker, dates, prices)
        save_chart(fig, ticker, output_dir="../charts")

    print(f"Saved {len(results)} charts to ../charts/")

if __name__ == "__main__":
    main()

