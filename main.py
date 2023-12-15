from weather_api import get_current_weather


# create main function
def main():

    # welcome the user to the service
    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("\n\n$$\   $$\\                           $$\                              ")
    print("$$\   $$\                           $$\                              ")
    print("$$$$\ $$ | $$$$$$\   $$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\   $$$$$$$\\")
    print("$$ $$\$$ | \____$$\  \____$$\ $$  __$$ |$$  __$$\ $$  __$$\ $$  _____|")
    print("$$ \$$$$ | $$$$$$$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|\$$$$$$\\")
    print("$$ |\$$$ |$$  __$$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |       \____$$\\")
    print("$$ | \$$ |$$$$$$$$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      $$$$$$$  |")
    print("\__|  \__|\_______| \_______| \_______| \_______|\__|      \_______/")
    print("\n$$\      $$\                      $$\     $$\                           ")                          
    print("$$ | $\  $$ |                     $$ |    $$ |")                          
    print("$$ |$$$\ $$ | $$$$$$\   $$$$$$\ $$$$$$\   $$$$$$$\   $$$$$$\   $$$$$$\  ")  
    print("$$ $$ $$\$$ |$$  __$$\  \____$$\\_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\ ")
    print("$$$$  _$$$$ |$$$$$$$$ | $$$$$$$ | $$ |    $$ |  $$ |$$$$$$$$ |$$ |  \__|")
    print("$$$  / \$$$ |$$   ____|$$  __$$ | $$ |$$\ $$ |  $$ |$$   ____|$$ |")      
    print("$$  /   \$$ |\$$$$$$$\ \$$$$$$$ | \$$$$  |$$ |  $$ |\$$$$$$$\ $$ |")      
    print("\__/     \__| \_______| \_______|  \____/ \__|  \__| \_______|\__|")
    print("\n $$$$$$\                                $$\                     ")
    print("$$  __$$\                               \__|                    ")
    print("$$ /  \__| $$$$$$\   $$$$$$\ $$\    $$\ $$\  $$$$$$$\  $$$$$$\  ")
    print("\$$$$$$\  $$  __$$\ $$  __$$\\$$\  $$  |$$ |$$  _____|$$  __$$\ ")
    print(" \____$$\ $$$$$$$$ |$$ |  \__|\$$\$$  / $$ |$$ /      $$$$$$$$ |")
    print("$$\   $$ |$$   ____|$$ |       \$$$  /  $$ |$$ |      $$   ____|")
    print("\$$$$$$  |\$$$$$$$\ $$ |        \$  /   $$ |\$$$$$$$\ \$$$$$$$\ ")
    print(" \______/  \_______|\__|         \_/    \__| \_______| \_______|")      



    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("\n\n==================================================")
    print("\nWelcome to the Weather App!")
    print("\n==================================================")

    # get user input
    city = input("\nEnter the city: ")
    country = input("Enter the country code: ")
    units = input("Enter units (e.g., 'M' for Metric, 'I' for Imperial): ")
    language = input("Enter language code (e.g., 'en' for English): ")

    # ask user if they want to see advanced data
    show_advanced_data = input("Do you want to see advanced data? (yes/no): ").lower() == 'yes'

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
        display_weather(weather_data, units, show_advanced_data)
    else:
        print("Failed to retrieve weather data")

    
    # have a nice day message
    print("\n==================================================")
    print("\nHave a nice day!")
    print("\n==================================================")

    


# create display_weather function (display's weather for user)
def display_weather(weather_data, units, show_advanced_data=False):

    if 'data' in weather_data:
        current_data = weather_data['data'][0]

        # determine units based on user selection
        temperature_unit = '°C'
        if units == 'I':
            temperature_unit = "°F"

        wind_speed_unit = "m/s"
        if units == 'I':
            wind_speed_unit = "mph"

        solar_unit = "W/m²"
        if units == 'I':
            solar_unit = "(BTU/h·ft²)"

        pressure_unit = "hPa"
        if units == 'I':
            pressure_unit = "inHg"

        distance_unit = "km"
        if units == 'I':
            distance_unit = "mi"

        small_distance_unit = "mm"
        if units == 'I':
            small_distance_unit = 'in'

        print("\n==================================================")
        print("\nCurrent Weather:")
        print("\n==================================================")
        print(f"\nLocation: {current_data['city_name']}, {current_data['country_code']}")
        print("------------------------------------------------")
        print(f"Temperature: {current_data['temp']}{temperature_unit}")
        print("------------------------------------------------")
        print(f"Description: {current_data['weather']['description']}")
        print("------------------------------------------------")
        print(f"Humidity: {current_data['rh']}%")
        print("------------------------------------------------")
        print(f"Wind Speed: {current_data['wind_spd']} {wind_speed_unit}")
        print("\n==================================================")

        # addition of advanced data
        if show_advanced_data:
            print("\n Advanced Data")
            print("\n==================================================")
            print(f"\nSolar Radiation: {current_data['solar_rad']} {solar_unit}")
            print("------------------------------------------------")
            print(f"Air Quality Index (AQI): {current_data['aqi']}")
            print("------------------------------------------------")
            print(f"Dew Point: {current_data['dewpt']}{temperature_unit}")
            print("------------------------------------------------")
            print(f"Direct Normal Irradiance (DNI): {current_data['dni']} {solar_unit}")
            print("------------------------------------------------")
            print(f"Diffuse Horizontal Irradiance (DHI): {current_data['dhi']} {solar_unit}")
            print("------------------------------------------------")
            print(f"Solar Elevation Angle: {current_data['elev_angle']}°")
            print("------------------------------------------------")
            print(f"Global Horizontal Irradiance (GHI): {current_data['ghi']}")
            print("------------------------------------------------")
            print(f"Gust Speed: {current_data['gust']} {wind_speed_unit}")
            print("------------------------------------------------")
            print(f"Latitude: {current_data['lat']}")
            print("------------------------------------------------")
            print(f"Longitude: {current_data['lon']}")
            print("------------------------------------------------")
            print(f"Solar Noon Angle: {current_data['h_angle']}°")
            print("------------------------------------------------")
            print(f"Precipitation: {current_data['precip']} {small_distance_unit}")
            print("------------------------------------------------")
            print(f"Pressure: {current_data['pres']} {pressure_unit}")
            print("------------------------------------------------")
            print(f"Snowfall: {current_data['snow']} {small_distance_unit}")
            print("------------------------------------------------")
            print(f"Sea Level Pressure: {current_data['slp']} {pressure_unit}")
            print("------------------------------------------------")
            print(f"Sunrise Time: {current_data['sunrise']} o'clock")
            print("------------------------------------------------")
            print(f"Sunset Time: {current_data['sunset']} o'clock")
            print("------------------------------------------------")
            print(f"UV Index: {current_data['uv']}")
            print("------------------------------------------------")
            print(f"Visibility: {current_data['vis']} {distance_unit}")
            print("------------------------------------------------")


    else:
        print("\n==================================================")
        print("\nInvalid or incomplete weather data.")
        print("\n==================================================")


if __name__ == "__main__":
    main()
    