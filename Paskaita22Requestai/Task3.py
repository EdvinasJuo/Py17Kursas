import requests
import re

r = requests.get('https://orai.15min.lt/prognoze/vilnius')

if r.status_code == 200:
    page_info = r.text
    weather = r'[+-]?\d+(?:.\d+)?°'
    weather_info = re.search(weather, page_info)
    print(f'Dabartine temperatura Vilniuje: {weather_info[0]}')
else:
    print('Nepavyko rasti rysio su svetaine..')