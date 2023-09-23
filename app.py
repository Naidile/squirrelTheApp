import streamlit as st
from inputs import *
from outputs import *

# Set the title of the app
st.title("Squirrel")



if store_inputs():
    show_outputs()
    

# You can run this app using the following command in your terminal:
# streamlit run basic_streamlit_app.py
