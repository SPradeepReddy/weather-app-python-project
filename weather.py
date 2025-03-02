import requests

API_KEY = "your_openweather_api_key"  # Replace with your actual API key from https://openweathermap.org/api
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"🌤 Weather in {city}: {data['weather'][0]['description']}")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        print(f"📈 Humidity: {data['main']['humidity']}%")
    else:
        print("❌ City not found!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
