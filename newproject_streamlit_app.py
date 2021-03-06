import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from matplotlib import pyplot as plt

st.write("""
# Stock Tracker
Enter a **ticker symbol** into the text box to examine a different company.
Use the slider to choose a **time interval** type and the amount of time back from today that will be pulled.
""")

timeChoices = {'Daily':['Days',365,'1d'],'Weekly':['Weeks',104,'1wk'],'Monthly':['Months',60,'1mo'],'Quarterly':['Quarters',48,'3mo']}
timeDf = pd.DataFrame(timeChoices)

# This takes input from the user on which stock ticker that they would like to look at and gives a sliding scale to choose how much data to look back at in months
tickerSymbol = st.text_input("Enter a ticker symbol: ", "TSLA")
timeChoiceSlider = st.select_slider("Choose the type of data you would like to pull: ", options=["Daily", "Weekly", "Monthly", "Quarterly"])
timeSlider = st.slider("Number of Previous %s" % timeDf[timeChoiceSlider][0], min_value=1, max_value = timeDf[timeChoiceSlider][1], value = timeDf[timeChoiceSlider][1], step = 1)

#Input ticker symbol sent to yfinance to get additional data long name of the company is pulled from the ticker
tickerData = yf.Ticker(tickerSymbol)

companyName = tickerData.info['longName']
if timeChoiceSlider == "Daily":
    days = timeSlider
    weeks = 0
    months = 0
elif timeChoiceSlider == "Weekly":
    days = 0
    weeks = timeSlider
    months = 0
elif timeChoiceSlider == "Monthly":
    days = 0
    weeks = 0
    months = timeSlider
else:
    days = 0
    weeks = 0
    months = timeSlider*3

#Pulling date from today for most updated info, and picks a starting date based on slider
endDay = date.today()
startDay = endDay - relativedelta(days=days, weeks = weeks, months = months)

#history data values pulled based on startDay, endDay and the ticker previously chosen.
tickerDf = tickerData.history(start=startDay, end=endDay, interval=timeDf[timeChoiceSlider][2])

st.write("""
Shown are the stock opening, closing, high, low, and volume on the day for %s.
""" % companyName)

#Open Price graphed
st.write("""
### Opening Price
""")
st.line_chart(tickerDf.Open)

#High Price graphed
st.write("""
### High Price
""")
st.line_chart(tickerDf.High)

#Low Price graphed
st.write("""
### Low Price
""")
st.line_chart(tickerDf.Low)

#Closing price graphed
st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)

#Volume graphed
st.write("""
### Volume
""")
st.line_chart(tickerDf.Volume)

# tickerDF_greyed = tickerDf.Close[tickerDf.Date < startDay]

# #Close Price but using MatPlotLib
# fig, ax = plt.subplots()
# plt.plot(tickerDf.Close, color="green")
# plt.plot(tickerDF_greyed, color="blue")
# plt.title("Closing Prices for %s for the past %s months" % (tickerSymbol, monthsSlider))
# plt.xlabel("Closing Price")
# plt.ylabel("Time")
# ax.set_facecolor("gray")
# plt.grid(b=True, which='both',axis='both',c='blue')
# st.pyplot(fig)
# st.plotly_chart(fig)
