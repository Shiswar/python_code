import datetime, requests, pandas as pd, requests
import matplotlib.pyplot as plt
import numpy as np
import math
import json

from candlesticks import * 

base_url = "https://api.gemini.com/v2/candles"
symbol = "ethusd"
timeframe = "6hr"

url = f"{base_url}/{symbol}/{timeframe}"

response = requests.get(url=url)

# def hammer(candlestick):
#     top_wick_size = candlestick["High"] - max(candlestick["Open"], candlestick["Close"])
#     bot_wick_size = min(candlestick["Open"], candlestick["Close"]) - candlestick["Low"]
#     body_size = abs(candlestick["Open"] - candlestick["Close"])+0.00001
    
#     if (top_wick_size/body_size) >= 3 and (bot_wick_size/body_size) <= 1.2:
#         print(candlestick)
#         return True
#     elif (bot_wick_size/body_size) >= 3 and  (top_wick_size/body_size)<= 1.2:
#         print(candlestick)
#         return True


def to_dataframe(json_data: str) -> pd.DataFrame:
    candles_df = pd.DataFrame(json_data)
    candles_df.columns = [
        "Time",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]
    candles_df["Time"] = candles_df["Time"].apply(
        lambda x: datetime.datetime.fromtimestamp(x/1000.0)
    )
    return candles_df

def to_candle_group(json_data: str):
    df = to_dataframe(json_data)
    open = df["Open"]
    close = df["Close"]
    high = df["High"]
    low = df["Low"]
    volume = df["Volume"]
    c = CandleGroup(open, high, low, close, volume)
    return c
        


def plot_down_arrow():
    plt.plot([x[idx], x[idx]], [val['High'] + 50, val['High'] + 60], color = "red")
    plt.plot([x[idx]-1, x[idx]], [val['High'] + 60, val['High'] + 50], color = "red")
    plt.plot([x[idx]+1, x[idx]], [val['High'] + 60, val['High'] + 50], color = "red")

def plot_up_arrow():
    plt.plot([x[idx], x[idx]], [val['Low'] - 50, val['Low'] - 60], color = "blue")
    plt.plot([x[idx]-1, x[idx]], [val['Low'] - 60, val['Low'] - 50], color = "blue")
    plt.plot([x[idx]+1, x[idx]], [val['Low'] - 60, val['Low'] - 50], color = "blue")

df = to_dataframe(response.json())

candle_list = to_candle_group(response.json())











# for index, candlestick in df.iterrows():
    # if str(candlestick["Time"]) == "2021-09-18 12:00:00":
    #     print(candlestick)
    #     top_wick_size = candlestick["High"] - max(candlestick["Open"], candlestick["Close"])
    #     bot_wick_size = min(candlestick["Open"], candlestick["Close"]) - candlestick["Low"]
    #     body_size = abs(candlestick["Open"] - candlestick["Close"])

    #     print("top:",top_wick_size)
    #     print("bot:",bot_wick_size)
    #     print("Body:",body_size)
    #     print(top_wick_size/body_size)
    #     print(bot_wick_size/body_size)
    #     break
    # is_hammer(candlestick)

x = np.arange(0,len(df))
fig, ax = plt.subplots(1, figsize=(12,6))

# maximas = candle_list.get_maxima_indexes()
# minimas = candle_list.get_minima_indexes()
# three_green_candles = candle_list.get_three_green_candles()
# bearish_engulfing = candle_list.get_bearish_engulfing_2()
hanging_man = candle_list.hanging_man_5()

for idx, val in df.iterrows():
    color = "red" if val["Open"] > val["Close"] else "green"

    plt.plot([x[idx], x[idx]], [val['Low'], val['High']], color = color)
    plt.plot([x[idx]-0.2, x[idx]], [val['Open'], val['Open']], color = color)
    plt.plot([x[idx], x[idx]+0.2], [val['Close'], val['Close']], color = color)

    # if idx in maximas:
    #     plot_down_arrow()
    # if idx in minimas:
    #     plot_up_arrow()
    # if idx in three_green_candles:
    #     plot_up_arrow()
    # if idx in bearish_engulfing:
    #     plot_down_arrow()
    if idx in hanging_man:
        plot_down_arrow()


plt.show()