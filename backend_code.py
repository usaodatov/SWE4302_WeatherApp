import requests                                      # import the requests library to send HTTP requests
import json                                          # import the json library to parse JSON data


'''
Flow of the code:

1. The function get_weather_data sends a GET request to 
the OpenWeatherMap API to get weather data for a certain city.

2. The function accepts a city name as an argument and returns, 
if all goes well, the weather data in the form of a dictionary.

3. The function returns None if the request fails or if the city is not valid.

4. The function display_weather pulls out and shows weather particulars from the weather data dictionary.

5. The function takes care of exceptions of the KeyError kind that may 
crop up if the data structure is not as it should be.

6. The main.py script prompts the user for a city name, calls the get_weather_data function 
to retrieve weather data, then invokes the display_weather function to present the weather particulars.

7. If the retrieval of weather data fails or the city is invalid, the script will display an error message.

8. The file backend_code.py includes two functions used in the script main.py. These are get_weather_data
and display_weather.

'''



def get_weather_data(city): # Function to get weather data from OpenWeatherMap API
    api_key = "e43ee3855b6b5e89e32ac6c050235f29"  # My API @openweathermap
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(base_url)                      # Send a GET request to the OpenWeatherMap API
        data = response.json()                                              # Parse the JSON response

     # 'Invalid city' error handling based on "cod"
        if data.get("cod") != 200:                             # Check if the response status code is 200 (OK)
            print(f"Error: {data.get('message', 'Unknown error')}")
            return None

        return data                                            # Return the weather data as a dictionary

    except requests.exceptions.RequestException as e:          # Catch any network exception
        # Display error message if an error occurs
        print(f"Error retrieving weather data for {city}: Error Code:  {e}")
        return None                                                         # Return None if an error occurs

def display_weather(data): # Function to display weather data
    try:
        # Extract weather details and assign to variables
        city = data["name"]                                                 # Get city name
        country = data["sys"]["country"]                                    # Get country code
        temp = data["main"]["temp"] - 273.15                    # Convert from Kelvin to Celsius c = K-273.15
        condition = data["weather"][0]["description"]                       # Get weather condition
        humidity = data["main"]["humidity"]                                 # Get humidity
        wind_speed = data["wind"]["speed"]                                  # Get wind speed

        # Display weather details
        print(f"The weather in {city} ({country}) :")
        print(f"Temperature: {temp:.2f}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    except KeyError:                                         # Catch any KeyError exception
        print("Invalid data received.")                      # Display error message if invalid data received
