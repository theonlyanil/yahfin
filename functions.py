import requests
import pandas as pd
from utils import formatColumn, chunk_list

base_query = 'https://query2.finance.yahoo.com'

"""This function takes in a symbol and gets the latest Income Statements from Yahoo Finance"""
def getIncomeStatementHistory(symbol):
    url = base_query + f'/v10/finance/quoteSummary/{symbol}?modules=incomeStatementHistory'
    req = requests.get(url)
    jsonData = req.json()
    income_statements = jsonData['quoteSummary']['result'][0]['incomeStatementHistory']['incomeStatementHistory']
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
    url = base_query + f'/v10/finance/quoteSummary/{symbol}?modules=assetProfile'
    req = requests.get(url)
    jsonData = req.json()

    asset_profile = jsonData['quoteSummary']['result'][0]['assetProfile']
    df = pd.DataFrame(asset_profile)

    return df

# To be modified
def getPriceData(symbol):
    url = base_query + f'/v10/finance/quoteSummary/{symbol}?modules=price'
    req = requests.get(url)
    jsonData = req.json()

    price_data = jsonData['quoteSummary']['result'][0]['price']
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
