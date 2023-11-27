import requests
import json

def currency_pair_analysis(first_currency, second_currency, start_date, end_date):
    url = f'https://api.frankfurter.app/{start_date}..{end_date}'
    r = requests.get(url)
    if r.ok:
        data_dict = json.loads(r.text)
        print(data_dict)
        rates = data_dict["rates"]
        print(rates)

        print(rates.values())

        print(f'Valiutų poroje {first_currency}-{second_currency}, periode nuo {start_date} iki {end_date}:')
        # print(f'Žemiausias kursas buvo {min_rate}')
        # print(f'Didžiausias kursas buvo {max_rate}')

    else:
        print(f'Nepavyko pasiekti puslapio. Statuso kodas: {r.status_code}')

currency_pair_analysis("EUR", "GBP", "2019-12-11", "2019-12-12")