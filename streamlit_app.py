import streamlit

streamlit.title('My Parents New Healthy Diner')

# Add Breakfast title and menu

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Free-range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# Add Smoothie Menu

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

  # Import fruit list with pandas
import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

  # Add a pick list to pick the fruit the user wants to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

  # Display the table on the page.
streamlit.dataframe(fruits_to_show)
