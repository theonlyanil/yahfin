# YahFin 0.3.x (Yahoo Finance Python Wrapper - Unofficial)

The Ultimate Yahoo Finance Python module you'll ever need.
> I was using the other yahoo finance library but it was fetching some of the data through web scrapping which was slow and some of its features didn't work at all.

### Features:
- Live Price Data
- Historical Price Data
- Multi Symbol Data
- Options Data
- Company Profile
- Shareholding Info
- Fundamental Statements
 - Balance Sheets
 - P&L
 - Cash Flows
 - (Yearly and Quarterly upto 4 years/qtrs)

## Quick Guide

### Importing into python file
```
  # one way
  from yahfin import yahfin as yf

  # other way
  import yahfin.yahfin as yf
```

### The Symbol Object
```
  tsla = yf.Symbol('TSLA')
  multiSymbols = yf.Symbol('TSLA, AAPL, MSFT, FB, ZOOM, GOOG')
```

### Quick Examples - Single Symbol
```
  from yahfin import yahfin as yf

  tsla = yf.Symbol('tsla')

  # Get Company Profile -
  tsla.profile()

  # Get Company's Key Managerial Personnel Info
  tsla.profile('kmp')

  # Live Price Data
  tsla.livePriceData()

  # Historical Prices
  tsla.history()  # defaults: period=max, interval=1d
  tsla.history(start='2021-01-01', end='2021-01-05')
  tsla.history(period='1y')
  tsla.history(period='5d', interval='1m')

  #valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
  #valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

  # Options Data
  tsla.options('calls')
  tsla.options('puts')
  tsla.options('dates')
  tsla.options('strikes')
  tsla.options('quotes')

  # Analysis Data
  tsla.analysis()

  # Shareholding Data
  tsla.shareholding()

```

### Multi Symbol Data
```
  from yahfin import yahfin as yf

  multiSymbols = yf.Symbol('TSLA, AAPL, GOOG, FB, RELIANCE.NS')

  # All data at once
  m = multiSymbols.multi()

  # dataPoints of all symbols
  prices = m['regularMarketPrice']
  marketCaps = m['marketCap']

  # Individual Data
  aapl_price = prices['AAPL']

  # Note: The best thing is that it also works with single symbol.

```

### Fundamental Data
```
  from yahfin import yahfin as yf

  tsla = yf.Symbol('tsla')

  # Balance Sheets
  tsla.balanceSheets()
  tsla.balanceSheetsQtr()

  # Profile and Loss Statements
  tsla.incomeStatements()
  tsla.incomeStatementsQtr()

  # Cash Flow Statements
  tsla.cashFlows()
  tsla.cashFlowsQtr()
```

### Requirements
 - Python >= 3.7.x
 - Pandas
