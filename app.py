import streamlit as st
from inputs import *
from outputs import *

# Set the title of the app
st.title("Squirrel")

if store_inputs():
    show_outputs()
    


