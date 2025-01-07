
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

if __name__ == "__main__": # Run the script if it's the main program (not imported)
    cities = input("Enter city names separated by commas: ").split(",")  # Input multiple cities
    for city in cities:                       # Loop through each city
        city = city.strip()  # Remove any extra spaces
        weather_data = get_weather_data(city) # Get weather data for the city
        if weather_data:                      # If weather data is available
            display_weather(weather_data)     # Display weather data
            print()                           # Print a blank to separate the weather data of different cities
        else:                                 # If weather data is not available
            print(f"Could not retrieve weather data for '{city}'. Please try again.")
