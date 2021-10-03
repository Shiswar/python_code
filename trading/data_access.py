import datetime, requests, pandas as pd, requests
import matplotlib.pyplot as plt
import numpy as np
import math
import json
from Classes.candlesticks import Candle as cs
from Classes.three_stick_pattern import ThreeStickPattern as tsp

base_url = "https://api.gemini.com/v2/candles"
symbol = "ethusd"
timeframe = "1hr"

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

def to_candle_list(json_data: str):
    dump = json.dumps(json_data)
    print(dump)
    


def plot_down_arrow():
    plt.plot([x[idx], x[idx]], [val['High'] + 50, val['High'] + 60], color = "red")
    plt.plot([x[idx]-1, x[idx]], [val['High'] + 60, val['High'] + 50], color = "red")
    plt.plot([x[idx]+1, x[idx]], [val['High'] + 60, val['High'] + 50], color = "red")

def plot_up_arrow():
    plt.plot([x[idx], x[idx]], [val['High'] + 50, val['High'] + 60], color = "blue")
    plt.plot([x[idx]-1, x[idx]], [val['High'] + 50, val['High'] + 60], color = "blue")
    plt.plot([x[idx]+1, x[idx]], [val['High'] + 50, val['High'] + 60], color = "blue")

df = to_dataframe(response.json())
# to_candle_list(response.json())

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

close = df["Close"]
for i in range(1, len(close)-2):
    sticks = [close[i-1], close[i], close[i+1]]
    three = tsp(sticks)
    
    if three.minima():
        plot_down_arrow()
        
    elif three.maxima:
        plot_up_arrow()


for idx, val in df.iterrows():
    color = "red" if val["Open"] > val["Close"] else "green"

    plt.plot([x[idx], x[idx]], [val['Low'], val['High']], color = color)
    plt.plot([x[idx]-0.1, x[idx]], [val['Open'], val['Open']])
    plt.plot([x[idx], x[idx]+0.1], [val['Close'], val['Close']])
    # if hammer(val):
    #     plot_down_arrow()
    
 


    
    
    # last_3 = tsp.ThreeStickPattern[c0, c1, c2]

    # if last_3.deliberation:
    #     plot_down_arrow()




    # if str(val["Time"]) == "2021-09-12 12:00:00":
    #     break

plt.show()