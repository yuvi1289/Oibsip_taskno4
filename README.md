# Basic-Weather-App

Description:

Creating a command-line weather app in python that fetches and displays the current weather data for the user-specified location or ZIP code (e.g., City name or the zip code) using a weather API(like OpenWeather api). Shows the basic information such as the temperture, humidity, and weather conditions.

What the app does:

* The weather app will run in the command-line 
* Where  users can enter a city name to get current and forecast weather information. 
* It displace the weather information for the Users based on there input.
* And it displaces the following information:
    - Temperature (Fahrenheit)
    - Humidity %
    - Weather Conditions

Requirements:

Before you start, make sure you have installed the required dependencies using pip:
- requests
- json
You also need an API key from OpenWeatherMap.org. You can sign up for an API key [here](https://openweathermap.org/api).



How to use the application:

1. Open your terminal or command prompt.
2. Navigate to the directory where you have saved the project files.
3. Run the command "python weather_app.py"
4. When prompted, type in the name of any city or zip you would like to know about its  weather.
5. Hit Enter.
6. You should see a display that looks something like this:
    Enter city name or ZIP code: new york
    Weather Report for New York:
    Temperature: 5.87°C
    Humidity: 73%
    Weather Condition: overcast clouds
