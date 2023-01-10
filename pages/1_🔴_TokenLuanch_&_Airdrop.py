# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import numpy as np
import altair as alt
from pandas.core.reshape.reshape import unstack

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='$OP Token - Airdrop Overview', page_icon=':bar_chart:', layout='wide')
st.title('🔴 Token Launch & Airdrop')

# Style
# with open('style.css') as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("###### Airdrop OP Token Overview...")


# Data Sources
# @st.cache(ttl=600)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Airdrop Token Claiming Overview':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/af0841da-b849-4293-87c4-a79b982ea46e/data/latest'
        )


airdrop_claim_overview = gat_data('Airdrop Token Claiming Overview')
st.dataframe(airdrop_claim_overview, use_container_width=True)


# Claim Over Time....


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Claim Tokens Over Time':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/e8a235bd-0b3a-4d01-b533-97011852913d/data/latest'
        )


st.write("")
st.write("")
airdrop_claim_daily = gat_data('Claim Tokens Over Time')
df = airdrop_claim_daily
fig = px.bar(df, x='DATE', y=['CLAIMS', 'CLAIMERS'])
fig.update_layout(title_text='Airdrop OP Token Claims & Claimer Count Over Time')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("")
st.write("")

fig = px.bar(df, x='DATE', y=['CLAIMED_OP', 'PENDING_OP'])
fig.update_layout(title_text='Airdrop OP Token Claimed & Pended Volume Over Time')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("")
st.write("")

fig = px.area(df, x='DATE', y=['CUM_CLAIMED_OP', 'CUM_CLAIMS'])
fig.update_layout(title_text='Airdrop OP Token Cumulative Claimed Volume & Claims Count Over Time')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("")
st.write("")
st.write("###### Airdrop OP Token Holding Overview...")


# Data Sources
# @st.cache(ttl=600)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Token Holding Overview':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/c3086428-ac35-4bbb-8c1b-bfe747f2ea5d/data/latest'
        )


# Claim Over Time....
airdrop_holding_overview = gat_data('Token Holding Overview')
st.dataframe(airdrop_holding_overview, use_container_width=True)

st.write("")
st.write("")
st.write("###### Airdrop OP Token Delegation Overview...")


# Data Sources
# @st.cache(ttl=600)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Token Delegation Overview':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/5dbf9aeb-ff38-40d4-9305-76849d936259/data/latest'
        )


# Claim Over Time....

airdrop_delegation_overview = gat_data('Token Delegation Overview')
st.dataframe(airdrop_delegation_overview, use_container_width=True)


# Top 10 Delegate Destinations by Delegate Count....

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Top 10 Delegate Destinations by Delegator':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/ddac16ee-a66f-47bc-b032-c1955518b404/data/latest'
        )


st.write("")
st.write("")
airdrop_top10_delegate_count = gat_data('Top 10 Delegate Destinations by Delegator')
df = airdrop_top10_delegate_count
fig = px.bar(df, x='Destination Name', y='Number of Delegator', color='Destination Name')
fig.update_layout(title_text='Top 10 Delegate Destinations by # of Delegate')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Top 10 Delegate Destinations by Delegate Volume....

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Top 10 Delegate Destinations by Volume':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/00457e10-f65d-4cc5-95da-e7c1adf8206f/data/latest'
        )


st.write("")
st.write("")
airdrop_top10_delegate_volume = gat_data('Top 10 Delegate Destinations by Volume')
df = airdrop_top10_delegate_volume
fig = px.bar(df, x='Destination Name', y='Number of Delegator', color='Destination Name')
fig.update_layout(title_text='Top 10 Delegate Destinations by Volume of Delegate')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# $OP, BTC & ETH Daily Average Price ....


@st.cache(ttl=10000)
def gat_data(query):
    if query == '$OP Daily Average Price':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/3f6ae6bb-ec25-42d7-8faf-bdb2513f084b/data/latest'
        )


st.write("")
st.write("")
average_price_daily = gat_data('$OP Daily Average Price')
df = average_price_daily
base = alt.Chart(df).encode(x=alt.X('DATE', axis=alt.Axis(labelAngle=325)))
line = base.mark_line(color='orange').encode(y=alt.Y('BTC_PRICE', axis=alt.Axis(grid=True)))
bar = base.mark_line(color='purple',opacity=0.5).encode(y='OP_PRICE')
st.altair_chart(((bar + line).resolve_scale(y='independent').properties(title='Daily $OP vs $BTC price evolution')),
                use_container_width=True, theme=theme_plotly)
st.write("")
st.write("")
base = alt.Chart(df).encode(x=alt.X('DATE', axis=alt.Axis(labelAngle=325)))
line = base.mark_line(color='orange').encode(y=alt.Y('ETH_PRICE', axis=alt.Axis(grid=True)))
bar = base.mark_line(color='purple',opacity=0.5).encode(y='OP_PRICE')
st.altair_chart(((bar + line).resolve_scale(y='independent').properties(title='Daily $OP vs $ETH price evolution')),
                use_container_width=True, theme=theme_plotly)
