import yfinance as yf

symbol = input("Enter a ticker symbol: ").upper()
ticker = yf.Ticker(symbol)
print("The last bid price of " + symbol + " is $" + str(ticker.info["bid"]))