from bs4 import BeautifulSoup
import requests

phones = []
prices = []

for page_number in range(1, 3):
    url = f'https://www.telia.lt/prekes/mobilieji-telefonai/samsung?page={page_number}'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')

    blokai = soup.find_all('div', class_='mobiles-product-card card card__product card--anim js-product-compare-product')

    for blokas in blokai:
        try:
            pavadinimas = blokas.find('a', class_='mobiles-product-card__title js-open-product').text.strip()
            kaina = blokas.find_all('div', class_='mobiles-product-card__price-marker')[1].text.strip()

            # Remove spaces and &nbsp; from kaina, replace , with ., and remove € symbol
            kaina = kaina.replace(' ', '').replace('\xa0', '').replace(',', '.').replace('€', '')

            phones.append(pavadinimas)
            prices.append(float(kaina))
        except:
            pass

# Find the index of the minimum and maximum price
min_price_index = prices.index(min(prices))
max_price_index = prices.index(max(prices))

min_price_phone = phones[min_price_index]
max_price_phone = phones[max_price_index]

print(f'Maziausiai kaina : {min(prices)} € - Telefonas: {min_price_phone}')
print(f'Didziausia kaina: {max(prices)} € - Telefonas: {max_price_phone}')