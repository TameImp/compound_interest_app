import streamlit as st
st.title('hello')

import streamlit as st
from calc import monthly_compounding

st.title("Compound Interest Calculator")

initial = st.number_input('Initial investment', min_value = 0, max_value = 100000000000, step= 1)
monthly = st.number_input('Monthly Contribution', min_value = 0, max_value = 100000000000, step= 10)
years = st.number_input('Investment Duration (Years)', min_value = 0, max_value = 100, step= 1)
annual_rate = st.slider('Annual percentage interest', min_value = 0, max_value = 15, step= 1)

sum= round(monthly_compounding(initial, monthly, years, annual_rate),2)

st.markdown(f' After {years} years, you would have £{sum}')

'''
python -m pytest
'''