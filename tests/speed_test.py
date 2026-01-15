import sys
import time
import pandas as pd
from datetime import datetime

# Relative import setup
sys.path.append("..")
from yahfin import yahfin as yf
import yfinance as fy

# 15 Diverse Symbols (US & NSE)
SYMBOLS = [
    'AAPL', 'RELIANCE.NS', 'MSFT', 'TCS.NS', 
    'GOOGL', 'INFY.NS', 'TSLA', 'HDFCBANK.NS', 
    'AMZN', 'ICICIBANK.NS', 'META', 'SBIN.NS', 
    'NVDA', 'BHARTIARTL.NS', 'AMD'
]

symbol_idx = 0

def get_next_symbol():
    global symbol_idx
    s = SYMBOLS[symbol_idx]
    symbol_idx += 1
    return s

def benchmark(label, func, *args, **kwargs):
    """ Standardized timing utility with High-Precision Counter """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    duration = end - start
    print(f"{label:25} : {duration:.6f}s")
    return result

print(f"--- 🚀 yahfin vs yfinance Head-to-Head (Symbol Rotation) ---")

# 1. CATEGORY: INIT (Fresh Symbol: AAPL)
s = SYMBOLS[0]
benchmark(f"yahfin - Init ({s})", yf.Symbol, s)
benchmark(f"yfinance - Init ({s})", fy.Ticker, s)

# 2. CATEGORY: HISTORY (Fresh Symbol: RELIANCE.NS)
s = SYMBOLS[1]
a_hist = yf.Symbol(s)
b_hist = fy.Ticker(s)
benchmark(f"yahfin - History ({s})", a_hist.history, period='max')
benchmark(f"yfinance - History ({s})", b_hist.history, period='max')

# 3. CATEGORY: PROFILE (Fresh Symbol: TSLA)
s = SYMBOLS[2]
a_prof = yf.Symbol(s)
b_prof = fy.Ticker(s)
benchmark(f"yahfin - Profile ({s})", a_prof.profile)
benchmark(f"yfinance - Info ({s})", getattr, b_prof, "info")

# 4. CATEGORY: BALANCE SHEET (Fresh Symbol: TCS.NS)
s = SYMBOLS[3]
a_bs = yf.Symbol(s)
b_bs = fy.Ticker(s)
benchmark(f"yahfin - BalSheet ({s})", a_bs.balanceSheets)
# Exposing the cold-start network call for yfinance
benchmark(f"yfinance - BalSheet ({s})", getattr, b_bs, "balance_sheet")
"""
    Results as on 15/01/2026:

    --- 🚀 yahfin vs yfinance Head-to-Head (Symbol Rotation) ---
    yahfin - Init (AAPL)      : 0.000003s
    yfinance - Init (AAPL)    : 0.000345s
    yahfin - History (RELIANCE.NS) : 0.206492s
    yfinance - History (RELIANCE.NS) : 1.567013s
    yahfin - Profile (MSFT)   : 0.289219s
    yfinance - Info (MSFT)    : 0.376009s
    yahfin - BalSheet (TCS.NS) : 0.108522s
    yfinance - BalSheet (TCS.NS) : 0.237472s


"""
