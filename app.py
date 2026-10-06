import streamlit as st
import pandas as pd
import numpy as np

st.title("🚀 Crypto & Stock Price Prediction Dashboard")
st.write("Yeh mera AI-powered prediction dashboard hai!")

# Sample graph dikhane ke liye
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Bitcoin', 'Ethereum', 'Solana']
)
st.line_chart(chart_data)
