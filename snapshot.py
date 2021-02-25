import os
import yfinance as yf

with open('symbols.csv') as f:
    lines = f.read().splitlines()
    for symbol in lines:
        print(symbol)
        data = yf.download(symbol, start="2020-07-01", end="2021-02-25")
        data.to_csv("datasets/{}.csv".format(symbol))