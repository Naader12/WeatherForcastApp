from weather_api import get_current_weather


# create main function
def main():
    print("\n\n==================================================")
    print("\nWelcome to the Weather App!")
    print("\n==================================================")

    # get user input
    city = input("\nEnter the city: ")
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
        display_weather(weather_data, units)
    else:
        print("Failed to retrieve weather data")

    


# create display_weather function (display's weather for user)
def display_weather(weather_data, units):

    if 'data' in weather_data:
        current_data = weather_data['data'][0]

        # determine temperature and wind speed units
        temperature_unit = '°C'
        if units == 'I':
            temperature_unit = "°F"

        wind_speed_unit = "m/s"
        if units == 'I':
            wind_speed_unit = "mph"

        print("\n==================================================")
        print("\nCurrent Weather:")
        print("\n==================================================")
        print(f"\nLocation: {current_data['city_name']}, {current_data['country_code']}")

        # set temperature value
        temperature_value = current_data['temp']
       
        print("------------------------------------------------")
        print(f"Temperature: {temperature_value}{temperature_unit}")
        print("------------------------------------------------")
        print(f"Description: {current_data['weather']['description']}")
        print("------------------------------------------------")
        print(f"Humidity: {current_data['rh']}%")

        # set wind speed value
        wind_speed_value = current_data['wind_spd']
    
        print("------------------------------------------------")
        print(f"Wind Speed: {wind_speed_value} {wind_speed_unit}")
        print("\n==================================================")
        print("\n Advanced Data")
        print("\n==================================================")
        print(f"\nSolar Radiation: {current_data['solar_rad']}")
        print("------------------------------------------------")
        print(f"\nAir Quality Index (AQI): {current_data['aqi']}")
        print("------------------------------------------------")
        print(f"\nDew Point: {current_data['dewpt']}{temperature_unit}")
        print("------------------------------------------------")
        print(f"\nDirect Normal Irradiance (DNI): {current_data['dni']}")
        print("------------------------------------------------")
        print(f"\nDiffuse Horizontal Irradiance (DHI): {current_data['dhi']}")
        print("------------------------------------------------")
        print(f"\nSolar Elevation Angle: {current_data['elev_angle']}")
        print("------------------------------------------------")
        print(f"\nGlobal Horizontal Irradiance (GHI): {current_data['ghi']}")
        print("------------------------------------------------")
        print(f"\nGust Speed: {current_data['gust']} {wind_speed_unit}")
        print("------------------------------------------------")
        print(f"\nLatitude: {current_data['lat']}")
        print("------------------------------------------------")
        print(f"\nLongitude: {current_data['lon']}")
        print("------------------------------------------------")
        print(f"\nSolar Noon Angle: {current_data['h_angle']}")
        print("------------------------------------------------")
        print(f"\nPrecipitation: {current_data['precip']}")
        print("------------------------------------------------")
        print(f"\nPressure: {current_data['pres']}")
        print("------------------------------------------------")
        print(f"\nSnowfall: {current_data['snow']}")
        print("------------------------------------------------")
        print(f"\nSea Level Pressure: {current_data['slp']}")
        print("------------------------------------------------")
        print(f"\nSunrise Time: {current_data['sunrise']}")
        print("------------------------------------------------")
        print(f"\nSunset Time: {current_data['sunset']}")
        print("------------------------------------------------")
        print(f"\nUV Index: {current_data['uv']}")
        print("------------------------------------------------")
        print(f"\nVisibility: {current_data['vis']}")
        print("------------------------------------------------")


    else:
        print("\n==================================================")
        print("\nInvalid or incomplete weather data.")
        print("\n==================================================")


if __name__ == "__main__":
    main()
    