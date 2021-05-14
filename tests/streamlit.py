import streamlit as st
import yahfin.yahfin as yf

st.title('Yahfin Interactive')
# All features.
singleSymbol = yf.Symbol(st.text_input('Single Symbol', 'TSLA'))

#Profile
st.subheader('Company Profile')
with st.echo():
    tsla = yf.Symbol("TSLA")
    tsla.profile()
profile = singleSymbol.profile()
profile

#KMP
st.subheader('KMP')
with st.echo():
    tsla.profile('kmp')
kmp =  tsla.profile('kmp')
kmp

# Live Price Data
st.subheader('Live Price Data')
with st.echo():
    tsla.livePriceData()

livePrice = tsla.livePriceData()
livePrice
