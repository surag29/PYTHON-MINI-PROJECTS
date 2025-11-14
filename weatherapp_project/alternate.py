import requests
import json
from config import API_KEY

city = input("ENTER CITY NAME: ")

url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

try:
    r = requests.get(url)
    r.raise_for_status()        # To catch HTTP errors

    data = r.json()             # Direct JSON parsing

    if "error" in data:
        print("❌ Error:", data["error"]["message"])
    else:
        print("🌡 Temperature in", city, "=", data["current"]["temp_c"], "°C")

except requests.exceptions.RequestException as e:
    print("❌ Network Error:", e)
