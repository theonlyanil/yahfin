import streamlit as st
import yahfin as yf

# All features.
singleSymbolInput = yf.Symbol(st.text_input('Single Symbol', 'TSLA'))
singleSymbol = yf.Symbol(singleSymbolInput)

st.title('Company Profile')
profile = singleSymbol.profile()
profile
