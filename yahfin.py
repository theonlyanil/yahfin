"""
    Yahoo Finance API Wrapper
    v0.1

    by Anil Sardiwal
    Started on 8th Nov'20
    last modified on 23/12/2020
"""
from functions import getIncomeStatementHistory,  getAssetProfile,  getLivePriceData,  getMultiSymbolData

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

# Test!
if __name__ == "__main__":
    msft = Symbol('TSLA')

    print(msft.livePriceData()['preMarketChange']['raw'])
