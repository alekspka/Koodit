# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests


hakusana = input("Name a city: ")

api_key = "870e779592515e63783ea34944e3f8a0"
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid={api_key}"
vastaus = requests.get(pyyntö)

if vastaus.status_code == 200:
    data = vastaus.json()
    säätila = data["weather"][0]["description"]
    lämpötila_kelvin = data["main"]["temp"]
    lämpötila_celsius = lämpötila_kelvin - 273.15

    print(f"Weather: {säätila.capitalize()}")
    print(f"Temperature: {lämpötila_celsius:.2f} °C")
else:
    print("Couldn't find the city.")

