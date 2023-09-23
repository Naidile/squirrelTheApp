# squirrelTheApp

This is a Web App for an Online Shopping Aggregator.

## Inputs:

1. A text box to enter Product name
2. A dropdown menu with 2 credit card names: Amex, Chase (Both can be selected)
3. An adjustable price range with min and max

### Example: User enters:
1. Product name: nike shoes AND
2. Selects Amex and Chase as the credit cards owned AND
3. Selects $50-$70 as the price range 

Then hits the Search button

## Output:
User is shown a product comparison page with nike shoe offers from 2 stores side by side
Followed by credit card offers pertaining to the cards he has chosen

They can select one of the 2 products AND proceed to checkout.

## To run: 
You can run this app using the following command in your terminal:
`streamlit run app.py --server.headless=true`