import streamlit as st
import json


file_path = "inputs.json"


def get_inputs_from_user():

    with st.sidebar:
        # Input for Product Name
        product_name = st.text_input("Enter Product Name")

        # Input for Credit Cards Owned
        credit_cards_owned = st.selectbox("Select the Number of Credit Cards Owned", [0, 1, 2, 3, 4, 5])

        # Input for Price Range
        price_range = st.slider("Select Price Range", 0, 100, (0, 100))

        search = st.button("Search")

        inputs = {"product_name": product_name, 
                  "credit_cards_owned": credit_cards_owned,
                  "price_range_lower": price_range[0],
                  "price_range_upper": price_range[1],
                  "search": search}
        
        st.write("App by Naidile Murali")
        return inputs
        

def store_inputs():
    inputs = get_inputs_from_user()
    
    

    if inputs["search"]:
        with open(file_path, "w") as json_file:
            json.dump(inputs, json_file)
        return True
    
    return False

def read_inputs():
    loaded_data = {}

    # Open the JSON file in read mode and load its contents into the dictionary
    with open(file_path, "r") as json_file:
        loaded_data = json.load(json_file)

    return loaded_data

