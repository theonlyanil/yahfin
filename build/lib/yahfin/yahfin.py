"""
    Yahoo Finance API Wrapper
    v0.3.2

    by Anil Sardiwal
    Started on 8th Nov'20
    last modified on 31/12/2020
"""
from .functions import getIncomeStatementHistory,  getAssetProfile,  getLivePriceData,  getMultiSymbolData, getHistoricPrices, getIncomeStatementsQtr, getBalanceSheetYearly, getBalanceSheetQtrly, getCashFlowsYearly, getCashFlowsQtrly, getFinancialAnalysisData, getMajorHolders, getOptionsData

# Symbol class object
class Symbol:
    def __init__(self,  symbol):
        self.symbol = symbol.upper()

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

    def profile(self, kmp=''):
        return getAssetProfile(self.symbol, kmp)

    def livePriceData(self):
        return getLivePriceData(self.symbol)

    def multi(self):
        return getMultiSymbolData(self.symbol)

    def history(self, start=None, end=None, period='max', interval='1d'):
        return getHistoricPrices(self.symbol, start, end, period, interval)

    def options(self, dataType='calls'):
        return getOptionsData(self.symbol, dataType)

# Test!
if __name__ == "__main__":
    tsla = Symbol('TSLA')
    multi = Symbol('TSLA, AAPL, GOOG, AMZN')
    #msft = Symbol('MSFT')
    #print(msft.profile())

    msft = Symbol('RCF.NS')
    #print(msft.history())

    #symbols = Symbol('TSLA, MSFT, AAPL, GOOG')

    #tsla.livePriceData().to_csv('okokok.csv')
    #tsla.options('quotes').to_csv('okokok.csv')

    #tsla.profile('kmp').to_csv("okok.csv")
