# Create a streamlit app that shows the mongodb data
import streamlit as st
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient

## connect to mongodb
client = MongoClient('mongodb+srv://User:password@cluster0.ragcpnf.mongodb.net/?retryWrites=true&w=majority')

#  Get an existing database named "Marcello_test"
db1 = client.Marcello_test

#   Get a collection named "Seattle_listing"
collection_main = db1.Seattle_listing

# save the documents in a dataframe
df = pd.DataFrame(list(collection_main.find()))

df1 = df.drop(['_id'], axis=1)

########################### create the basic streamlit app #############################

# setting the screen size

st.set_page_config(layout="wide",
                   page_title="Seattle Airbnb Data")
                  

# main title
st.title('Seattle Airbnb Listings MongoDB')

# main text
st.subheader('This app is a Streamlit app that retrieve mongodb data and show it in a dataframe')

st.write('Data: Sample of Seattle listing with Name, Description, Price')

st.dataframe(df1)




