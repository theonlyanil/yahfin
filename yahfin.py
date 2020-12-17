"""
    Yahoo Finance API Wrapper
    v0.1

    by Anil Sardiwal
    Started on 8th Nov'20
"""
import pdb
from functions import getIncomeStatementHistory

class Ticker:
    def __init__(self, symbol):
        self.symbol = symbol

    def getIncomeStatementHistory(self):
        return getIncomeStatementHistory(self.symbol)


if __name__ == "__main__":
    msft = Ticker('MSFT')
    print(msft.getIncomeStatementHistory())
