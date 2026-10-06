import streamlit as st
import pandas as pd
import numpy as np

# Sidebar Navigation Menu
page = st.sidebar.selectbox("Navigation", ["Home", "Crypto Prediction"])

if page == "Home":
    st.title("🏠 Home Page")
    st.write("Khush amdeed! Yeh hamara AI-powered Cryptocurrency Price Prediction project hai.")
    st.info("👈 Side menu (sidebar) se 'Crypto Prediction' select kar ke dashboard dekhein.")
    
    st.subheader("Project ke baray mein:")
    st.write("- Is project mein hum LSTM / Transformers ka istemal kar ke crypto trends predict karte hain.")
    st.write("- Yeh ek interactive web dashboard hai.")

elif page == "Crypto Prediction":
    st.title("🚀 Live Crypto Prediction Dashboard")
    st.write("Yahan aapka live data aur graph show hoga.")

    # Sample graph
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Bitcoin', 'Ethereum', 'Solana']
    )
    st.line_chart(chart_data)
