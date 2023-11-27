import requests
import json

def get_rates(first_currency, second_currency):

    r = requests.get('https://api.frankfurter.app/latest')
    if r.ok:
        data_dict = json.loads(r.text)
        rates = data_dict["rates"]
        base = data_dict["base"]

        if ((first_currency != base and first_currency not in rates)
                or (second_currency != base and second_currency not in rates)):
            print("Neteisingai suvestos valiutos. Galimų variantų sąrašas:")
            currency = ', '.join(rates.keys())
            print(currency + ", " + base)
        else:
            print(f'{first_currency}-{second_currency}: {rates.get(second_currency): >15}')

    else:
        print(f'Nepavyko pasiekti puslapio. Statuso kodas: {r.status_code}')


get_rates('EUR', 'PLN')