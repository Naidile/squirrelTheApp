import streamlit as st
import json
from inputs import *
import pandas as pd

def generate_outputs(inputs):
    '''Contains the logic to generate outputs using inputs'''

    #Dummy Output - Start
    outputs = inputs
    #Dummy Output - End

    return outputs


def display_outputs(outputs):
    '''Displays the outputs in the desired format'''

    #Dummy Output - Start
    st.write(f"Product Searched: {outputs['product_name']} \n\n Credit Cards Owned: {outputs['credit_cards_owned']} \n\n Price Range: {outputs['price_range_lower']} USD - {outputs['price_range_upper']} USD")
    outputCases(outputs)
    st.write("Credit Card Offers")
    # Create a sample dataframe
    df = pd.DataFrame({
        "Credit Card": ["AMEX", "Chase 1", "Chase Platinum", "Chase REG"],
        "Offer": ["25%", "20%", "15%", "10%"],
        "Promo Code": ["CRED1", "CRED2", "CRED3", "CRED4"]
    })

    # Display the dataframe in the first column
    col1, col2 = st.columns([5, 1]) # Adjust the ratio of the column widths as needed
    col1.dataframe(df)


def show_outputs():
    '''orchestrates the output generation and display'''
    inputs = read_inputs()
    outputs = generate_outputs(inputs)
    display_outputs(outputs)

def outputCases(inputs):
    col1, col2 = st.columns(2)
    if inputs['product_name'] == "Nike Shoes":
        col1.header("Amazon")
        col2.header("Dick's Sporting Goods")

        # Insert product 1 details in the first column
        with col1:
            st.image('/Users/naidilemurali/Documents/squirrelTheApp/images/nike-1.png', use_column_width=True)
            st.write('Price: $55.99')

        # Insert product 2 details in the second column
        with col2:
            st.image('/Users/naidilemurali/Documents/squirrelTheApp/images/nike-2.png', use_column_width=True)
            st.write('Price: $75.99')
    elif inputs['product_name'] == "Sony Headphones":
        col1.header("Amazon")
        col2.header("Best Buy")

        # Insert product 1 details in the first column
        with col1:
            st.image('/Users/naidilemurali/Documents/squirrelTheApp/images/sony-1.png', use_column_width=True)
            st.write('Price: $220.00')

        # Insert product 2 details in the second column
        with col2:
            st.image('/Users/naidilemurali/Documents/squirrelTheApp/images/sony-2.png', use_column_width=True)
            st.write('Price: $235.0')
    else:
        col1.header("Macy's")
        col2.header("Amazon")

        # Insert product 1 details in the first column
        with col1:
            st.image('/Users/naidilemurali/Documents/squirrelTheApp/images/nf-1.png', use_column_width=True)
            st.write('Price: $300.99')

        # Insert product 2 details in the second column
        with col2:
            st.image('/Users/naidilemurali/Documents/squirrelTheApp/images/nf-2.png', use_column_width=True)
            st.write('Price: $315.99')

