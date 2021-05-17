import streamlit as st
import numpy as np
import time

st.title('Yahfin Interactive')


appSelect = st.sidebar.radio(
    "Select Main Feature",
    ("Single Symbol", "Multi Symbol", "Fundamental Data", "Live Sandbox")
)

#Single Symbol
if appSelect == "Single Symbol":
    symbolName = st.text_input('Single Symbol(symbolName)', 'TSLA')
    st.header('Init')
    with st.echo():
        import yahfin.yahfin as yf
        symbol = yf.Symbol(symbolName)

    featureSelect = st.sidebar.radio(
        "Select Sub Feature",
        ('Profile', 'Live Price Data', 'Option Data', 'Historical Data', 'Analysis & Shareholding')
    )
    if featureSelect == 'Profile':
        st.header('Company Profile')
        with st.echo():
            profile = symbol.profile()
            profile

        st.header('KMP')
        with st.echo():
            kmp =  symbol.profile('kmp')
            kmp

    elif featureSelect == 'Live Price Data':
        # Live Price Data
        st.header('Live Price Data')
        with st.echo():
            livePrice = symbol.livePriceData()
            livePrice

    elif featureSelect == 'Option Data':
        st.header(featureSelect)
        optionSelect = st.sidebar.radio(
            "Select Sub Feature",
            ('Calls', 'Puts', 'Dates', 'Strikes', 'Quotes')
        )

        if optionSelect == 'Calls':
            st.subheader('Calls')
            with st.echo():
                calls = symbol.options('calls')
                calls
        elif optionSelect == 'Puts':
            st.subheader('Puts')
            with st.echo():
                puts = symbol.options('puts')
                puts
        elif optionSelect == 'Dates':
            st.subheader('Dates')
            with st.echo():
                dates = symbol.options('dates')
                dates
        elif optionSelect == 'Strikes':
            st.subheader('Strikes')
            with st.echo():
                strikes = symbol.options('strikes')
                strikes
        else:
            st.subheader('Quotes')
            with st.echo():
                quotes = symbol.options('quotes')
                quotes

    elif featureSelect == 'Historical Data':
        st.header(featureSelect)
        with st.echo():
            history = symbol.history()  # defaults: period=max, interval=1d
            history
        st.subheader('Start & End Date')
        with st.echo():
          history = symbol.history(start='2021-01-01', end='2021-01-05')
          history

        st.subheader('Period and Intervals')

        """Valid Periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max"""
        """Valid Intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo"""
        with st.echo():
          history = symbol.history(period='1y', interval='1d')
          history

    elif featureSelect == 'Analysis & Shareholding':
        st.header(featureSelect)
        st.subheader('Analysis')
        with st.echo():
            analysis = symbol.analysis()
            analysis
        st.subheader('Shareholding')
        with st.echo():
            shareholding = symbol.shareholding()
            shareholding
    else:
            pass

elif appSelect == "Fundamental Data":
    st.header(appSelect)
    symbolName = st.text_input('Single Symbol(symbolName)', 'TSLA')
    st.header('Init')
    with st.echo():
        import yahfin.yahfin as yf
        symbol = yf.Symbol(symbolName)

    featureSelect = st.sidebar.radio(
        "Select Sub Feature",
        ('Balance Sheet', 'Cash Flow Statement', 'P&L')
    )

    if featureSelect == 'Balance Sheet':
        st.header(featureSelect)
        with st.echo():
            bsheet = symbol.balanceSheets()
            bsheet
        st.subheader('Quarterly Data')
        with st.echo():
            bsheetQ = symbol.balanceSheetsQtr()
            bsheetQ
    elif featureSelect == 'Cash Flow Statement':
        st.header(featureSelect)
        with st.echo():
            cashFlows = symbol.cashFlows()
            cashFlows
        st.subheader('Quarterly Data')
        with st.echo():
            cashFlowsQtr = symbol.cashFlowsQtr()
            cashFlowsQtr
    else:
        st.header(featureSelect)
        with st.echo():
            incomeStatements = symbol.incomeStatements()
            incomeStatements
        st.subheader('Quarterly Data')
        with st.echo():
            incomeStatementsQtr = symbol.incomeStatementsQtr()
            incomeStatementsQtr

#Multi Symbol
elif appSelect == "Multi Symbol":
    st.header('Multi Symbol Data')
    multiSymbols = st.text_input('Multiple Symbols(multiSymbols)', 'TSLA, FB, GOOG, RELIANCE.NS')
    st.header('Init')
    with st.echo():
        from yahfin import yahfin as yf
        symbols = yf.Symbol(multiSymbols)
    st.subheader('All Data')
    with st.echo():
        multi = symbols.multi()
        multi
    st.subheader('Specific Data')
    with st.echo():
        # dataPoints of all symbols
        data = multi.reindex(columns=['symbol', 'marketCap', 'currency', 'regularMarketPrice'])
        data
else:
    st.header('Live Sandbox')
    st.text('Here you can test whatever feature of yahfin as you want...')
    st.markdown('**Coming soon**')


# Footer
"""Made in 🇮🇳 by Anil Sardiwal"""
