import streamlit as st
from inputs import get_inputs

# Set the title of the app
st.title("Basic Streamlit Greeting App")

# Add a text input widget to enter your name
user_name = st.text_input("Enter your name", "Your Name")

# Check if a name is provided and display a greeting message
if user_name != "Your Name":
    st.write(f"Hello, {user_name}!")

product_name, credit_cards_owned, price_range = get_inputs()

st.write(f"The Inputs are: product_name: {product_name} and credit_cards_owned: {credit_cards_owned} and price_range: {price_range}")
# You can run this app using the following command in your terminal:
# streamlit run basic_streamlit_app.py
