import requests

api_key = 'fe52dd6395fb413f8d9ea3886042e8b9'


def get_current_weather(api_key, city, country, units='M', language='en'):
    
    endpoint = 'https://api.weatherbit.io/v2.0/current'

    params = {
        'key': api_key,
        'city': city,
        'country': country,
        'units': units,
        'lang': language,
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
