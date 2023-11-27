import numpy as np
import pandas as pd

# np.random.seed(1)
#
# df = pd.DataFrame(np.random.rand(5, 6),
#                   ['a', 'b', 'c', 'd', 'e'],
#                   ['U', 'V', 'W', 'X', 'Y', 'Z'])
#
# print(df)
# print("---------------------------------")
# table = df[df > 0.1]
# print("---------------------------------")
# print(table.isnull())
# print("---------------------------------")
# print(table.isnull().sum())  # PASKAICIUOJAM KIEK TRUE REIKSMIU
# print(table["Y"].isnull())
#
# # ------------------------------------------DROPNA----------------------------------------
# print("---------------------------------")
# a = table.dropna()
# print(a)  # ISMES VISUS NOT A NUMBERIUS
#
# a = table.dropna(thresh=5)  # ISMETAM TIK 5 EILES JEIGU JU TIEK YRA
# print(a)
#
# # ------------------------------------------FILLNA----------------------------------------
# a = table.fillna(value=table.mean())  # UZPILDOM STULPELIU VIDURKIU
# print(a)
#
# table['W'].fillna(value=table['W'].mean())  # UZPILDOM TIK VIENA STULPELI
# print(a)

# ------------------------------------------GRUPAVIMAS----------------------------------------
duomenys = {'Šalis': ['Lietuva',
                      'Lietuva',
                      'Lietuva',
                      'Latvija',
                      'Latvija',
                      'Latvija',
                      'Estija',
                      'Estija',
                      'Estija'],
            'Miestas': ['Vilnius',
                        'Kaunas',
                        'Klaipėda',
                        'Ryga',
                        'Ventspilis',
                        'Daugpilis',
                        'Talinas',
                        'Tartu',
                        'Pernu'],
            'Gyv': [541, 287, 147, 716, 43, 105, 400, 101, 46]}

data = pd.DataFrame(duomenys)
print(data)

baltic = data.groupby('Šalis')
print(baltic['Gyv'].sum()) # SUSKAICIUOJA KIEK ZMONIU YRA SALYJE

print(baltic.count()) #.count() suskaičiuos kiek yra įrašų grupės stulpeliuose:

print(baltic.min()) # .max() duos eilutę su maksimaliu, .min() su minimaliu rezultatais:

print(baltic.sum().loc['Lietuva']) # iš groupby objektų galime traukti reikšmes:

print(baltic.describe()) #.describe() metodas duoda pagrindinę informaciją apie lentelės duomenis:

print(baltic.describe().transpose()) #galime sukeisti stulpelius su eilutėmis su .transpose():
print(baltic.describe().transpose()['Estija']) # jeigu domina vieno kurio nors stulpelio statistika, galime ją ištraukti taip:


#--------------------------------=---------DATAFRAME JUNGIMAS---------------------------------------------------------
data_main = data[0:6] # SUKURIAMAS ANTRAS DATAFRAME
print(data_main)
print("-----------------------")
data_bottom = data[6:]
print(data_bottom)
#data_right = data_right1.reset_index().drop(columns='index') kad veiktu pridetu dataframe prie stulpelio (AXIS)
print("-----------------------")
merged = pd.concat([data_main, data_bottom]) #norėdami sujungti data_main su data_bottom naudosime .concat() metodą, viduje įrašydami lentelių, kurias jungsime sąrašą:
print(merged)

# NURODOM, KAD JUNGTU PRIE STULPELIO (AXIS = 1)
merged2 = pd.concat([data_main, data_bottom], axis=1) # KAD SUTVARKYTI TAI REIKIA NURESETINTI INDEXUS(Zr.ATSPAUSDINUS)
print(merged2)

lenkija = {'Šalis': ['Lenkija', 'Lenkija', 'Lenkija'],
           'Miestas':['Varšuva', 'Vroclavas', 'Gdanskas'],
          'Gyv': [1688, 638, 461]}
pl = pd.DataFrame(lenkija)

