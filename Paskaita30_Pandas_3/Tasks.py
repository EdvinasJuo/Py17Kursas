import numpy as np
import pandas as pd

# 1. Ištraukite lentelę iš šios svetainės. Išsaugokite kintamąjame.
duomenys_html = pd.read_html('https://work.studentnews.eu/s/3695/75547-European-countries-the-table-language-population-capital-currency-phone-code-internet-code.htm')
table = duomenys_html[1]

# 2. šių duomenų pagrindu sukurkite CSV ir Excelio failus. Patikrinkite, ar suveikė.
table.to_csv('result.csv', index=False)
table.to_excel('result.xlsx', sheet_name='Sheet1')

# 3 Nuskaitykite į DF šį failą
print("--------------------------3----------------------------")
top = pd.read_csv('top_20_CA_wildfires.csv', encoding='ISO-8859-1')
print(top.head())

# 4 Kiek unikalių reikšmių yra stulpelyje 'cause'?
print("--------------------------4----------------------------")
unique_elements_of_cause = top['cause'].nunique()
print(unique_elements_of_cause)

# 5 Kokios gaisrų priežastys, kiek kartų pasitaiko lentelėje?
print("--------------------------5----------------------------")
causes_of_fire = top['cause'].value_counts()
print(causes_of_fire)

# 6 Kuriais metais buvo daugiausia gaisrų?
print("--------------------------6----------------------------")
years_of_most_fires = top['year'].value_counts().max()
name_of_most_fires = top['year'].value_counts().idxmax()
print(name_of_most_fires, years_of_most_fires)

# 7. Kiek buvo tokių gaisrų, kuriuose žuvo žmonės?
print("--------------------------7----------------------------")
fires_that_have_killed_people = (top['deaths'] > 0).sum()
print(fires_that_have_killed_people)

#8 Surūšiuokite eilutes pagal metus. Išsiaiškinkite, kaip rūšiuoti, kad naujausi gaisrai būtų viršuje
print("--------------------------8----------------------------")
sorted_fires = top.sort_values(['year','month'] ,ascending=False)
print(sorted_fires)

#9 Parašykite funkciją, kuri mėnesio pavadinimą verstų skaičiumi.
# Naudodami .apply() lentelėje pakeiskite mėnesių pavadinimus skaičiais.
print("--------------------------9----------------------------")
months = {
    'January': 1,
    'Feruary': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}
def change_month_name_into_number(month):
    return months.get(month, month)

top['month'] = top['month'].apply(change_month_name_into_number)
print(top.to_string())

# 10 Nuskaitykite lentelę iš čia.
print("--------------------------10----------------------------\n")
table_html = pd.read_html('https://lt.wikipedia.org/wiki/S%C4%85ra%C5%A1as:Lietuvos_miestai_pagal_gyventojus')
table_wiki = table_html[0]
original_table = table_wiki.set_index('Miestas')

original_table = original_table.drop('Tankumas (2019)', axis=1)
original_table = original_table.drop('Eilė', axis=1)

original_table = original_table.fillna(0)


for col in original_table.columns:
    original_table[col] = original_table[col].apply(lambda x: int(x) if str(x).isnumeric() else 0)

print(original_table.info())