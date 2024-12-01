import streamlit as st
import pandas as pd
import numpy as np
import datetime
import requests


####################### TEMP CODE ###############################
POLYGON_BASE_URL = "https://api.polygon.io/v2/aggs/ticker"
POLYGON_API_KEY = st.secrets["polygon"]["api_key"]

@st.cache_data(ttl=86400)
def fetch_stock_data(symbol):
    print(f"Fetch data for {symbol}")

    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=30)
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = today.strftime("%Y-%m-%d")

    url = f"{POLYGON_BASE_URL}/{symbol}/range/1/day/{start_date_str}/{end_date_str}"

    response = requests.get(url, headers={"Authorization": f"Bearer {POLYGON_API_KEY}"})

    if response.status_code == 200:
        return True
    else:
        st.error(f"Failed to fetch IBM data: {response.status_code} - {response.text}")
        return None
stock_data = fetch_stock_data('IBM')

####################### TEMP CODE ###############################




# """
# Page 'render'
# """
API_KEY = st.secrets["openweather"]["api_key"]
#weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
#forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
city_coordinates = dict(lon=None, lat=None)

header = st.header(body=f"Robot Dreams Pyton - Weather Map & Data Visualization App")
text_input_city = st.text_input(label=f"Enter city name:", value="London")
fetch_button = st.button(label="Fetch")
sub_header = st.subheader(body=f'Current weather in:  {text_input_city}')
kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric('Hello', value=100)
kpi2.metric('Kpi 2', value=f'300 $')


df = pd.DataFrame({'lon': 17.747139 ,'lat':47.551964}, index=[0])
city_map = st.map(data=df, latitude="lat", longitude="lon")



####################### TEMP CODE ###############################
POLYGON_BASE_URL = "https://api.polygon.io/v2/aggs/ticker"
POLYGON_API_KEY = st.secrets["polygon"]["api_key"]

@st.cache_data(ttl=86400)
def fetch_stock_data(symbol):
    print(f"Fetch data for {symbol}")

    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=30)
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = today.strftime("%Y-%m-%d")

    url = f"{POLYGON_BASE_URL}/{symbol}/range/1/day/{start_date_str}/{end_date_str}"

    response = requests.get(url, headers={"Authorization": f"Bearer {POLYGON_API_KEY}"})

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None
####################### TEMP CODE ###############################