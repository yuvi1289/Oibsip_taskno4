import requests
import json

def fetch_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == "404":
        print("City not found. Please try again.")
    else:
        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"Weather Report for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {description}")

def main():
    api_key = "API_KEY" #Put your OpenWeather Api key  
    location = input("Enter city name or ZIP code: ")
    weather_data = fetch_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
