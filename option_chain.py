import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from scipy.stats import norm
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils.breeze_utils import safe_api_call, get_spot_price, calculate_greeks

def fetch_option_chain(breeze, index_config):
    """Fetch option chain data from Breeze API"""
    if not breeze:
        return pd.DataFrame(), 0

    try:
        # Fetch call options
        ce_data = safe_api_call(
            breeze.get_option_chain_quotes,
            stock_code=index_config["stock_code"],
            exchange_code=index_config["exchange"],
            product_type="options",
            expiry_date=index_config["expiry"],
            right="call"
        )

        # Fetch put options
        pe_data = safe_api_call(
            breeze.get_option_chain_quotes,
            stock_code=index_config["stock_code"],
            exchange_code=index_config["exchange"],
            product_type="options",
            expiry_date=index_config["expiry"],
            right="put"
        )

        # Get spot price
        spot_price = get_spot_price(breeze, index_config["stock_code"])

        if ce_data and pe_data and "Success" in ce_data and "Success" in pe_data:
            ce_list = ce_data["Success"] if isinstance(ce_data["Success"], list) else []
            pe_list = pe_data["Success"] if isinstance(pe_data["Success"], list) else []

            return process_option_data(ce_list, pe_list, spot_price, index_config["expiry"])

        return pd.DataFrame(), spot_price

    except Exception as e:
        st.error(f"Error fetching option chain: {e}")
        return pd.DataFrame(), 0

def process_option_data(ce_data, pe_data, spot_price, expiry_date):
    """Process raw option data into structured DataFrame"""
    # Implementation from original code
    pass

def slice_atm_data(df, spot_price):
    """Slice data around ATM strikes"""
    # Implementation from original code
    pass

def create_oi_chart(df, spot_price, index_name):
    """Create Open Interest chart"""
    # Implementation from original code
    pass

def create_iv_chart(df, spot_price, index_name):
    """Create IV chart"""
    # Implementation from original code
    pass

def get_market_sentiment(df, spot_price):
    """Determine market sentiment based on OI and PCR"""
    # Implementation from original code
    pass

def display_option_chain_tab(breeze, index_config, data):
    """Display option chain for a specific index"""
    if not data['df'].empty:
        expiry_date = index_config["expiry"]
        st.markdown(f"### {index_config['name']} Option Chain (Spot: {data['spot']:,.0f} | Expiry: {expiry_date})")

        # Display dataframe
        # Implementation from original code
        
        # Charts and analysis
        col1, col2 = st.columns(2)
        with col1:
            oi_chart = create_oi_chart(data['df'], data['spot'], index_config['name'])
            st.plotly_chart(oi_chart, use_container_width=True)
        with col2:
            iv_chart = create_iv_chart(data['df'], data['spot'], index_config['name'])
            st.plotly_chart(iv_chart, use_container_width=True)
        
        # Market metrics
        # Implementation from original code
