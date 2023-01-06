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
st.set_page_config(page_title='Swap & DEXs', page_icon=':bar_chart:', layout='wide')
st.title('📊 Swap & DEXs')


# Style
# with open('style.css')as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


st.write("")
st.write("")
st.subheader('DEXs Overall View')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'DEXs Overall View':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/e2e6136e-461f-4705-bcfb-516baf751c72/data/latest'
        )


st.write("")
dex_overall_view = gat_data('DEXs Overall View')
df = dex_overall_view
fig = px.bar(df, x='DEX', y=['Swaps Tx Cnt', 'Swappers'])
fig.update_layout(title_text='DEXs Swaps Tx & Swapper Count in Total')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.subheader('DEXs Swaps Metric Over Time')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Swaps Metric Over Time':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/e94c465d-f331-4fd7-b5c8-840df633b238/data/latest'
        )


dex_over_time = gat_data('Swaps Metric Over Time')
df = dex_over_time
fig = px.bar(df, x='DATE', y='Swaps Tx Cnt', color='DEX')
fig.update_layout(title_text='Weekly Swaps Tx Count by DEXs')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y='Cumulative Swaps Tx Cnt', color='DEX')
fig.update_layout(title_text='Cumulative Swaps Tx Cnt by DEXs')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y='Swappers', color='DEX')
fig.update_layout(title_text='Weekly Swapper Count by DEXs')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.subheader('DEXs New Swappers Over Time')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'New Swappers Over Time':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/cb98f6cc-bb46-47a5-b421-5ff4543adea7/data/latest'
        )


dex_new_usr_over_time = gat_data('New Swappers Over Time')
df = dex_new_usr_over_time
fig = px.bar(df, x='DATE', y='New Swapper', color='DEX')
fig.update_layout(title_text='Weekly New Swapper Count by DEXs')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y=['Cumulative New Swapper'], color='DEX')
fig.update_layout(title_text='Cumulative New Swapper by DEXs')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Weekly Popular Swaps Pairs':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/0bffd4e5-2c24-4a50-8d03-195aebf47a32/data/latest'
        )


popular_pairs = gat_data('Weekly Popular Swaps Pairs')
df = popular_pairs
fig = px.bar(df, x='DATE', y='Swaps Tx Cnt', color='PAIRS')
fig.update_layout(title_text='Weekly Top 5 Popular Pairs by the Most Swaps Tx Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Top 5 Pairs by DEXs':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/01b79334-c12f-4348-9162-d7b812ea096f/data/latest'
        )


top5_pairs_by_dex = gat_data('Top 5 Pairs by DEXs')
df = top5_pairs_by_dex
fig = px.bar(df, x='DEX', y='Swaps Tx Cnt', color='PAIRS', log_y=True)
fig.update_layout(title_text='Top 5 Pairs Based on Tx Count by DEXs (Log Scale)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Weekly Migrate From Uniswap to Velodrome':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/bc9e5e3f-359f-421f-965f-8d7a80d73195/data/latest'
        )


migrate_from_uniswap_to_vlodrome = gat_data('Weekly Migrate From Uniswap to Velodrome')
df = migrate_from_uniswap_to_vlodrome
fig = px.bar(df, x='DATE', y='Migrator')
fig.update_layout(title_text='Weekly Migrator Count From Uniswap to Velodrome')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y='Cumulative Migrator')
fig.update_layout(title_text='Cumulative Migrator Count From Uniswap to Velodrome')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Which DEX top swapper did choose?':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/26007c3f-6b34-43f4-8d1e-578959ba0975/data/latest'
        )


top_dex_by_tx = gat_data('Which DEX top swapper did choose?')
df = top_dex_by_tx
fig = px.bar(df, x='Top DEXs', y='Swaps Tx Cnt', color='RANK')
fig.update_layout(title_text='Which DEX top swapper did choose?')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
