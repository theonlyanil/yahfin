# For relative imports to work
import sys

sys.path.append("..")
from yahfin import yahfin as yf #works when yahfin is not installed
import yfinance as fy
from datetime import datetime

symbol = 'AAPL'

"""
    Testing INIT
"""
start_yf = datetime.now()
a = yf.Symbol(symbol)
end_yf = datetime.now()
print(f"yahfin - Init: {end_yf - start_yf}" )

start_fy = datetime.now()
b = fy.Ticker(symbol)
end_fy = datetime.now()
print(f"yfinance - Init: {end_fy - start_fy}" )


"""
    Testing History
"""
start_yf = datetime.now()
a.history(period='max')
end_yf = datetime.now()
print(f"yahfin - history: {end_yf - start_yf}" )

start_fy = datetime.now()
b.history(period='max')
end_fy = datetime.now()
print(f"yfinance - history: {end_fy - start_fy}" )

"""
    Testing Profile
"""
start_yf = datetime.now()
a.profile()
end_yf = datetime.now()
print(f"yahfin - profile: {end_yf - start_yf}" )

start_fy = datetime.now()
b.info
end_fy = datetime.now()
print(f"yfinance - profile: {end_fy - start_fy}" )

"""
    Testing Balance Sheet
"""
start_yf = datetime.now()
a.balanceSheets()
end_yf = datetime.now()
print(f"yahfin - BS: {end_yf - start_yf}" )

start_fy = datetime.now()
b.balance_sheet
end_fy = datetime.now()
print(f"yfinance - BS: {end_fy - start_fy}" )


"""
    Results as on 15/07/21

    yahfin - Init: 0:00:00.000006
    yfinance - Init: 0:00:00.004649
    yahfin - history: 0:00:00.409379
    yfinance - history: 0:00:00.828099
    yahfin - profile: 0:00:00.299894
    yfinance - profile: 0:00:03.436584
    yahfin - BS: 0:00:00.480830
    yfinance - BS: 0:00:00.000007

"""
