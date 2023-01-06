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
st.set_page_config(page_title='Inflow & Outflow', page_icon=':bar_chart:', layout='wide')
st.title('💸 Inflow & Outflow')

# ETH => OP Transferring Overview....
st.write("")
st.write("")
st.subheader('PartI: ETH => OP Transferring Overview')

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'ETH => OP Over Time':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/35d10455-d567-440b-8b82-d47278f23a85/data/latest'
        )

st.write("")
st.write("")
transfer_eth_op = gat_data('ETH => OP Over Time')
df=(transfer_eth_op)
fig = px.bar(df, x='DATE', y='TOTAL_TX', color='SYMBOL')
fig.update_layout(title_text='Weekly Transfer Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("")
st.write("")
transfer_eth_op = gat_data('ETH => OP Over Time')
df = transfer_eth_op
fig = px.bar(df, x='DATE', y='TOTAL_USER', color='SYMBOL')
fig.update_layout(title_text='Weekly Transferring User Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write("")
st.write("")
transfer_eth_op = gat_data('ETH => OP Over Time')
df = transfer_eth_op
fig = px.bar(df, x='DATE', y='VOLUME_USD', color='SYMBOL')
fig.update_layout(title_text='Weekly Transferred Volume($)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# ETH => OP Transferring In Total....
st.write("")
st.subheader('Overall view')

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'ETH => OP in Total':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/d3028042-4a9c-4bd5-b458-5e75403498e6/data/latest'
        )

transfer_eth_op_total = gat_data('ETH => OP in Total')
df = transfer_eth_op_total
c1, c2 = st.columns(2)
with c1:
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['SYMBOL'], y=df['TOTAL_TX'], name='Transactions'), secondary_y=False)
    fig.add_trace(go.Bar(x=df['SYMBOL'], y=df['TOTAL_USER'], name='Users'), secondary_y=False)
    fig.update_layout(title_text='Total Tx & User Count by Token')
    fig.update_yaxes(title_text='Transactions', secondary_y=False)
    fig.update_yaxes(title_text='Users', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['SYMBOL'], y=df['VOLUME_USD'], name='Volume($)'))
    fig.update_layout(title_text='Total Transferred Volume($) by Token')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("")
c1, c2 = st.columns(2)
with c1:
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['BRIDGE'], y=df['TOTAL_TX'], name='Transactions'), secondary_y=False)
    fig.add_trace(go.Bar(x=df['BRIDGE'], y=df['TOTAL_USER'], name='Users'), secondary_y=False)
    fig.update_layout(title_text='Total Tx & User Count by Bridge')
    fig.update_yaxes(title_text='Transactions', secondary_y=False)
    fig.update_yaxes(title_text='Users', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['BRIDGE'], y=df['VOLUME_USD'], name='Volume($)'))
    fig.update_layout(title_text='Total Transferred Volume($) by Bridge')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# #####################################
# #####################################
# #####################################
# #####################################

# OP => ETH Transferring Overview....
st.write("")
st.write("")
st.subheader('PartII: OP => ETH Transferring Overview')

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'OP => ETH Over Time':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/50d26cb7-d52a-4a2d-8eba-7630e5816b63/data/latest'
        )


st.write("")
transfer_op_eth = gat_data('OP => ETH Over Time')
df = transfer_op_eth
fig = px.bar(df, x='DATE', y='TOTAL_TX', color='SYMBOL')
fig.update_layout(title_text='Weekly Transfer Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write("")
transfer_op_eth = gat_data('OP => ETH Over Time')
df = transfer_op_eth
fig = px.bar(df, x='DATE', y='TOTAL_USER', color='SYMBOL')
fig.update_layout(title_text='Weekly Transferring User Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write("")
transfer_op_eth = gat_data('OP => ETH Over Time')
df = transfer_op_eth
fig = px.bar(df, x='DATE', y='VOLUME_USD', color='SYMBOL')
fig.update_layout(title_text='Weekly Transferred Volume($)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# OP => ETH Transferring In Total....
st.write("")
st.subheader('Overall view')

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'OP => ETH in Total':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/2ab0d727-d804-41bd-8c1e-a0016c3870df/data/latest'
        )

transfer_op_eth_total = gat_data('OP => ETH in Total')
df = transfer_op_eth_total
c1, c2 = st.columns(2)
with c1:
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['SYMBOL'], y=df['TOTAL_TX'], name='Transactions'), secondary_y=False)
    fig.add_trace(go.Bar(x=df['SYMBOL'], y=df['TOTAL_USER'], name='Users'), secondary_y=False)
    fig.update_layout(title_text='Total Tx & User Count by Token')
    fig.update_yaxes(title_text='Transactions', secondary_y=False)
    fig.update_yaxes(title_text='Users', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['SYMBOL'], y=df['VOLUME_USD'], name='Volume($)'))
    fig.update_layout(title_text='Total Transferred Volume($) by Token')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)
with c1:
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['BRIDGE'], y=df['TOTAL_TX'], name='Transactions'), secondary_y=False)
    fig.add_trace(go.Bar(x=df['BRIDGE'], y=df['TOTAL_USER'], name='Users'), secondary_y=False)
    fig.update_layout(title_text='Total Tx & User Count by Bridge')
    fig.update_yaxes(title_text='Transactions', secondary_y=False)
    fig.update_yaxes(title_text='Users', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df['BRIDGE'], y=df['VOLUME_USD'], name='Volume($)'))
    fig.update_layout(title_text='Total Transferred Volume($) by Bridge')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)