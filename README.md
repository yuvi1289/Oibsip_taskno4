# Basic Weather App

## Description

The Basic Weather App is a command-line application built in Python that fetches and displays current weather data for a user-specified location or ZIP code using a weather API (such as OpenWeather API). It provides basic information such as temperature, humidity, and weather conditions.

## What the App Does

- The weather app runs in the command-line interface.
- Users can enter a city name or ZIP code to retrieve current and forecast weather information.
- It displays weather information based on the user's input, including:
    - Temperature (Fahrenheit)
    - Humidity (%)
    - Weather Conditions

## Requirements

Before starting, ensure you have installed the required dependencies using pip:
- requests
- json

You also need an API key from OpenWeatherMap.org. You can sign up for an API key [here](https://openweathermap.org/api).

## How to Use the Application

1. Open your terminal or command prompt.
2. Navigate to the directory where you have saved the project files.
3. Run the command `python weather_app.py`.
4. When prompted, type in the name of any city or ZIP code for which you'd like to know the weather.
5. Hit Enter.
6. You should see a display similar to the following:

    ```
    Enter city name or ZIP code: New York
    Weather Report for New York:
    Temperature: 5.87°C
    Humidity: 73%
    Weather Condition: overcast clouds
    ```

