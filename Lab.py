import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import ipywidgets

%matplotlib inline

coins = pd.read_csv(r"https://raw.githubusercontent.com/febos/mipt-python19/master/LabWork/coins.csv")
coins.head(10)

typesofcoins = set(coins['symbol'])
countofcoins = len(typesofcoins)
countofcoins

datas = set(coins['date'])
coins['date'].min()

coins['date'].max()

set(coins.isnull()['price'])

coins.loc[(coins['price'] == coins['price'].max()), ['date', 'symbol']]

typesofcoins = list(typesofcoins)
typesofcoins
len(typesofcoins)

capital = []
for i in range(len(typesofcoins)):
    summary = coins[(coins['symbol'] == typesofcoins[i])]['market'].sum()
    capital.append(summary)
len(capital)
mx = 0
for i in range(len(typesofcoins)):
    if capital[i] > mx:
        mx = capital[i]
mx
mxtypesofcoins[capital.index(mx)]

mn = capital[0]
for i in range(len(typesofcoins)):
    if capital[i] < mn:
        mn = capital[i]
mn
typesofcoins[capital.index(mn)]

mpl.rcParams.update({'font.size': 0.0})
plt.pie(capital, labels = typesofcoins, autopct="%.1f%%", radius=4.0)
plt.show()

def plot_fancy_price_action(coins, symbol, start_date, end_date):
    tmp = coins.loc[(coins['symbol'] == symbol), ['date', 'high', 'low']]
    tmp = tmp[(coins['date'] >= start_date)]
    tmp = tmp[(coins['date'] <= end_date)]

    x = list(tmp['date'])
    y1 = list(tmp['high'])
    y2 = list(tmp['low'])

    fig = plt.figure(
        figsize=(16, 9),
        facecolor='whitesmoke',
        dpi=200
    )

    plt.suptitle('This is a title for the whole figure', fontsize=30)
    plt.title('This is a title for our plot', fontsize=20)

    plt.plot(x, y1, color="blue")
    plt.plot(x, y2, color="blue")

    plt.xlabel(
        'This is an date axis label',
        fontdict=dict(family='serif', color='darkred', weight='normal', size=16)
    )
    plt.ylabel(
        'This is a cost axis label',
        fontdict=dict(family='monospace', color='peru', weight='light', size=25)
    )

    plt.grid(True)

    plt.show()

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

def find_most_severe_pump_and_dump(coins, symbol, start_date, end_date):
    tmp = coins.loc[(coins['symbol'] == symbol), ['date', 'high', 'open', 'close']]
    tmp = tmp[(coins['date'] >= start_date)]
    tmp = tmp[(coins['date'] <= end_date)]
    pmp = list(tmp['high'] / tmp['open'])
    dmp = list(tmp['high'] / tmp['close'])
    time = list(tmp['date'])
    res = []
    for i in range(len(pmp)):
        res.append(maximum(pmp[i],dmp[i]))
    mx = 0
    for i in range(len(res)):
        if res[i] > mx:
            mx = res[i]
    ind = res.index(mx)
    result = [symbol, time[ind], mx]
    return result

find_most_severe_pump_and_dump(coins, 'BTC', '2018-05-28', '2018-06-06')
