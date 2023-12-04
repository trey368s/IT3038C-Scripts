import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import datetime, timedelta

symbol = input("Enter a stock symbol to view a candlestick chart of its most recent full trading day: ").upper()

today = datetime.today()
if today.weekday() == 0: 
    trading_day = today - timedelta(days=3)
elif today.weekday() == 6:
    trading_day = today - timedelta(days=2)
else:
    trading_day = today - timedelta(days=1)

data = yf.download(symbol, start=datetime(trading_day.year, trading_day.month, trading_day.day, 0, 0, 0),
                          end=datetime(trading_day.year, trading_day.month, trading_day.day, 23, 59, 59), interval="1h")

if not data.empty:
    data.index.name = 'Date'
    mpf.plot(data, type='candle', style='yahoo', title=f'Candlestick Chart for {symbol} on {trading_day.strftime("%m-%d-%Y")}')
else:
    print(f"No hourly data available for {symbol} on {trading_day.strftime('%m-%d-%Y')}")
