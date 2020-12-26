import requests
import pandas as pd
import time
from datetime import datetime

from utils import formatColumn, chunk_list, epochToDatetimeList

base_query = 'https://query2.finance.yahoo.com'

"""This function takes in a symbol and gets the latest Income Statements from Yahoo Finance"""
def getIncomeStatementHistory(symbol):

    income_statements = v10(symbol, 'incomeStatementHistory')['incomeStatementHistory']['incomeStatementHistory']
    df = pd.DataFrame(income_statements)

    # Format cells
    df['endDate'] = formatColumn(df['endDate'], 'fmt')
    df['totalRevenue'] = formatColumn(df['totalRevenue'], 'raw')
    df['costOfRevenue'] = formatColumn(df['costOfRevenue'], 'raw')
    df['grossProfit'] = formatColumn(df['grossProfit'], 'raw')
    df['researchDevelopment'] = formatColumn(df['researchDevelopment'], 'raw')
    df['sellingGeneralAdministrative'] = formatColumn(df['sellingGeneralAdministrative'], 'raw')
    df['nonRecurring'] = formatColumn(df['nonRecurring'], 'raw')
    df['otherOperatingExpenses'] = formatColumn(df['otherOperatingExpenses'], 'raw')
    df['operatingIncome'] = formatColumn(df['operatingIncome'], 'raw')
    df['totalOperatingExpenses'] = formatColumn(df['totalOperatingExpenses'], 'raw')
    df['totalOtherIncomeExpenseNet'] = formatColumn(df['totalOtherIncomeExpenseNet'], 'raw')
    df['ebit'] = formatColumn(df['ebit'], 'raw')
    df['interestExpense'] = formatColumn(df['interestExpense'], 'raw')
    df['incomeBeforeTax'] = formatColumn(df['incomeBeforeTax'], 'raw')
    df['incomeTaxExpense'] = formatColumn(df['incomeTaxExpense'], 'raw')
    df['minorityInterest'] = formatColumn(df['minorityInterest'], 'raw')
    df['netIncomeFromContinuingOps'] = formatColumn(df['netIncomeFromContinuingOps'], 'raw')
    df['discontinuedOperations'] = formatColumn(df['discontinuedOperations'], 'raw')
    df['extraordinaryItems'] = formatColumn(df['extraordinaryItems'], 'raw')
    df['effectOfAccountingCharges'] = formatColumn(df['effectOfAccountingCharges'], 'raw')
    df['otherItems'] = formatColumn(df['otherItems'], 'raw')
    df['netIncome'] = formatColumn(df['netIncome'], 'raw')
    df['netIncomeApplicableToCommonShares'] = formatColumn(df['netIncomeApplicableToCommonShares'], 'raw')

    return df

""" Gets a company's asset profile as in: address, summary, website, employees, etc. """
def getAssetProfile(symbol):
    asset_profile = v10(symbol, 'assetProfile')['assetProfile']
    df = pd.DataFrame(asset_profile)

    return df

# To be modified
def getLivePriceData(symbol):
    price_data = v10(symbol, 'price')['price']
    df = pd.DataFrame(price_data)
    return df

"""
    This function returns data for multiple symbols in one go
    (or more if symbols are more than 100).

    Input: "AAPL, MSFT, ESCORTS.NS, JSLHISAR.NS" #Spaces_are_optional

    Outputs: CMP, marketCap, Day High+Low+Volume, bid_ask, and more!
"""
def getMultiSymbolData(symbols):
    # A base DataFrame to which we will append more DFs later in this function.
    base_df = pd.DataFrame()

    # first remove spaces, if any
    symbols = symbols.replace(" ", "")

    # Extract every symbol separated by comma and store in a set (unique values)
    symbolss = symbols.split(',')
    symbolSet = set()
    for symbol in symbolss:
        symbolSet.add(symbol)

    symbolSet = sorted(symbolSet) # sort the list

    # if symbolSet length is  more than 100, split it into multiples of 100, and
    # find values and attach to one DataFrame
    if len(symbolSet) > 100:
        # Splitting a list into multiple lists of size 100
        symbolList = list(chunk_list(symbolSet, 100))

        # Iterate through each list containing
        for singleSymbolList in symbolList:
            # convert list into a single String
            symbols = ",".join(str(x) for x in singleSymbolList)

            # Run v7multi and get a DataFrame and append to base_df
            base_df = base_df.append(v7multi(symbols))
    else:
        # convert list into a single String
        symbols = ",".join(str(x) for x in symbolSet)

        # Run v7multi and get a DataFrame and append to base_df
        base_df = base_df.append(v7multi(symbols))
    return base_df

""" Yahoo Finance V7 Multi Endpoint """
def v7multi(symbols):
    url = base_query + f"/v7/finance/quote?symbols={symbols}"
    req = requests.get(url)
    jsonData = req.json()
    multiData = jsonData['quoteResponse']['result']
    df = pd.DataFrame(multiData)
    df.set_index('symbol', inplace=True, drop=True)
    return df

""" Yahoo Finance V10 Single Symbol Endpoint with Module(s) feature """
def v10(symbol, module):
    url = base_query + f'/v10/finance/quoteSummary/{symbol}?modules={module}'
    req = requests.get(url)
    jsonData = req.json()
    data = jsonData['quoteSummary']['result'][0]
    return data

""" Yahoo Finance V8 Single Symbol Endpoint with start, end and interval """
def v8(symbol, start_date, end_date, interval):
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?period1={start_date}&period2={end_date}&interval={interval}'
    print(url)
    req = requests.get(url)
    jsonData = req.json()

    # We'll need these two data points:
    timestamps = jsonData['chart']['result'][0]['timestamp']
    priceData = jsonData['chart']['result'][0]['indicators']['quote'][0]

    # Returns a list of timestamps and priceData
    return [timestamps, priceData]

"""
    It gets symbol's historic price data (open, high, low, close) with timestamps.

    Start and End are provided as "YY-mm-dd" and converted to epocs (Yahoo Finance)

    It then calls v8 function (written in this module) and we convert timestamps
    and priceData into separate DataFrames and then we join both DFs and return.
"""
def getHistoricPrices(symbol, start_date, end_date, period):
    start = int(time.mktime(time.strptime(str(start_date), '%Y-%m-%d')))
    end = int(time.mktime(time.strptime(str(end_date), '%Y-%m-%d')))

    data_lists = v8(symbol, start, end, period)
    timestamps = pd.DataFrame(epochToDatetimeList(data_lists[0]))
    priceData = pd.DataFrame(data_lists[1])

    final_df = timestamps.join(priceData)
    return final_df
