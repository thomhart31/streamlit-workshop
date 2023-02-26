import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('Streamlit Workshop Example')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

file_path='https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt'

dataframe=pandas.read_csv(file_path).set_index('Fruit')

selection = streamlit.multiselect(
    label='Pick some fruits:', 
    options=list(dataframe.index), 
    default=['Apple','Avocado'])

streamlit.dataframe(dataframe.loc[selection])

streamlit.header('FruityVice Response')

choice = streamlit.text_input(label='Fruit: ',value='Kiwi')
streamlit.write('User entered: ',choice)

response = requests.get(f'https://fruityvice.com/api/fruit/{choice}')
streamlit.text(response.json())

dataframe_fruityvice = pandas.json_normalize(response.json())
streamlit.dataframe(dataframe_fruityvice)

# connecting to snowflake
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# my_cur.execute("select * from fruit_load_list")
# # my_data_row = my_cur.fetchone()
# my_data_row = my_cur.fetchall()
# streamlit.text("The fruit load list contains:")
# streamlit.dataframe(my_data_row)

# choice2 = streamlit.text_input(label='What would you like to add:')
# streamlit.text(f'Thanks for adding: {choice2}')

# my_cure.execute(f"insert into fruit_load_list values ('{choice2}')")

if streamlit.button('Get Fruit Load List'):    
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_cur.execute("select * from fruit_load_list")
    my_data_row = my_cur.fetchall()
    my_cnx.close()
    streamlit.dataframe(my_data_row)

choice2 = streamlit.text_input(label='What would you like to add:')
if streamlit.button('Add Fruit to List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_cur.execute(f"insert into fruit_load_list values ('{choice2}')")
    my_cnx.close()
    streamlit.text(f'Thanks for adding: {choice2}')
    
