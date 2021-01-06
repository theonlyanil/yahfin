import pandas as pd
import time
import pdb

from .utils import chunk_list, epochToDatetimeList, returnDf, formatColumns
from .engines import v8_period, v8_range, v7multi, v10, v7_options

""" Gets a company's asset profile as in: address, summary, website, employees, etc. """
def getAssetProfile(symbol, kmp):
    try:
        asset_profile = v10(symbol, 'assetProfile')['assetProfile']

        # If user asks for kmp (key managerial personnel), return specific data
        if kmp == 'kmp':
            profile = asset_profile['companyOfficers']
            df = pd.DataFrame(profile)

            # formatColumns(df) because some values have options for 'raw' and 'fmt'.
            return formatColumns(df)
        else:
            df = pd.DataFrame(asset_profile)
            # Keep only the first row i.e. 'raw'
            df = df.iloc[:1]
            return df.to_dict('records')[0] # return as a dict
    except Exception as e:
        error = v10(symbol, 'incomeStatementHistory')
        return error


# To be modified
def getLivePriceData(symbol):
    try:
        price_data = v10(symbol, 'price')['price']
        df = pd.DataFrame(price_data)

        # Keep only the first row i.e. 'raw'
        df = df.iloc[:1]
        return df.to_dict('records')[0] # return as a dict
    except Exception as e:
        error = v10(symbol, 'incomeStatementHistory')
        return error


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
    # Extract every symbol separated by comma and this makes a list
    symbolss = symbols.split(',')

    # Filter list(symbolss) to drop '' and make a set (unique vals) and sort it
    symbolSet = sorted(set(filter(None, symbolss)))

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
        if symbolSet[0] == '':
            return 'No symbols were passed'

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
        end = int(time.mktime(time.strptime(str(end_date), '%Y-%m-%d'))) + 86400    #end is always +1day

        data_lists = v8_period(symbol, start, end, interval)
    else:
        data_lists = v8_range(symbol, period, interval)

    try:
        timestamps = pd.DataFrame(epochToDatetimeList(data_lists[0]))
        priceData = pd.DataFrame(data_lists[1], columns=['open', 'high', 'low', 'close', 'volume'])

        # Join both DFs
        final_df = timestamps.join(priceData)

        final_df.columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume']

        return final_df
    except Exception as e:
        return data_lists

"""This function takes in a symbol and gets the latest Income Statements from Yahoo Finance"""
def getIncomeStatementHistory(symbol):
    try:
        income_statements = v10(symbol, 'incomeStatementHistory')['incomeStatementHistory']['incomeStatementHistory']
        return returnDf(income_statements)
    except Exception as e:
        error = v10(symbol, 'incomeStatementHistory')
        return error


"""This function takes in a symbol and gets the latest Income Statements (Qtrly) from Yahoo Finance"""
def getIncomeStatementsQtr(symbol):
    try:
        income_statements = v10(symbol, 'incomeStatementHistoryQuarterly')['incomeStatementHistoryQuarterly']['incomeStatementHistory']
        return returnDf(income_statements)
    except Exception as e:
        error = v10(symbol, 'incomeStatementHistoryQuarterly')
        return error


def getBalanceSheetYearly(symbol):
    try:
        bs = v10(symbol, 'balanceSheetHistory')['balanceSheetHistory']['balanceSheetStatements']
        return returnDf(bs)
    except Exception as e:
        error = v10(symbol, 'balanceSheetHistory')
        return error


def getBalanceSheetQtrly(symbol):
    try:
        bs = v10(symbol, 'balanceSheetHistoryQuarterly')['balanceSheetHistoryQuarterly']['balanceSheetStatements']
        return returnDf(bs)
    except Exception as e:
        error = v10(symbol, 'balanceSheetHistoryQuarterly')
        return error


def getCashFlowsYearly(symbol):
    try:
        cf = v10(symbol, 'cashflowStatementHistory')['cashflowStatementHistory']['cashflowStatements']
        return returnDf(cf)
    except Exception as e:
        error = v10(symbol, 'cashflowStatementHistory')
        return error


def getCashFlowsQtrly(symbol):
    try:
        cf = v10(symbol, 'cashflowStatementHistoryQuarterly')['cashflowStatementHistoryQuarterly']['cashflowStatements']
        return returnDf(cf)
    except Exception as e:
        error = v10(symbol, 'cashflowStatementHistory')
        return error


def getFinancialAnalysisData(symbol):
    try:
        analysisData = v10(symbol, 'financialData')['financialData']
        df = pd.DataFrame(analysisData)

        # Keep only the first row i.e. 'raw'
        df = df.iloc[:1]
        return df.to_dict('records')[0] # return as a dict
    except Exception as e:
        error = v10(symbol, 'cashflowStatementHistory')
        return error

"""
    Returns Major Shareholders' percentage share by company's Symbol.
    New: Added retailers' shareholding.
"""
def getMajorHolders(symbol):
    try:
        holders = v10(symbol, 'majorHoldersBreakdown')['majorHoldersBreakdown']
        df = pd.DataFrame(holders)

        # Keep only the first row i.e. 'raw'
        df = df.iloc[:1]

        # renaming columns
        df = df.rename(columns={"insidersPercentHeld": "promoters", "institutionsFloatPercentHeld": "institutions"})

        pd.to_numeric(df['promoters'])
        pd.to_numeric(df['institutions'])

        # creating a new column: 'retailers': {1 - (promoters + institutions)}
        df['retailers'] =  1 - (df['promoters'] + df['institutions'])
        df = df[['promoters', 'institutions', 'retailers', 'institutionsCount']]

        return df.to_dict('records')[0] # return as a dict
    except Exception as e:
        error = v10(symbol, 'majorHoldersBreakdown')
        return error


"""
    # TODO: add try/except
    This function gets options data of a given symbol. Probably only available for US stocks.
    Also takes in an input of dataType i.e. calls, puts, dates, strikes, quotes
"""
def getOptionsData(symbol, dataType):
    optionsData = v7_options(symbol)
    options = None

    try:
        if dataType == 'calls':
            options = optionsData['options'][0]['calls']
        elif dataType == 'puts':
            options = optionsData['options'][0]['puts']
        elif dataType == 'dates':
            options = optionsData['expirationDates']
            options = epochToDatetimeList(options)  #because timestamps are unreadable in raw format
        elif dataType == 'strikes':
            options = optionsData['strikes']
        elif dataType == 'quotes':
            options = optionsData['quote']
            # Passes scaler values, so had to pass an index and return function from here.
            df = pd.DataFrame(options, index=[0])
            return df.to_dict('records')[0] # return as a dict
        else:
            # Wrong dataType, empty dataFrame is returned.
            return pd.DataFrame()

        df = pd.DataFrame(options)
        return df
    except Exception as e:
        return []
