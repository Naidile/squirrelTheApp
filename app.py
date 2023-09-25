import streamlit as st
from inputs import *
from outputs import *

# Set the title of the app
st.title("Squirrel")


if store_inputs():
    show_outputs()
else:
    st.subheader("Your One-Stop Shop for the best deals!")
    st.image('/Users/naidilemurali/Documents/squirrelTheApp/images/Squirrel-Logo.png')    


