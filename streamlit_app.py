import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cl
import datetime

#title

st.markdown('Stock Price WebApp')
st.write('by Raul Hoyos')

#menu

st.sidebar.subheader('Date Range')
start_date = st.sidebar.date_input('start date', datetime.date(2019,1,1))
end_date = st.sidebar.date_input('end date', datetime.date(2021,1,31))

#tickerdata
ticker_list = pd.read_csv("s&p500.txt")
tickerSymbol = st.sidebar.selectbox('Stock Ticker', ticker_list)
tickerData = yf.Ticker(tickerSymbol)
tickerDataHistory = tickerData.history(period='1d', start = start_date, end = end_date) #make period dynamic

#info
st.header('**INFO**')
st.markdown(tickerData.info['longName'])
st.markdown(tickerData.info['sector'])
st.write(tickerDataHistory)

#graph

st.header('Graphs')
qf = cl.QuantFig(tickerDataHistory, title = 'first graph', legend = 'top', name = 'GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)
