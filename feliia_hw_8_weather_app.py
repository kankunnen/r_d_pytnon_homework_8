import streamlit as st


# """
# Page 'render'
# """

header = st.header(body=f"Robot Dreams Pyton - Weather Map & Data Visualization App")
text_input_city = st.text_input(label=f"Enter city name:", value="London")