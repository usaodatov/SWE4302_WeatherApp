
'''

The weather application has a main entry point defined by this script.

It asks the user to provide a name for the city.
It then gets the weather data associated with that city using the `get_weather_data` function.
That function is in the core module, `backend_code.py`, which houses all the application's essential logic.
The entry point script, however, is a simple affair, with only two necessary function calls to make:
one to retrieve data and another to display it.
If the user or upstream data sources provide invalid inputs,
the script has error messages built in to handle those contingencies.

'''



from backend_code import get_weather_data, display_weather          # Importing functions from backend_code.py

if __name__ == "__main__":
    city = input("Enter city name: ").strip()                       # Get city name from user
    weather_data = get_weather_data(city)                           # Getting weather data - routing to backend

    if weather_data:                                                # If data retrieved from back end valid, display it
        display_weather(weather_data)
    else:                                                           # If data not retrieved, display error message
        print(f"Could not retrieve weather data for '{city}'. Please try again or Enter valid city.")
