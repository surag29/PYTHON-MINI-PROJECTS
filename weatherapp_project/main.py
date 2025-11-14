import requests
import json
from config import API_KEY
city =  input("ENTER CITY NAME ")
url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
r = requests.get(url)
print(r.text)
print(type(r.text))
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])