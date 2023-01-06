# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import numpy as np
from pandas.core.reshape.reshape import unstack

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Secondary NFT Market', page_icon=':bar_chart:', layout='wide')
st.title('🎨 Secondary NFT Market')

# ETH => OP Transferring Overview....
st.write("")
st.write("")
st.subheader('Secondary NFT Market')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Secondary NFT Market':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/81dbb8c1-0cb1-46d4-b1e2-bbb393944e81/data/latest'
        )


st.write("")
secondary_NFT_market = gat_data('Secondary NFT Market')
df = secondary_NFT_market
fig = px.bar(df, x='DATE', y=['BUYERS', 'SELLERS'])
fig.update_layout(title_text='Weekly Buyer & Seller Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['SALES', 'NFT_SALES_CNT', 'NFT_TOKEN_CNT'])
fig.update_layout(title_text='Weekly Sales Tx, Collection & NFT Token Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['SALES_VOLUME_USD'])
fig.update_layout(title_text='Weekly Sales Volume($)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y=['CUMULATIVE_SALES', 'CUMULATIVE_VOLUME'])
fig.update_layout(title_text='Weekly Cumulative Sales Count & Volume($)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Optimism - NFT - Collection Sales Performance
st.subheader('Optimism NFT Collection Sales Performance')


# Data Sources
# @st.cache(ttl=600)
@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Optimism-NFT-Collection Sales Performance':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/634ef56e-c0bb-4f60-bbe5-17492f3a7891/data/latest'
        )


optimism_NFT_collection_performance = gat_data('Optimism-NFT-Collection Sales Performance')
st.write("")
df = optimism_NFT_collection_performance
fig = px.bar(df, x='Project', y=['7D 🢒🢐'], color='Project')
fig.update_layout(title_text='7D Sales Volume($)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='Project', y=['7D 🢒🢐 %'], color='Project')
fig.update_layout(title_text='7D Sales Volume($) % Change')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Project'], y=df['7D Buyers'], name='7D Buyers'), secondary_y=False)
fig.add_trace(go.Bar(x=df['Project'], y=df['7D Tx'], name='7D Transactions'), secondary_y=False)
fig.update_layout(title_text='7D Buyer & Sales Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.dataframe(df, use_container_width=True)
