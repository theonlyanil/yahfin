# For relative imports to work
import sys

sys.path.append("..")
from yahfin import yahfin as yf #works when yahfin is not installed

us_symbol = yf.Symbol('AAPL')
in_symbol = yf.Symbol('RELIANCE.NS')

"""
    Single Symbol Testing
"""
# Get Company Profile
print(us_symbol.profile())

"""
# Get Company's Key Managerial Personnel Info
us_symbol.profile('kmp')

# Live Price Data
us_symbol.livePriceData()

# Historical Prices
us_symbol.history()

# Options Data
us_symbol.options('calls')
us_symbol.options('puts')
us_symbol.options('dates')
us_symbol.options('strikes')
us_symbol.options('quotes')

# Analysis Data
us_symbol.analysis()

# Shareholding Data
us_symbol.shareholding()
"""
