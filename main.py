

import requests
import json
import win32com.client as wincom
import time
city = input("enter the name of the city \n")
url = f"https://api.weatherapi.com/v1/current.json?key=029278eb1df24b41acc71930230908&q={city}"
r = requests.get(url)

wdic = json.loads(r.text)


temperature_c = wdic["current"]["temp_c"]
print(f"The current temperature in {city} is {temperature_c}°C")

speak = wincom.Dispatch("SAPI.Spvoice")
text = f"The current weather in {city} is {temperature_c} degrees Celsius ."

speak.Speak(text)
