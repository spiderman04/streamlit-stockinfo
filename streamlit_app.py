import streamlit as st
import yfinance as yf

st.title('Streamlit Stockinfo App')
st.write('Hello world!')

# get basic ticker information
tickerData = yf.Ticker('NVDA')
tickerDf = tickerData.history(period='6mo', start='2024-01-01', end='2024-11-07')

st.lin_chart(tickerDf.Open)
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
