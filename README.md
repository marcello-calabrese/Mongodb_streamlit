# Database for Datascientist? Easy and quick solution with MongoDB and Pandas+Streamlit (Part 2)

## Introduction

In the previous article, we have seen how to create a database with MongoDB and how to use it with Pandas. In this article, we will see how to use MongoDB with Streamlit and deploy as a web application.

## Streamlit

[Streamlit](https://streamlit.io/) is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. It is a great tool for data scientists and machine learning engineers to create web applications for their projects. It is very easy to use and has a lot of features. It is also very easy to deploy on Heroku.

The nice thing about Streamlit is that it is very easy to use. You can create a web application with just a few lines of code, no HTML, CSS, or JavaScript required.

And the other nice thing is that you can deploy for free on different platforms like Heroku, AWS, and Google Cloud.

![streamlit_intro](https://user-images.githubusercontent.com/74682725/198874217-52c94378-a8d3-46f9-9562-602368c5b5c7.JPG)

## Installation

To install Streamlit, is very easy, it can be done with pip in your dedicated python environment.

```
pip install streamlit
```

After installing Streamlit, to verify that it is installed correctly, you can run the following command in your terminal.

```
streamlit hello
```

This will open a new tab in your browser with a simple web application as shown in the image below.

![streanlithello](https://user-images.githubusercontent.com/74682725/198874238-e5f848f8-7625-4228-aed3-7f3b45b91259.jpeg)

## Create a basic web application with Streamlit and plug it to MongoDB

In the following section we will create a basic web application with Streamlit that retrieves data from MongoDB and displays it in a table.
The app is very basic and it is just to show how to use Streamlit with MongoDB, so don't expect a lot of features, it will only display the data in a table built with st.dataframe() :-). If you are interested in more advanced features of Streamlit, write a comment below and I will write another article about it :-).

## The dataset: Seattle Airbnb Listings

The dataset I used for this example is the Seattle Airbnb Listings dataset. It contains information about the listings of Airbnb in Seattle. The dataset is available on [Kaggle](https://www.kaggle.com/airbnb/seattle/data).

I will not explain in details here how I loaded on my MongoDB database, but for this exercise you can upload the csv file using the MongoDB Compass GUI, you can find the documentation [here](https://docs.mongodb.com/compass/master/import-export/). It is quite easy to do. You can also do it programmatically, using the pymongo Python API for MongoDB.
See below the screenshots of how easy is to add a csv file into your database using MongoDB Compass.

1. Add the dataset to MongoDB Compass

![Mongocompass](https://user-images.githubusercontent.com/74682725/198874257-83cd275b-cc9e-4c11-9744-b587bc508558.JPG)

2. Import CSV and JSON files into MongoDB Compass

![Mongocompass_importfile](https://user-images.githubusercontent.com/74682725/198874274-b91e2ae1-3180-48b7-a97c-c291dc94c403.JPG)

3. Dataset visualization as collection in MongoDB Compass

![Mongocompass_seattle](https://user-images.githubusercontent.com/74682725/198874292-d534f3cd-27f3-4ade-ab88-09e55b5b716e.JPG)

## The code: let's build our simple web application

Now that we have our dataset in MongoDB, we can start building our web application.
It is a python file so we need to save it with the .py extension. I called it app_st.py(not very creative, I know :-)).

1. Import the libraries

```python
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
import streamlit as st
```

2. Connect to MongoDB

After importing the libraries, we need to connect to our MongoDB database. We can do it using the MongoClient() function from the pymongo library. We need to specify the host and the port of our MongoDB database. In my case, I am using the default host and port, so I don't need to specify them. I masked my user name and password of course :-).

```python
## connect to mongodb
client = MongoClient('mongodb+srv://User:mypsw@cluster0.ragcpnf.mongodb.net/?retryWrites=true&w=majority')
```

3. Get the database and the collection

After connecting to MongoDB, we need to specify the database and the collection we want to use. In my case, I am using the database "Marcello_test"(my name...) and the collection "Seattle_listing".

```python
#  Get an existing database named "Marcello_test"
db1 = client.Marcello_test

#   Get a collection named "Seattle_listing"
collection_main = db1.Seattle_listing
```

4. Parsing the documents from MongoDB to Pandas

Now that we have the collection, we can parse the documents to Pandas. We can do it using the find() function from the pymongo library. We can also specify the fields we want to retrieve from the collection. In my case, I am retrieving all the fields.

```python
# save the documents in a dataframe
df = pd.DataFrame(list(collection_main.find()))

df1 = df.drop(['_id'], axis=1) # drop the _id field, not needed, it is created automatically by MongoDB
```

5. Create the web application with Streamlit

Now that we have the data in a Pandas dataframe, we can create our web application with Streamlit. We can use the st.dataframe() function to display the data in a table. We can also use the st.title() function to add a title to our web application.

```python
# setting the screen size

st.set_page_config(layout="wide",
                   page_title="Seattle Airbnb Data")
                  

# main title
st.title('Seattle Airbnb Listings MongoDB') # title of the web application

# main text
st.subheader('This app is a Streamlit app that retrieve mongodb data and show it in a dataframe') # subheader

st.write('Data: Sample of Seattle listing with Name, Description, Price') # write text and description

st.dataframe(df1) # display the dataframe in a table
```

All done!! with just a few lines of code we have created a web application that retrieves data from MongoDB and displays it in a table.

6. Run the web application locally with Streamlit

Now that the code is ready, we can run the web application locally with Streamlit. We can do it using the following command in the terminal.

```
streamlit run app_st.py
```

This code will open a new tab in your browser with the web application as shown in the image below, using a local host.

Et voi la! We have created a web application that retrieves data from MongoDB and displays it in a table.


https://user-images.githubusercontent.com/74682725/198874351-64b157c8-2e00-4a8f-846b-a3be8058940c.mp4



