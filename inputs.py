import streamlit as st

def get_inputs():

    with st.sidebar:
        # Input for Product Name
        product_name = st.text_input("Enter Product Name")

        # Input for Credit Cards Owned
        credit_cards_owned = st.selectbox("Select the Number of Credit Cards Owned", [0, 1, 2, 3, 4, 5])

        # Input for Price Range
        price_range = st.slider("Select Price Range", 0, 100, (0, 100))

    return product_name, credit_cards_owned, price_range


