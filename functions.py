import pandas as pd

from utils import chunk_list, epochToDatetimeList, returnDf
from engines import v8_period, v8_range, v7multi, v10

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

"""
    It gets symbol's historic price data (open, high, low, close) with timestamps.

    Start and End are provided as "YY-mm-dd" and converted to epocs (Yahoo Finance)

    It then calls v8 function (written in this module) and we convert timestamps
    and priceData into separate DataFrames and then we join both DFs and return.
"""
def getHistoricPrices(symbol, start_date=None, end_date=None, period=None, interval=None):
    data_lists = []
    if start_date and end_date:
        start = int(time.mktime(time.strptime(str(start_date), '%Y-%m-%d')))
        end = int(time.mktime(time.strptime(str(end_date), '%Y-%m-%d')))

        print(f'start: {start}, end: {end}')

        data_lists = v8_period(symbol, start, end, interval)
    else:
        data_lists = v8_range(symbol, period, interval)

    try:
        timestamps = pd.DataFrame(epochToDatetimeList(data_lists[0]))
        priceData = pd.DataFrame(data_lists[1], columns=['open', 'high', 'low', 'close', 'volume'])

        final_df = timestamps.join(priceData)
        final_df.columns = [['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume']]
        return final_df
    except Exception as e:
        return 'Please modify your period/interval'

"""This function takes in a symbol and gets the latest Income Statements from Yahoo Finance"""
def getIncomeStatementHistory(symbol):
    income_statements = v10(symbol, 'incomeStatementHistory')['incomeStatementHistory']['incomeStatementHistory']
    return returnDf(income_statements)

"""This function takes in a symbol and gets the latest Income Statements (Qtrly) from Yahoo Finance"""
def getIncomeStatementsQtr(symbol):
    income_statements = v10(symbol, 'incomeStatementHistoryQuarterly')['incomeStatementHistoryQuarterly']['incomeStatementHistory']
    return returnDf(income_statements)

def getBalanceSheetYearly(symbol):
    bs = v10(symbol, 'balanceSheetHistory')['balanceSheetHistory']['balanceSheetStatements']
    return returnDf(bs)

def getBalanceSheetQtrly(symbol):
    bs = v10(symbol, 'balanceSheetHistoryQuarterly')['balanceSheetHistoryQuarterly']['balanceSheetStatements']
    return returnDf(bs)
