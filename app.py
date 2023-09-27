import streamlit as st
from inputs import *
from outputs import *
from itertools import cycle

# Set the title of the app
st.title("Squirrel")



if store_inputs():
    show_outputs()
else:
    st.image('/Users/naidilemurali/Documents/squirrelTheApp/images/Squirrel-Logo.png', width =250)
    st.subheader("Your One-Stop Shop for the best deals!")

    filteredImages = ['/Users/naidilemurali/Documents/squirrelTheApp/images/walmart.png', '/Users/naidilemurali/Documents/squirrelTheApp/images/best-buy.png', '/Users/naidilemurali/Documents/squirrelTheApp/images/macys.png', '/Users/naidilemurali/Documents/squirrelTheApp/images/amazon.png', '/Users/naidilemurali/Documents/squirrelTheApp/images/target.png'] # your images here
    #caption = [] # your caption here
    cols = cycle(st.columns(4))
    for idx, filteredImage in enumerate(filteredImages):
        #next(cols).image(filteredImage, width=150, caption=caption[idx])
        next(cols).image(filteredImage, width=150)



