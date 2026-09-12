import yfinance as yf

df = yf.Ticker("AAPL").history(period="1mo")
print(df.columns)
print(df.index.dtype)
print(df.tail(10))
print(type(df))

