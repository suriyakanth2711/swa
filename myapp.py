import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
""")

#define the ticker symbol
tickerSymbol = 'MSFT'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1mo', start='2010-5-31', end='2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)

tickerData.recommendations
