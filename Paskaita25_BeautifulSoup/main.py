import requests
from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

#-----------------------------------------------------------------------------------------

# SUKURIAMAS SOUP KLASES OBJEKTAS
# soup = BeautifulSoup(html, "html.parser")
# print(type(soup))

#-----------------------------------------------------------------------------------------

#GALIMA PASIIMTI PROPERTY IS HTML, SIUO ATVEJU PASIEMAM BODY ir DIV kuri pirma sutinka
# print(soup.body) # PASIEMAM BODY
# print(soup.body.div) #PASIEMAM VIENA DIV (PIRMA KURI SUTINKA)
# print(soup.find("div")) # FIND SURAS VEL TIK PIRMA DIV
# print(soup.find_all("div")) # FIND SURAS VISUS DIV BET GRAZINS LIST ELEMENTA. JEIGU NURIM KAZKA PASIIMTI REIKIA KREIPTIS KAIP I LISTA NURODANT INDEXA[0]
# print(soup.find(id="first")) # SURAS PAGAL ID="First".
# print(soup.find(class_="special")) # KAI IESKOM PAGAL KLASE REIKIA PRIDETI UNDERSCORA, nes paprastas class yra rezervuotas pythono kalboj
# print(soup.find_all(attrs={'data-example': 'yes'})) # IESKOM PAGAL ATRIBUTA

#-----------------------------------------------------------------------------------------

#VEIKIA IS SU CSS FAILAIS. REIKIA PAIMTI SU SELECT
# print(soup.select(('#first')))
# print(soup.select(('.special')))

#-----------------------------------------------------------------------------------------

# ISTRAUKIAMAS KONKRETUS TEKSTAS
# element = soup.select('.special')[0]  # NURODOMAS indexas kuri teksta paimti is special
# print(element.get_text())


# ISTRAUKIAMAS IS LIST
# elements = soup.select('.special')
# for element in elements:
#     print(element.get_text())

# ATPRINITI VISUS ELEMENTUS
# for element in elements:
#     print(element.name)

# DAR KITAS BUDAS
# elements = soup.select('meta')
# print(elements[0].attrs)

# DAR VIENAS BUDAS
# attribute = soup.select('div')[0]['id']
# print(attribute)

#-----------------------------------------------------------------------------------------

# NAVIGACIJA PER HTML DOKUMENTA
# soup = BeautifulSoup(html, "html.parser")
#
# print(soup.div.contents) # GRAZINA CONTENTS
# print(soup.div.next_sibling.next_sibling) # GRAZINA HERARCHISKAI MAZESNI ELEMENTA
#
#
# li = soup.find("li")
# print(li.next_sibling.next_sibling) # VAIKSTO PER SIBLINGS
#
#
# li = soup.find('li')
# res = li.find_parent().find_previous_sibling()['id'] #KOMBINUOJAM
# print(res)
#
# res = soup.body.next_element.next_element.next_element.next_element.get_text() # PASIEMEM TEKSTA
# print(res)
#-----------------------------------------------------------------------------------------
#
#                                         #PAVYZDYS
# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
#
# blokas = soup.find('div', class_ = 'headline')
# # print(blokas.prettify())   # NAUDOJAMAS TIK ATVAIZDAVIMUI, NES PAVIRSTA STRING IR PRARANDA VISAS SOUP FUNKCIJAS
#
# kategorija = blokas.find('div', class_ = 'headline-category').text.strip() #text.strip() grazina teksta be bereikalingu tusciu tarpu
# tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
# linkas = blokas.find('a', class_="CBarticleTitle")['href']
#
# print(kategorija)
# print(tekstas)
# print(linkas)

#-----------------------------------------------------------------------------------------
# GAUTI VISU BLOKU INFORMACIJA

# from bs4 import BeautifulSoup
# import requests
#
# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_ = 'headline')
#
# for blokas in blokai:
#     try:
#         kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
#         tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
#         linkas = blokas.find('a', class_="CBarticleTitle")['href']
#         print(kategorija)
#         print(tekstas)
#         print(linkas)
#     except AttributeError: # JEIGU KAZKO NERAS, KAD NENULUZTU PROGRAMA
#         pass

#-----------------------------------------------------------------------------------------
# IRASYTI INFORMACIJA I CSV FAILA
# from bs4 import BeautifulSoup
# import requests
# import csv
#
# source = requests.get('https://www.delfi.lt/').text
#
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_="headline")
#
# with open("delfi_naujienos.csv", 'w', encoding="UTF-8", newline='') as failas:
#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['KATEGORIJA', 'ANTRAŠTĖ', 'NUORODA'])
#
#     for blokas in blokai:
#         try:
#             kategorija = blokas.find("div", class_='headline-category').text.strip()
#             tekstas = blokas.find('a', class_="CBarticleTitle").text.strip()
#             linkas = blokas.find('a', class_="CBarticleTitle")['href']
#             print(kategorija, tekstas, linkas)
#             csv_writer.writerow([kategorija, tekstas, linkas])
#         except:
#             pass

#-----------------------------------------------------------------------------------------

# DAUGIAU REZULTATU SU REGEX

# from bs4 import BeautifulSoup
# import requests
# import csv
# import re
#
# source = requests.get('https://www.delfi.lt/').text
#
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_=re.compile(r'col-xs-.'))
#
# with open("delfi_naujienos.csv", 'w', encoding="UTF-8", newline='') as failas:
#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['KATEGORIJA', 'ANTRAŠTĖ', 'NUORODA'])
#
#     for blokas in blokai:
#         try:
#             kategorija = blokas.find("div", class_='headline-category').text.strip()
#             tekstas = blokas.find('a', class_="CBarticleTitle").text.strip()
#             linkas = blokas.find('a', class_="CBarticleTitle")['href']
#             print(kategorija, tekstas, linkas)
#             csv_writer.writerow([kategorija, tekstas, linkas])
#         except:
#             pass

#-----------------------------------------------------------------------------------------
                                        # KITAS PAVYZDYS
import csv

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung').text
soup = BeautifulSoup(source, 'html.parser')

blokai = soup.find_all('div', class_ = 'mobiles-product-card card card__product card--anim js-product-compare-product')

with open("Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])

    for blokas in blokai:
        try:
            pavadinimas = blokas.find('a', class_ = 'mobiles-product-card__title js-open-product').text.strip()
            men_kaina = blokas.find('div', class_ = 'mobiles-product-card__price-marker').text.strip()
            kaina = blokas.find_all('div', class_ = 'mobiles-product-card__price-marker')[1].text.strip()
            print(pavadinimas, men_kaina, kaina)
            csv_writer.writerow([pavadinimas, men_kaina, kaina])
        except:
            pass