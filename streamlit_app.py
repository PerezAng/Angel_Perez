import streamlit as st
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

st.title('EaR APP')

assets = ['EURUSD=X']

pf_data = pd.DataFrame()
for t in assets:
    pf_data[t] = wb.DataReader(t, data_source='yahoo', start='2015-1-1')['Adj Close']
    
spot_price=pf_data.iloc[-1,0]
spot_price

st.text_input("Introduce tu strike", "Type Here ...") 
  
if(st.button('Submit')): 
    result = name.title() 
    st.success(result) 

strike= float(input("Introduce tu strike "))

st.text_input("Introduce tu exposición", "Type Here ...") 

Exposición_USD = float(input("Introduce la exposición en USD "))

MtM= (Exposición_USD / spot_price) - (Exposición_USD / strike)

st.text('El valor de mercado de la cobertura es EUR: {:,.2f}'.format(MtM))
