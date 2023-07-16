import streamlit as st
import requests

st.set_page_config(page_title='Погода',page_icon=":bar_chart",layout="wide")

try:
    city = st.text_input('Введите город: ')  # ввод города
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?appid=214d146724ad2dfdc38107dc9fbed72d&q={city}").json()
    st.subheader(
        f"Температура: {int(round(res['main']['temp'] - 274.15, 0))} °C")  # число,округление,вид,-274.15,до каких
    st.subheader(f"Ощущается как: {int(round(res['main']['feels_like'] - 274.15, 0))} °C")
    st.subheader(f"Влажность: {res['main']['humidity']} %")
    st.subheader(f"Давление: {res['main']['pressure']} Па")
except KeyError:
    pass