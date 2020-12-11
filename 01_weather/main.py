import requests
from requests.exceptions import HTTPError

params = {'lang': 'ru', 'nTqum': ''}
url_template = 'http://wttr.in/{}'
cities = ['Лондон', 'Шереметьево', 'Череповец']

for city in cities:
    try:
        url = url_template.format(city)
        response = requests.get(url, params=params)
        print(response.url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(response.text)
