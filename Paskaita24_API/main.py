import requests

# people = requests.get('http://api.open-notify.org/astros.json')
# print(people.text)
#----------------------------------------------------------------------------------

# headers = {"apikey": "KQVVznJtJA4eY4DBAk0cCGATHJ0BaHyF"}
# months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# for month in months:
#     url = f"https://api.apilayer.com/exchangerates_data/2021-{month}-16?symbols=USD&base=EUR"
#     response = requests.get(url, headers=headers)
#     result = response.json()
#     print(f"2021-{month}-15     EUR-USD    {result['rates']['USD']}")

#----------------------------------------------------------------------------------

import webbrowser as wb
import requests
import json

API_key = '14795746-624081efd179b5bd9be0efe43'


def open_first(query):
   payload = {'key': API_key, 'q': query, 'img_type': 'photo', 'pretty': 'true'}
   r = requests.get('https://pixabay.com/api/', params=payload)
   print(r.url)
   json_str = r.text
   result = json.loads(json_str)
   wb.open_new_tab(result['hits'][1]['largeImageURL'])

open_first('elephant')

#----------------------------------------------------------------------------------
