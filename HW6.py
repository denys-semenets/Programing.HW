

import pandas as pd
import yfinance as yf

data= yf.Ticker("GLD")
df = pd.DataFrame(data.history(period="5y"))

df = df.drop(["Dividends","Stock Splits"],axis=1)
df["ave_10"] = df["Close"].rolling(window = 10).mean()
df["ave_50"] = df["Close"].rolling(window = 50).mean()

df = df[49:]
df["sign"] = 0
df.sign[0] = "Buy"
df.sign[-1] = "Sell"
for i in range(len(df)-1):
    if (df["ave_10"][i] < df["ave_50"][i]) & (df["ave_50"][i+1] < df["ave_10"][i+1]):
        df["sign"][i+1] = "Buy"
    elif (df["ave_10"][i] > df["ave_50"][i]) & (df["ave_50"][i+1] > df["ave_10"][i+1]):
        df["sign"][i+1] = "Sell"

df = df[df.sign != 0]
df_trade  = df[["Open","sign"]]


money = 100000
shares =0
for i in range(len(df_trade)):
    if df_trade.sign[i] =="Buy":
        shares = int(money/df_trade.Open[i])
        money = money - shares*df_trade.Open[i]
    elif df_trade.sign[i] =="Sell":
        money += shares*df_trade.Open[i]
        shares = 0
print(round(money,2))
