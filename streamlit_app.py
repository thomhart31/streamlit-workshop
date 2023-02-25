import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

file_path='https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt'

dataframe=pandas.read_csv(file_path).set_index('Fruit')

selection = streamlit.multiselect(
    label='Pick some fruits:', 
    options=list(dataframe.index), 
    default=['Apple','Avacado'])

streamlit.dataframe(dataframe.loc[selection])

# adding in a multi select
