# Libraries
import streamlit as st


# [theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"


# Layout
st.set_page_config(page_title='Definitions & Data Transparency', page_icon=':bar_chart:', layout='wide')
st.write("#### 📜 Definitions & Data Transparency")


st.write("")
st.write("")
st.write("")
st.write("")

st.write(
    """
    The main data source is [**Flipside Crypto**](https://flipsidecrypto.xyz/). They offer free access to blockchain 
    data across a variety of different blockchains. 
    The SQL queries to extract the data to display are written by me and are automatically updated every
    24 hours. They all are open-sourced and feel free to reach out if you need access to anything in
    particular. 
    """
)
st.write(
    """
    ### How are daily transactions counted?    
    To calculate daily transactions on Optimism (as well as other chains transactions), 
    all transactions that interact with on protocols are included. 
    
    The users that have had as the first transactions called as **New Users**.
    All addresses that execute a transaction interacting on Optimisms' ecosystem
    for the first time have been counted as **New Users** number.
    
    ### Popularity assessed by:
    The volume of active users on Optimism per week over past year
    The adoption by new users per week
    
    ### How is the users growth(Cumulative) calculated?    
    On a given week, all addresses that execute a transaction interacting for the first time have been counted 
    towards the weekly New Users number. 
    The cumulative curve is simply a progressive sum of the new weekly users.  
    
    ### Performance assessed by:
    The success rate of transactions in the Optimism
    The average STPM(Succeed Transactions per Minute) per week
    The average FTR(Failed Transactions Rate) per week
    The average blocks size
    The average transactions fee($)
    """

)

st.write("")
st.write("")
st.write("")
st.write("")

st.subheader('Queries')
st.write(
    """
    1. https://app.flipsidecrypto.com/velocity/queries/1c55b40e-a8c8-4b84-881f-d0be15fa6a2a
    2. https://app.flipsidecrypto.com/velocity/queries/86bf2a74-99ab-4e9c-9491-d0cc1b0d9ad8
    3. https://app.flipsidecrypto.com/velocity/queries/8e51e7c4-18b4-47e9-b038-b92462b60c1c
    4. https://app.flipsidecrypto.com/velocity/queries/85e57c27-19aa-43c5-a60e-165ecd4ccd6b
    5. https://app.flipsidecrypto.com/velocity/queries/4ae2751b-1174-4b59-9ee9-e51671ec37a0
    6. https://app.flipsidecrypto.com/velocity/queries/1bfe61d9-9380-4fa5-bc3e-8c2679e8863e
    7. https://app.flipsidecrypto.com/velocity/queries/902b3c5e-671b-4a69-82ef-8057864ae36a
    8. https://app.flipsidecrypto.com/velocity/queries/4bdd8473-1561-4539-a8c7-8fa64815283a
    9. https://app.flipsidecrypto.com/velocity/queries/cb98f6cc-bb46-47a5-b421-5ff4543adea7
    10. https://app.flipsidecrypto.com/velocity/queries/0bffd4e5-2c24-4a50-8d03-195aebf47a32
    11. https://app.flipsidecrypto.com/velocity/queries/634ef56e-c0bb-4f60-bbe5-17492f3a7891
    12. https://app.flipsidecrypto.com/velocity/queries/81dbb8c1-0cb1-46d4-b1e2-bbb393944e81
    13. https://app.flipsidecrypto.com/velocity/queries/2ab0d727-d804-41bd-8c1e-a0016c3870df
    14. https://app.flipsidecrypto.com/velocity/queries/35d10455-d567-440b-8b82-d47278f23a85
    15. https://app.flipsidecrypto.com/velocity/queries/e8a235bd-0b3a-4d01-b533-97011852913d
    """
)

st.write("")
st.write("")
st.write("")
st.write("")


fig = st.write(
    """
                     ### Made with :red[❤] & Honor
    """
)