import requests
import pandas as pd
import time
from datetime import datetime

query1 = 'https://query1.finance.yahoo.com'
query2 = 'https://query2.finance.yahoo.com'

""" Yahoo Finance V7 Multi Endpoint """
def v7multi(symbols):
    url = query2 + f"/v7/finance/quote?symbols={symbols}"
    req = requests.get(url)
    jsonData = req.json()
    multiData = jsonData['quoteResponse']['result']
    df = pd.DataFrame(multiData)
    df.set_index('symbol', inplace=True, drop=True)
    return df

""" Yahoo Finance V7 Options Endpoint """
def v7_options(symbol):
    url = query1 + f'/v7/finance/options/{symbol}'
    req = requests.get(url)
    jsonData = req.json()
    optionData = jsonData['optionChain']['result'][0]
    return optionData

""" Yahoo Finance V10 Single Symbol Endpoint with Module(s) feature """
def v10(symbol, module):
    url = query2 + f'/v10/finance/quoteSummary/{symbol}?modules={module}'
    req = requests.get(url)
    jsonData = req.json()
    data = jsonData['quoteSummary']['result'][0]
    return data

""" Yahoo Finance V8 Single Symbol Endpoint with start, end and interval """
def v8_period(symbol, start_date, end_date, interval):
    url = f'{query2}/v8/finance/chart/{symbol}?period1={start_date}&period2={end_date}&interval={interval}'
    print(url)
    req = requests.get(url)
    jsonData = req.json()

    # We'll need these two data points:
    timestamps = jsonData['chart']['result'][0]['timestamp']
    priceData = jsonData['chart']['result'][0]['indicators']['quote'][0]

    # Returns a list of timestamps and priceData
    return [timestamps, priceData]

""" Yahoo Finance V8 Single Symbol Endpoint with range and interval """
def v8_range(symbol, range, interval):
    url = f'{query2}/v8/finance/chart/{symbol}?range={range}&interval={interval}&events=divsplit'
    print(url)
    req = requests.get(url)
    jsonData = req.json()

    try:
        # We'll need these two data points:
        timestamps = jsonData['chart']['result'][0]['timestamp']
        priceData = jsonData['chart']['result'][0]['indicators']['quote'][0]
        events = jsonData['chart']['result'][0]['events']

        # Returns a list of timestamps and priceData
        return [timestamps, priceData, events]
    except Exception as e:
        return 'Please modify your period/interval'
