"""
    Yahoo Finance API Wrapper
    v0.1

    by Anil Sardiwal
    Started on 8th Nov'20
"""
import pdb
from functions import getIncomeStatementHistory

# Symbol class object
class Symbol:
    def __init__(self, symbol):
        self.symbol = symbol

    def incomeStatements(self):
        return getIncomeStatementHistory(self.symbol)


# Test!
if __name__ == "__main__":
    msft = Symbol('MSFT')
    print(msft.incomeStatements())
