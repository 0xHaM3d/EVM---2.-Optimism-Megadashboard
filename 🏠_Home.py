# Libraries
import streamlit as st
# from PIL import Image

# Layout
st.set_page_config(page_title='Welcome to Optimism 2022 Recap', page_icon=':bar_chart:', layout='wide')
st.write("## Welcome to Optimism 2022 Recap! ✨🔴_🔴✨")

# Content
# Content
# c1 = st.columns(1)
# c1.image(Image.open('Images/Optimism.png'))
# image = Image.open('optimism.png')
# st.image(image, caption='Sunrise by the mountains')

# image = Image.open('Optimism.png')
# st.image(image, caption='Sunrise by the mountains')

st.write("")
st.write("")
st.write("")
st.write("")

st.write(
    """
    The crypto industry continues to progress and its development has never stopped. Contributors
    of each blockchain keep developing each segment of the industry and the whole crypto ecosystem.
    This tool is designed to allow viewers to recap the 2022 Optimisms' ecosystem, 
    Optimism is a layer 2 scaling solution chain for Ethereum. It functions on top of the Ethereum mainnet (layer 1),
    while transactions take place on Optimism. It increases the speed of transactions and decreases the fees of 
    transactions using Ethereum.
    This building dashboard keeps track of the popularity and performance of Optimism. It also presents an overview of 
    the OP token.
    The Ecosystem section presents analytics for the two most popular NFT marketplace and Defi protocol on Optimism; 
    such as: Velodrome and Quixotic.
    This tool is designed and structured in multiple **Pages** that are accessible using the sidebar.
    Each of these Pages addresses a different category of the ecosystem. Within each category
    (Airdrop $OP Token, Inflows & Outflows, Swaps, NFTs, etc.) you are able to filter your desired class to
    narrow/expand the 2022 recap. 

    All values for amounts, prices, and volumes are in **U.S. dollars** and the time frequency of the
    analysis was limited to the over **2022 year by week**.
    """
)

st.subheader('Methodology')
st.write(
    """
    The data for this Optimism 2022 recap were selected from the [**Flipside Crypto**](https://flipsidecrypto.xyz/)
    data platform by using its **REST API**. These queries are currently set to **re-run every 24 hours** to cover the 
    latest data and are imported as a JSON file directly to each page. The codes for this tool are saved and accessible
     in its [**GitHub Repository**](https://github.com/0xHaM3d/Optimism-2022-Recap/tree/master).

    As the queries are updated on a daily basis to cover the most recent data, there is a chance
    that viewers encounter inconsistent data through the app. Due to the heavy computational power required to execute
    the queries, and also the size of the raw data being too large, it may take a few minutes to reload the data,
    or by downloading the data and loading it from the repository itself. Therefore, the REST API was selected as the
    proper form of loading data for the time being.

    Besides the codes and queries mentioned above, the following dashboards created using Flipside Crypto were used
    as the core references in developing the current tool:
    - [$OP Airdrop (Redux)](https://app.flipsidecrypto.com/dashboard/op-airdrop-redux-WDQW-m)
    - [Inflows and Outflows (redux)](https://app.flipsidecrypto.com/dashboard/inflows-and-outflows-redux-L8u-is)
    - [Secondary NFT Market Mega Dashboard](https://app.flipsidecrypto.com/dashboard/secondary-nft-market-mega-dashboard-7APV8c)
    - [Optimism DEXs (redux)](https://app.flipsidecrypto.com/dashboard/optimism-de-xs-copy-0QBjhj)
    """
)

st.subheader('Future Works')
st.write(
    """
    This tool is a work in progress and will continue to be developed moving forward. Adding other subjects,
    more KPIs and metrics, optimizing the code in general, enhancing the UI/UX of the tool, and more importantly,
    improving the data pipeline by utilizing [**Flipside ShroomDK**](https://sdk.flipsidecrypto.xyz/shroomdk) are
    among the top priorities for the development of this app. Feel free to share your feedback, suggestions, and
    also critics with me.
    """
)

c1, c2 = st.columns(2)
with c1:
    st.info('**Developer/Analyst: [@0xHaM☰d](https://twitter.com/0xham3d_eth)**', icon="💻")
with c2:
    st.info('**Data: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")