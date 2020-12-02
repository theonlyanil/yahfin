"""
    Yahoo Finance API Wrapper
    v0.1

    by Anil Sardiwal
    Started on 8th Nov'20
"""
import requests
import pandas as pd
import pdb

base_query = 'https://query2.finance.yahoo.com'

def  SymbolBase(symbol):
    symbol = None
    def __init__(self, symbol):
        symbol = symbol.upper()

    print(symbol)

    # TODO Price Data
    def history(self, period="1mo", interval="1d", start=None, end=None):
        url = base_query + f'/v8/finance/chart/{symbol}?symbol={symbol}&period1=0&period2=9999999999&interval=interval'

def getIncomeStatementHistory(symbol):
    print('doing')
    url = base_query + f'/v10/finance/quoteSummary/{symbol}?modules=incomeStatementHistory'
    req = requests.get(url)
    jsonData = req.json()
    income_statements = jsonData['quoteSummary']['result'][0]['incomeStatementHistory']['incomeStatementHistory']
    df = pd.DataFrame(income_statements)
    df['endDate'] = formatCell(df['endDate'], 'fmt')
    df['endDate'] = formatCell(df['endDate'], 'fmt')
    df['endDate'] = formatCell(df['endDate'], 'fmt')
    df['endDate'] = formatCell(df['endDate'], 'fmt')
    df.to_csv('d.csv')
    print(df)

def formatCell(df_series, dataType):
    results = []
    for item in df_series:
        item = item[dataType]
        results.append(item)
    return results
# Yahoo Finance Symbol Object (YFSO)
def Symbol(SymbolBase):

    def getSymbol(self):
        print('sds')
        return self.Symbol

    def getIncomeStatementHistory(self):
        print(self.Symbol)
        return SymbolBase(self.Symbol).getIncomeStatementHistory()


if __name__ == "__main__":
    getIncomeStatementHistory('msft')
