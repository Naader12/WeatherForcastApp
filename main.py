from weather_api import get_current_weather

api_key = 'fe52dd6395fb413f8d9ea3886042e8b9'

 params = {
        'key': api_key,
        'city': city,
        'country': country,
        'units': units,
        'lang': language,
    }

weather_data = get_weather(**weather_params)

if weather_data:
    #process and use the weather data as needed
    print(weather_data)