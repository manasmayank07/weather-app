import requests
from config import API_KEY

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f"Temperature in {city}: {temp}°C")
        print(f"Weather: {weather}")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
