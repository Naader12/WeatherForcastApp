from weather_api import get_current_weather


# create main function
def main():
    print("Welcome to the Weather App!")

    # get user input
    city = input("Enter the city: ")
    country = input("Enter the country code: ")
    units = input("Enter units (e.g., 'M' for Metric, 'I' for Imperial): ")
    language = input("Enter language code (e.g., 'en' for English): ")

    # get api key
    api_key = 'fe52dd6395fb413f8d9ea3886042e8b9'

    # set all necessary parameters
    weather_params = {
        'api_key': api_key,
        'city': city,
        'country': country,
        'units': units,
        'language': language,
    }
    params = {
        'key': api_key,
        'city': city,
        'country': country,
        'units': units,
        'lang': language,
    }

    weather_data = get_current_weather(**weather_params)

    if weather_data:
        # process and use the weather data
        print(weather_data)
    else:
        print("Failed to retrieve weather data")


# create display_weather function (display's weather for user)
def display_weather(weather_data):
    if 'data' in weather_data:
        current_data = weather_data['data'][0]

        print("Current Weather:")
        print(f"Location: {current_data['city_name']}, {current_data['country_code']}")
        print(f"Temperature: {current_data['temp']}°C")
        print(f"Description: {current_data['weather']['description']}")
        print(f"Humidity: {current_data['rh']}%")
        print(f"Wind Speed: {current_data['wind_spd']} m/s")
    else:
        print("Invalid or incomplete weather data.")


if __name__ == "__main__":
    main()
    