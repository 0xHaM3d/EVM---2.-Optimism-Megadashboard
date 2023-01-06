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
st.title('🚀 Development')

st.write("")
st.write("")
st.subheader('Deploying Contracts')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Deploying Contracts':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/1bfe61d9-9380-4fa5-bc3e-8c2679e8863e/data/latest'
        )


st.write("")
deploying_contracts = gat_data('Deploying Contracts')
df = deploying_contracts
fig = px.bar(df, x='DATE', y='Contract Count', color='Contract Type')
fig.update_layout(title_text='Weekly New Deployed Contracts')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y='Cumulative Contract Count', color='Contract Type')
fig.update_layout(title_text='Cumulative New Deployed Contracts')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Contracts Traffic':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/902b3c5e-671b-4a69-82ef-8057864ae36a/data/latest'
        )


contracts_traffic = gat_data('Contracts Traffic')
df = contracts_traffic
fig = px.bar(df, x='DATE', y='Contracts Tx Traffic', color='PROJECT_NAME')
fig.update_layout(title_text='Weekly Contracts Tx Traffic')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y='Contracts Usr Traffic', color='PROJECT_NAME')
fig.update_layout(title_text='Contracts User Traffic')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y='Cum Contracts Tx Traffic', color='PROJECT_NAME')
fig.update_layout(title_text='Cumulative Contracts Tx Traffic')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='PROJECT_NAME', y=['Contracts Tx Traffic', 'Contracts Usr Traffic'], log_y=True)
fig.update_layout(title_text='Contracts Total Tx & User Traffic (Log Scale)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Contracts Type Traffic':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/4bdd8473-1561-4539-a8c7-8fa64815283a/data/latest'
        )


contracts_type_traffic = gat_data('Contracts Type Traffic')
df = contracts_type_traffic
fig = px.bar(df, x='DATE', y='Contracts Type Tx Traffic', color='Contract Type')
fig.update_layout(title_text='Weekly Contracts Type Tx Traffic')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y='Contracts Type Usr Traffic', color='Contract Type')
fig.update_layout(title_text='Contracts Type User Traffic')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y='Cum Contracts Type Tx Traffic', color='Contract Type')
fig.update_layout(title_text='Cumulative Contracts Type Tx Traffic')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='Contract Type', y=['Contracts Type Tx Traffic', 'Contracts Type Usr Traffic'], log_y=True)
fig.update_layout(title_text='Contracts Type Total Tx & User Traffic (Log Scale)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)