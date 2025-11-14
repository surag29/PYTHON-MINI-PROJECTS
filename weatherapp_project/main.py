import requests
import json
from config import API_KEY
city =  input("ENTER CITY NAME ")
url = f"https://api.weatherapi.com/v1/current.json?key=3c121dad148e4686af3100053251411&q={city}"
r = requests.get(url)
print(r.text)
print(type(r.text))
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])