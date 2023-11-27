import numpy as np
import pandas as pd
# --------------------------------------
# labels = ['x', 'y', 'z']
# custom_data = [20, 30, 40]
# series = pd.Series(custom_data, labels) # SUKURIAMAS SERIES
# print(series)
#
# zodynas = {'a':10, 'b':10, 'c':30} # NURODOMI ISKART LABELS IR CUSTOM DATA. KEY PAIME UZ LABEL O VALUE UZ REIKSMES
# series2 = pd.Series(zodynas)
# print(series2)

# # --------------------------------------
# KAIP ISSITRAUKTI IS PANDOS
# serija = pd.Series([1,2,3,4,5], ['Vilnius', 'Kaunas', 'Klaipėda', 'Panevėžys', 'Šiauliai'])
# print(serija['Kaunas'])
#
# # SUDEDAMOS DVI SERIES
# serija2 = pd.Series([1,2,3,4,5], ['Vilnius', 'Kaunas', 'Lentvaris', 'Šiauliai', 'Klaipėda'])
# print(serija + serija2)


# ---------------------------------------------- DATA FRAME  --------------------------------------------------

np.random.seed(1)
random_data = np.random.rand(5,6)
df = pd.DataFrame(random_data,
                  ['a', 'b', 'c', 'd', 'e'],
                  ['U', 'V', 'W', 'X', 'Y', 'Z'])

print(type(df))
print("--------------")
# print(df[["U", "Y", "Z"]]) #PASIEMAM STULPELIUS
#
# df['naujas'] = [1, 2, 3, 4, 5] #Naujo stulpelio sukūrimas
# print(df)
# print("--------------")
# # print(df.drop('naujas', axis=1)) # ISTRINTI STULPELI ir grazina nauja DATAFRAME
# print(df.drop('naujas', axis=1, inplace=True)) #ATNAUJINS ORGINALU DATAFRAME naudojant inplace=True


print(df.loc['e']) # Istrauks visa eiluciu turini su loc.
print("--------------")
print(df.iloc[3]) # Istrauk visa eiluciu turini su iloc pagal indekso skaiciu. Siuo atveju D eilutes

print(df.loc[['a', 'd']]) #Istraukiama pora stulpeliu
print(df.loc['c', 'Z'])  # Istraukiama viena konkreti reiksme.

print(df.loc[['a', 'c'], ['U', 'V', 'Z']]) # istraukiam sesias reiksmes

#-----------ISTRAUKIA REIKSMES IS DATAFRAME PAGAL SALYGAS
print(df[df>0.4])
print("-------------------------------------")
print(df[df['W']>0.5]) # nurodom specifinio stulpelio pavadinima

print("-------------------------------------")
print(df[df['W']>0.5][['U', 'W', 'Z']]) # GALIMA Kombinuoti uzklausas.

print("-------------------------------------")
print(df[(df['U']>0.4) & (df['Z']<0.4)][['U', 'Z']])


#--------------------------------------------INDEXAI-------------------------------
print("-------------------------------------")
naujas_indeksas = 'Vilnius Kaunas Klaipėda Šiauliai Panevežys'.split()
df['Miestai'] = naujas_indeksas
print(df)
df.set_index('Miestai', inplace=True)
print(df)
print("-------------------------------------")
df.reset_index(inplace=True) # RESETINAM INDEXA Ir jis pastumia per stlpeli ir eilute i prieki
print(df)