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
    st.write(f"The Inputs are: \n\n product_name: {outputs['product_name']} \n\n credit_cards_owned: {outputs['credit_cards_owned']} \n\n price_range_lower: {outputs['price_range_lower']} \n\n price_range_upper: {outputs['price_range_upper']}")
    #Dummy Output - End


def show_outputs():
    '''orchestrates the output generation and display'''
    inputs = read_inputs()
    outputs = generate_outputs(inputs)
    display_outputs(outputs)

