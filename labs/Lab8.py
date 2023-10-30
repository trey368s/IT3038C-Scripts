import requests
from bs4 import BeautifulSoup

symbol = input("Input a stock symbol: ")
url = "https://finance.yahoo.com/quote/"+symbol+"?p="+symbol
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find("fin-streamer", {'data-symbol': symbol } ).text

print("The current stock price of "+symbol+" is "+price)