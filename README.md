### INF601 - Advanced Programming in Python
### Chase Coble
### Mini Project 2
 
 
# Yahoo Stock Plotter
 
Generates line plots for the last 10 trading days of the following stocks: Oracle, Amazon, Nvidia, Google (Alphabet), and Apple
 
## Description
 
Developed with AI-assisted test driven development. This uses Yahoo Finance's package yFinance to fetch closing prices for the stocks over the past 30 days, then I clipped it to the last 10 trading days. After conversion into a numpy array, matplotlib is utilized to create plots, which are then saved to /charts. Note that yFinance is known for aggressive rate-limiting, and this application is designed to fail fast, the script aborts if rate limit is triggered, due to Yahoo rate-limits by session.
 
## Getting Started
 
### Dependencies
 
* Python 3
* matplotlib
* pandas
* numpy
* yfinance
 
## Installing

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/miniproject2ChaseCoble.git
   cd miniproject2ChaseCoble
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
 
### Executing program
 
Run the main script from inside the `src` directory:

```bash
cd src
python3 main.py
```

This will fetch the last 10 trading days of closing price data for 5 tickers, generate one line chart per ticker, and save them as PNG files in a `charts/` folder (created automatically if it doesn't exist).

**Note:** This project uses the [yfinance](https://pypi.org/project/yfinance/) library to pull live stock data from Yahoo Finance. Yahoo occasionally rate-limits requests. If you see a rate-limit error and no charts are generated, wait a few minutes and try again.

 
## Authors

Chase Coble
 

## Version History
* 1.1.1
    * README updated
* 1.1
    * Plot format polish applied. 
* 1.0
    * Full functionality confirmed, plots are subpar presentation
* 0.11
    * Fixed bug where output/_dir was not set correctly
* 0.10
    * Claude implements plot saving
* 0.9
    * Test written for proper plot saving
* 0.8
    * Claude implements plotting function (naive)
* 0.7
    * Wrote test for matplotlib plotting functions
* 0.6
    * Claude implements orchestrator
    * Test added for correct dictionary keying
* 0.5
    * Test written for orchestrator
* 0.4
    * Claude implements custom error class
* 0.3
    * Test written for rate-limit error handling
* 0.2
    * Claude implements to/_price/_array and fetch/_ticker
* 0.1
    * Initial Release after two tests written

## License
* This project is unlicensed

## Acknowledgements
* Full API reference in the [yFinance Reference](https://ranaroussi.github.io/yfinance/reference/index.html)

## AI Usage
    * Claude Code utilized to create implementation code after human writing of tests. Human execution of tests and by-change diffanalysis.
