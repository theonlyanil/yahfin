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
    df['totalRevenue'] = formatCell(df['totalRevenue'], 'raw')
    df['costOfRevenue'] = formatCell(df['costOfRevenue'], 'raw')
    df['grossProfit'] = formatCell(df['grossProfit'], 'raw')
    df['researchDevelopment'] = formatCell(df['researchDevelopment'], 'raw')
    df['sellingGeneralAdministrative'] = formatCell(df['sellingGeneralAdministrative'], 'raw')
    df['nonRecurring'] = formatCell(df['nonRecurring'], 'raw')
    df['otherOperatingExpenses'] = formatCell(df['otherOperatingExpenses'], 'raw')
    df['operatingIncome'] = formatCell(df['operatingIncome'], 'raw')
    df['totalOperatingExpenses'] = formatCell(df['totalOperatingExpenses'], 'raw')
    df['totalOtherIncomeExpenseNet'] = formatCell(df['totalOtherIncomeExpenseNet'], 'raw')
    df['ebit'] = formatCell(df['ebit'], 'raw')
    df['interestExpense'] = formatCell(df['interestExpense'], 'raw')
    df['incomeBeforeTax'] = formatCell(df['incomeBeforeTax'], 'raw')
    df['incomeTaxExpense'] = formatCell(df['incomeTaxExpense'], 'raw')
    df['minorityInterest'] = formatCell(df['minorityInterest'], 'raw')
    df['netIncomeFromContinuingOps'] = formatCell(df['netIncomeFromContinuingOps'], 'raw')
    df['discontinuedOperations'] = formatCell(df['discontinuedOperations'], 'raw')
    df['extraordinaryItems'] = formatCell(df['extraordinaryItems'], 'raw')
    df['effectOfAccountingCharges'] = formatCell(df['effectOfAccountingCharges'], 'raw')
    df['otherItems'] = formatCell(df['otherItems'], 'raw')
    df['netIncome'] = formatCell(df['netIncome'], 'raw')
    df['netIncomeApplicableToCommonShares'] = formatCell(df['netIncomeApplicableToCommonShares'], 'raw')

    df.to_csv('d.csv')
    print(df)

def formatCell(df_series, dataType):
    results = []
    for item in df_series:
        try:
            item = item[dataType]
            results.append(item)
        except Exception as e:
            results.append(0)
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
