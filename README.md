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
  tsla.
```
