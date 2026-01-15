import pandas as pd
import time
import datetime
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
def getMultiSymbolData(symbols_str):
    # 1. Clean and unique-ify the symbols list
    # Strip spaces and split by comma
    raw_list = [s.strip() for s in symbols_str.split(',') if s.strip()]
    symbol_set = sorted(set(raw_list))

    if not symbol_set:
        return 'No symbols were passed'

    # 2. Prepare a list to hold the DataFrames
    all_dfs = []
    
    # 3. Chunking logic (Optimized)
    chunk_size = 100
    for i in range(0, len(symbol_set), chunk_size):
        chunk = symbol_set[i:i + chunk_size]
        symbols_chunk_str = ",".join(chunk)
        
        print(f"Fetching chunk {i//chunk_size + 1}: {len(chunk)} symbols")
        
        # Fetch data using your existing v7multi
        df_chunk = v7multi(symbols_chunk_str)
        
        # Ensure we actually got a DataFrame back (handle errors)
        if isinstance(df_chunk, pd.DataFrame):
            all_dfs.append(df_chunk)
        else:
            print(f"Warning: Failed to fetch data for chunk starting with {chunk[0]}")

    # 4. Final Merge (The "Apt" way)
    if not all_dfs:
        return "Failed to retrieve any data."
        
    final_df = pd.concat(all_dfs, ignore_index=True)
    return final_df

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
        data = v10(symbol, 'majorHoldersBreakdown')
        # Check if v10 returned an error string or valid dict
        if isinstance(data, str): return data 
        
        breakdown = data['majorHoldersBreakdown']

        # Extracting raw values directly (Clean & Fast)
        promoters = breakdown.get('insidersPercentHeld', {}).get('raw', 0)
        institutions = breakdown.get('institutionsPercentHeld', {}).get('raw', 0)
        inst_count = breakdown.get('institutionsCount', {}).get('raw', 0)

        others = round(1 - (promoters + institutions), 5)

        return {
            "promoters": round(promoters * 100, 2),
            "institutions": round(institutions * 100, 2),
            "others": round(others * 100, 2),
            "institutionsCount": inst_count
        }
    except Exception as e:
        return f"Processing Error: {str(e)}"


"""
    # TODO: add try/except
    This function gets options data of a given symbol. Probably only available for US stocks.
    Also takes in an input of dataType i.e. calls, puts, dates, strikes, quotes
"""
def getOptionsData(symbol, dataType, date=None):
    # Pass the date param to the engine
    optionsData = v7_options(symbol, date)
    
    if not optionsData:
        return pd.DataFrame() # Return empty DF on failure

    try:
        # 1. Simple List/Dict Returns (Metadata)
        if dataType == 'dates':
            # Extract timestamps from the root 'expirationDates' list
            dates = optionsData.get('expirationDates', []) #
            return [datetime.datetime.fromtimestamp(d).strftime('%Y-%m-%d') for d in dates]            
        
        if dataType == 'strikes':
            return optionsData.get('strikes', []) #
            
        if dataType == 'quotes':
            # Return the raw dict directly; converting to DF and back is inefficient
            return optionsData.get('quote', {}) #

        # 2. Complex DataFrame Returns (Calls/Puts)
        # Check if the specific options chain list exists
        chain_list = optionsData.get('options', [])
        if not chain_list:
            return pd.DataFrame()

        # Extract the specific list of contracts
        raw_contracts = []
        if dataType == 'calls':
            raw_contracts = chain_list[0].get('calls', []) #
        elif dataType == 'puts':
            raw_contracts = chain_list[0].get('puts', []) #
        else:
            return pd.DataFrame()

        # 3. Create and CLEAN the DataFrame
        df = pd.DataFrame(raw_contracts)
        
        if df.empty:
            return df

        # FLATTENING LOGIC: Extract 'raw' values from Yahoo's dict wrappers
        # Example: {'raw': 284.16, 'fmt': '284.16'} -> 284.16
        for col in df.columns:
            # We check the first non-null value to see if it's a dict
            first_valid = df[col].dropna().iloc[0] if not df[col].dropna().empty else None
            
            if isinstance(first_valid, dict) and 'raw' in first_valid:
                # Apply extraction to the whole column
                df[col] = df[col].apply(lambda x: x['raw'] if isinstance(x, dict) else x)
        
        # 4. Standardize Dates (Optional but recommended)
        # Convert Unix timestamps to readable dates if they exist
        if 'lastTradeDate' in df.columns:
            df['lastTradeDate'] = pd.to_datetime(df['lastTradeDate'], unit='s')

        return df

    except Exception as e:
        print(f"Parsing Error: {str(e)}")
        return pd.DataFrame()