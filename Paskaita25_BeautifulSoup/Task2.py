from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('div', class_ = 'headline')

count = 1
for blokas in blokai:
    try:
        tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
        count += 1
    except AttributeError: # JEIGU KAZKO NERAS, KAD NENULUZTU PROGRAMA
        pass

print(f"Straipsniu puslapyje yra : {count - 1}")