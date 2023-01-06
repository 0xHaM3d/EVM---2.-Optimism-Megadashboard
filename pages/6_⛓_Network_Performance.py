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
st.set_page_config(page_title='Development', page_icon=':bar_chart:', layout='wide')
st.title('⛓ Network Performance')

st.write("")
st.write("")
st.subheader('Network Performance Overall View')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Network Performance Overall View':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/1c55b40e-a8c8-4b84-881f-d0be15fa6a2a/data/latest'
        )


network_performance = gat_data('Network Performance Overall View')
df = network_performance
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(label='**Total Blocks**', value=str(df['Total # of Blocks'].map('{:,.0f}'.format).values[0]))

with c2:
    st.metric(label='**Blocks/Minute**', value=str(df['Blocks/Minute'].map('{:,.0f}'.format).values[0]))

with c3:
    st.metric(label='**Total # of Transactions**',
              value=str(df['Total # of Transactions'].map('{:,.0f}'.format).values[0]))

with c4:
    st.metric(label='**Transactions/Block**', value=str(df['Transactions/Block'].map('{:,.0f}'.format).values[0]))

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(label='**Transactions/Second(TPS)**', value=str(df['Transactions/Second'].map('{:,.0f}'.format).values[0]))

with c2:
    st.metric(label='**Average Difficulty**', value=str(df['Average Diffictuly'].map('{:,.0f}'.format).values[0]))

with c3:
    st.metric(label='**Average Block Gas Fees**',
              value=str(df['Average Block Gas Fees'].map('{:,.0f}'.format).values[0]))

with c4:
    st.metric(label='**Average Block Size**', value=str(df['Average Block Size'].map('{:,.0f}'.format).values[0]))

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(label='**Total # of Users**', value=str(df['Total # of Users'].map('{:,.0f}'.format).values[0]))

with c2:
    st.metric(label='**Users/Day**', value=str(df['Users/Day'].map('{:,.0f}'.format).values[0]))

with c3:
    st.metric(label='**Total Transactions Fee($)**',
              value=str(df['Total Transactions Fee($)'].map('{:,.0f}'.format).values[0]))

with c4:
    st.metric(label='**Average Transaction Fees($)**',
                        value=str(df['Average Transaction Fees($)'].map('{:,.2f}'.format).values[0]))

st.write("")
st.write("")
st.write("")
st.write("")
st.subheader('Transaction Overall View')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Transaction Overall View':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/86bf2a74-99ab-4e9c-9491-d0cc1b0d9ad8/data/latest'
        )


transaction = gat_data('Transaction Overall View')
df = transaction
fig = px.bar(df, x='DATE', y='Tx Count', color='Month Name')
fig.update_layout(title_text='Total # of Transactions per Month')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['Tx Count', 'User Count'])
fig.update_layout(title_text='Transaction & User Traffic per Weekdays')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['Succeed Tx Count', 'Failed Tx Count'])
fig.update_layout(title_text='Weekly # of Succeed vs. Failed Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['Transactions Fee($)'])
fig.update_layout(title_text='Weekly Transaction Fess Volume($)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y=['Cumulative Transactions Fee($)'])
fig.update_layout(title_text='Weekly Cumulative Transactions Fee Volume($)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y=['Success Rate', 'Failed Rate'])
fig.update_layout(title_text='Weekly Rate of Success vs. Fail Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(
         """
The dot graph by color assigned has been used for each individual dot over the past two months. 
The values of the related measurements are shown in the dot graphs, with the hours of the day and days of the 
week indicated by their positions along the x- and y-axes, respectively.
In the dot plots, when the  dot’s color become darker the rate went up and vice versa.
         """
         )


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Success transactions per Minute & Failed Rate':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/85e57c27-19aa-43c5-a60e-165ecd4ccd6b/data/latest'
        )


transaction_heatmap = gat_data('Success transactions per Minute & Failed Rate')
df = transaction_heatmap
c1, c2 = st.columns(2)
with c1:
    fig = px.scatter(df, x='HOUR_OF_DAY', y='DAY_OF_WEEK', color='STPM',
                                 title='Success transactions per minute on hour of day (UTC)')
    fig.update_layout(legend_title=None, xaxis_title='Hour', yaxis_title='Days of Week',
                          coloraxis_colorbar=dict(title='STPM'))
    fig.update_xaxes(categoryorder='category ascending')
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.scatter(df, x='HOUR_OF_DAY', y='DAY_OF_WEEK', color='TFR',
                                 title='Transactions fail rate on hours of day(UTC)')
    fig.update_layout(legend_title=None, xaxis_title='Hour', yaxis_title=None, coloraxis_colorbar=dict(title='TFR'))
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Success Tx/Minute & Failed Rate in Total':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/8e51e7c4-18b4-47e9-b038-b92462b60c1c/data/latest'
        )


success_fail_tx_rate = gat_data('Success Tx/Minute & Failed Rate in Total')
df = success_fail_tx_rate
c1, c2 = st.columns(2)
with c1:
    st.metric(label='**Success Tx/Minute**', value=str(df['Succeed Tx/Minute'].map('{:,.2f}'.format).values[0]))

with c2:
    st.metric(label='**Failed Transaction Rate(%)**', value=str(df['Failed Rate'].map('{:,.2f}'.format).values[0]))


