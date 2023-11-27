import requests
url = 'https://api.frankfurter.app/'
def get_currency_list():
    r = requests.get(f'{url}currencies')
    dictionary = r.json()
    currency_list = []
    for key in dictionary.keys():
        currency_list.append(key)
    return currency_list
def get_rate(base, to):
    if base in get_currency_list() and to in get_currency_list():
        payload = {'from': base, 'to': to}
        r = requests.get(f'{url}latest', params=payload)
        dictionary = r.json()
        print(f'{dictionary["base"]}-{to}:\t{dictionary["rates"][to]}')
    else:
        print(f'''
Neteisingai suvestos valiutos. Galimų variantų sąrašas:
{get_currency_list()}
''')
get_rate('GBP', 'PLN')