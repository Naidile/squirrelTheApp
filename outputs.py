import streamlit as st
import json
from inputs import *

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
    col1, col2 = st.columns(2)
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

    #Dummy Output - End


def show_outputs():
    '''orchestrates the output generation and display'''
    inputs = read_inputs()
    outputs = generate_outputs(inputs)
    display_outputs(outputs)

