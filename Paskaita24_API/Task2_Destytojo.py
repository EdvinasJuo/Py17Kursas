import requests
import json
url = 'https://api.frankfurter.app/'
def get_key(val, dct):
    """Little key by value extractor"""
    for k, v in dct.items():
        if val == v:
            return k
def currency_pair_analysis(base, to, start_date, end_date):
    payload = {'from': base, 'to': to}                                      # susikuriame parametrų žodyną
    r = requests.get(f'{url}{start_date}..{end_date}', params=payload)      # susikuriame užklausą pagal API dokumentaciją
    result = json.loads(r.text)                 # Atsakymą paverčiame Python žodynu
    new_dict = {}                               # Susikuriame tuščią žodyną
    for k, v in result['rates'].items():        # Užpildome jį reikšmėmis 'data': 'kursas'
        new_dict[k] = v[to]
    values_list = list(new_dict.values())       # Susikuriame kursų sąrašą
    min_value = min(values_list)                # Ištraukiame žemiausią reikšmę
    max_value = max(values_list)                # Ištraukiame aukščiausią reikšmę
    min_date = get_key(min_value, new_dict)     # Panaudojame pagalbinę funkciją rakto pagal reikšmę paieškai (gauname datą)
    max_date = get_key(max_value, new_dict)     # Gauname kitą datą
    ''' Formuojame Atsakymą:'''
    print(f'''
    Valiutų poroje {base}-{to}, periode nuo {start_date} iki {end_date}:
    Žemiausias kursas buvo {min_date} - {min_value}
    Aukščiausias kursas buvo {max_date} - {max_value}
    ''')
currency_pair_analysis('EUR','PLN', '2023-01-01', '2023-10-12')