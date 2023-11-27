import pandas as pd

top = pd.read_csv('top50.csv', encoding='ISO-8859-1')

print(top.head().to_string())

# print(top['Genre'].unique()) # GRAZINS UNIKALIU ZANRU SARASA
#
# print(len(top['Genre'].unique())) # GRAZINS KIEK TURIM ZANRU
# print(top['Genre'].nunique()) # GRAZINS KIEK TURIM ZANRU KITAS BUDAS SU nunique()
#
# print(top['Genre'].value_counts()) # GRAZINA KIEK IR KOKIU ZANRU YRA
#
#
# #su .apply() galime maudoti ir savo funkcijas. Parašykime funkciją, kuri iš duotų sekundžių
# # skaičiaus išskirs minutes ir sekundes formatu mm:ss
# def minutes_seconds(s):
#     minutes = s // 60
#     seconds = s % 60
#     if len(str(seconds)) < 2:
#         return f'{minutes}:0{seconds}'
#     return f'{minutes}:{seconds}'
#
# #pritaikykime šią funkciją stulpeliui 'Length.':
# lenght_pretty = top['Length.'].apply(minutes_seconds).head()
# print(lenght_pretty)
#
# #Gavome seriją. Galime jos pagrindu jos pagrindu pakoreguoti senąjį arba sukurti naują stulpelį, pvz.:
# top['Length.Pretty'] = lenght_pretty
# print(top.to_string())
#
# #pavertėme 'Energy' stulpelio įvertinimus iš šimtabalės į dešimtbalę sistemą.
# top['Energy'].apply(lambda x: round(x/10)).head()
# print(lenght_pretty)


print(top.columns) # gaunam visus colums
print(top.index) # gaunam visus index
print(top.shape) # GAUNAM DYDI
print(top.sort_values('Track.Name').head()) # .sort_values surūšiuoja eilutes pagal nurodytą stulpelį:
print(top.isnull().to_string()) #.isnull() grąžina lentelę su boolean reikšmėmis kur True reiškia NaN.




#-------------------- IRASYMAS I CSV---------------------------------
# norėdami įrašyti duomenis į csv failą, darome taip:
# duomenys.to_csv('result.csv', index=False)


# ------------------------------------IRASYMAS IS HTML------------------------------

duomenys_html = pd.read_html('https://lt.wikipedia.org/wiki/Vilniaus_miesto_savivaldyb%C4%97')

print(duomenys_html)