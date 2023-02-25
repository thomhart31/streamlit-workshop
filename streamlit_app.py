import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

file_path='https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt'

dataframe=pandas.read_csv(file_path).set_index('Fruit')

streamlit.multiselect('Pick some fruits:', list(dataframe.index))

streamlit.dataframe(dataframe)

# adding in a multi select
