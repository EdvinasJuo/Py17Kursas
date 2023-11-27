from bs4 import BeautifulSoup
import requests

# Parašyti programą, kuri atspausdintu visas puslapio www.15min.lt "Redakcija rekomenduoja" skilties antraštes

source = requests.get('https://www.15min.lt/').text
soup = BeautifulSoup(source, 'html.parser')

recommends_block = soup.find('div', class_ = 'widget-horizontal-items swipeable')

items = recommends_block.find_all('div', class_="item type_1")

count = 1
for item in items:
    try:
        heading = item.find('a', class_="title").text.strip()
        print(f'{count}. {heading}')
        count += 1

    except AttributeError:
        pass
