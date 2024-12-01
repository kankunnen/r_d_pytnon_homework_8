import streamlit as st
import pandas as pd
from pandas import DataFrame
import numpy as np
import datetime
import requests


class FetchWeatherResult:
    def __init__(self):
        self.error_code: int
        self.dataFrame: DataFrame
        self.lon: float
        self.lat: float
        self.temperature: str
        self.humidity: str
        self.wind_speed: str
        self.no_data_found: bool


API_KEY = st.secrets["openweather"]["api_key"]


@st.cache_data(ttl=86400)
def fetch_weather_data(city) -> FetchWeatherResult:
    # city = 'London'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={
        city}&appid={API_KEY}&units=metric'

    response = requests.get(url=weather_url)

    if response.status_code == 200:
        return response.json()
    else:
        st.write(f"Fetching weather data failes {
                 response.status_code} - {response.text}")


def process_weather_data(weather_data) -> FetchWeatherResult:

    main_section = weather_data['main']
    coord_section = weather_data['coord']
    wind_section = weather_data['wind']
    fetchData = FetchWeatherResult()
    if 'main' in weather_data:
        df = pd.DataFrame([main_section])
        print(df)
        fetchData.humidity = df.at[0, 'humidity']
        fetchData.temperature = df.at[0, 'temp']
        fetchData.no_data_found = False
    if 'coord' in weather_data:
        df = pd.DataFrame([coord_section])
        print(df)
        fetchData.lon = df.at[0, 'lon']
        fetchData.lat = df.at[0, 'lat']
    if 'wind' in weather_data:
        df = pd.DataFrame([wind_section])
        fetchData.wind_speed = df.at[0, 'speed']
        print(df)
    else:
        fetchData.no_data_found = True

    return fetchData


# """
# Page 'render'
# """
# weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
# forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
city_coordinates = dict(lon=None, lat=None)

header = st.header(
    body=f"Robot Dreams Pyton - Weather Map & Data Visualization App")
text_input_city = st.text_input(label=f"Enter city name:", value="London")
if text_input_city:
    result = process_weather_data(fetch_weather_data(text_input_city))
fetch_button = st.button(label="Fetch")
sub_header = st.subheader(body=f'Current weather in:  {text_input_city}')
kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric('Temperature (\u00B0C)', value=f'{result.temperature} \u00B0C')
kpi2.metric('Humidity (%)', value=f'{result.humidity} %')
kpi3.metric('Wind Speed (m/s)', value=f'{result.wind_speed} m/s')

df = pd.DataFrame({'lon': result.lon, 'lat': result.lat}, index=[0])
city_map = st.map(data=df, latitude="lat", longitude="lon")
