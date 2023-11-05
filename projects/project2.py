from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta


days=1
apiKey = "PK4PC5CXDNCF4UTBITT4"
apiSecret = "4xIewFitft6JCzwtdH9hVSAJZI6cHNBiA78f9IRz"
symbol = input("Enter a ticker symbol for information on it's last complete trading day: ").upper()

while True:
    try:
        client = StockHistoricalDataClient(apiKey, apiSecret)

        request_params = StockBarsRequest(
                                symbol_or_symbols=[symbol],
                                timeframe=TimeFrame.Day,
                                start=datetime.today() - timedelta(days),
                                end=datetime.today(),
                                limit = 1
                        )

        bars = client.get_stock_bars(request_params)

        print(bars.df)
        break
    except:
        days+=1
