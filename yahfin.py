"""
    Yahoo Finance API Wrapper
    v0.2

    by Anil Sardiwal
    Started on 8th Nov'20
    last modified on 27/12/2020
"""
from functions import getIncomeStatementHistory,  getAssetProfile,  getLivePriceData,  getMultiSymbolData, getHistoricPrices, getIncomeStatementsQtr, getBalanceSheetYearly, getBalanceSheetQtrly, getCashFlowsYearly, getCashFlowsQtrly, getFinancialAnalysisData, getMajorHolders, getOptionsData

# Symbol class object
class Symbol:
    def __init__(self,  symbol,  start=None, end=None, period='max', interval='1d'):
        self.symbol = symbol.upper()
        self.start = start
        self.end = end
        self.period = period
        self.interval = interval

    def incomeStatements(self):
        return getIncomeStatementHistory(self.symbol)

    def incomeStatementsQtr(self):
        return getIncomeStatementsQtr(self.symbol)

    def balanceSheets(self):
        return getBalanceSheetYearly(self.symbol)

    def balanceSheetsQtr(self):
        return getBalanceSheetQtrly(self.symbol)

    def cashFlows(self):
        return getCashFlowsYearly(self.symbol)

    def cashFlowsQtr(self):
        return getCashFlowsQtrly(self.symbol)

    def analysis(self):
        return getFinancialAnalysisData(self.symbol)

    def shareholding(self):
        return getMajorHolders(self.symbol)

    def profile(self):
        return getAssetProfile(self.symbol)

    def livePriceData(self):
        return getLivePriceData(self.symbol)

    def multi(self):
        return getMultiSymbolData(self.symbol)

    def history(self):
        return getHistoricPrices(self.symbol, self.start, self.end, self.period, self.interval)

    def options(self, dataType='calls'):
        return getOptionsData(self.symbol, dataType)

# Test!
if __name__ == "__main__":
    #msft = Symbol('MSFT')
    #print(msft.profile())

    #msft = Symbol('TSLA', start='2020-12-01', end='2020-12-05')
    #msft = Symbol('TSLA', start='2020-12-01', end='2020-12-02', interval='3m')
    #msft = Symbol('TSLA')
    #print(msft.history())

    #symbols = Symbol('TSLA, MSFT, AAPL, GOOG')
    #print(symbols.multi()['marketCap'])

    #tsla = Symbol('TSLA')
    #print(tsla.incomeStatementsQtr())

    #tsla = Symbol('TSLA')
    #print(tsla.balanceSheets())

    #tsla = Symbol('TSLA')
    #print(tsla.cashFlowsQtr())

    tsla = Symbol('TSLA')
    #print(tsla.analysis())
    #print(tsla.shareholding())
    #tsla.livePriceData().to_csv('okokok.csv')
    #print(tsla.livePriceData())

    print(tsla.options('quotessd'))
    tsla.options('quotes').to_csv('okokok.csv')
