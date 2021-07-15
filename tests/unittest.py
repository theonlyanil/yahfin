# For relative imports to work
import sys

sys.path.append("..")
from yahfin import yahfin as yf #works when yahfin is not installed

us_symbol = yf.Symbol('AAPL')
in_symbol = yf.Symbol('RELIANCE.NS')

# Test Options Data
#opt_us = us_symbol.options()
#opt_in = in_symbol.options()

#print(opt_in)
#print(opt_us)

print(us_symbol.incomeStatements())


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
