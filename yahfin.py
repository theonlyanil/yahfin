"""
    Yahoo Finance API Wrapper
    v0.1

    by Anil Sardiwal
    Started on 8th Nov'20
    last modified on 23/12/2020
"""
from functions import getIncomeStatementHistory,  getAssetProfile,  getLivePriceData,  getMultiSymbolData, getHistoricPrices

# Symbol class object
class Symbol:
    def __init__(self,  symbol):
        self.symbol = symbol

    def incomeStatements(self):
        return getIncomeStatementHistory(self.symbol)

    def profile(self):
        return getAssetProfile(self.symbol)

    def livePriceData(self):
        return getLivePriceData(self.symbol)

    def multi(self):
        return getMultiSymbolData(self.symbol)

class History:
    def __init__(self, symbol, start, end, period):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.period = period

    def prices(self):
        return getHistoricPrices(self.symbol, self.start, self.end, self.period)

# Test!
if __name__ == "__main__":
    msft = History('TSLA', '2020-12-01', '2020-12-02', '1d')

    print(msft.prices())
