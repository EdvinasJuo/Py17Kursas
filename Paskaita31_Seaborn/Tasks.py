import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg.head(10).to_string())
print(mpg.shape)

# #1 Atspausdinkite histogramą, kurioje matytųsi, kiek automobilių turi kokią akseleraciją.
# # Šioje ir kitose užduotyse žaiskite su stiliais ir spalvomis, taip, kaip jums patinka.
# print("--------------------1----------------------")
# print(sns.displot(mpg['acceleration']))
# plt.show()
#
# # 2 Atspausdinkite histogramą, kurioje matytųsi, kiek automobilių turi kokius variklio tūrius.
# print("--------------------2----------------------")
# print(sns.displot(mpg['displacement']))
# plt.show()

#3 Atspausdinkite histogramą, kurioje matytųsi, kokie yra cilindrų skaičiaus variantai.
# print("--------------------3----------------------")
# sns.set_style('darkgrid')
# custom_colors = ['blue', 'orange', 'green', 'red', 'purple']
# sns.countplot(x='cylinders', data=mpg, palette=custom_colors)
# plt.show()

# 4.Atspausdinkite histogramą, kurioje matytųsi, kiek yra pagaminimo metų variantų
# print("--------------------4----------------------")
# sns.countplot(x='model_year', data=mpg, palette='husl')
# plt.show()

# 5 Atspausdinkite histogramą, kurioje matytųsi, kiek automobilių lentelėje kokia šalis pagamino.\
# print("--------------------5----------------------")
# sns.countplot(x='origin', data=mpg, palette='mako')
# plt.show()

# 6 Atspausdinkite histogramą, kurioje matytųsi, koks kurioje šalyje pagamintų automobilių variklio tūrio vidurkis.
# print("--------------------6----------------------")
# sns.barplot(x='origin', y='displacement', data=mpg, ci=False, palette='cubehelix')
# plt.show()


#7 Atspausdinkite sklaidos diagramą, kurios x ašis būtų 'displacement', y - 'acceleration',
# taip pat kiekvienas taškas atspindėtų šalį gamintoją ir cilindrų skaičių
# print("--------------------7----------------------")
# sns.scatterplot(x='displacement', y='acceleration', data=mpg, hue='origin', size='cylinders', palette='husl')
# plt.show()


#8 Atspausdinkite visas įmanomas sklaidos diagramas lentelėje,
# kur pagal taško spalvą matytumėm šalį gamintoją. Kokias tendencijas galima aiškiai išskirti?
# print("--------------------8----------------------")
# sns.pairplot(mpg,hue='mpg', palette='husl')
# plt.show()

#9 Atspausdinkite stulpelinę diagramą, 'origin' x 'mpg'. Pabandykite interpretuoti rezultatą.
# print("--------------------9----------------------")
# sns.boxplot(x='origin', y='mpg', data=mpg, palette='rocket')
# plt.show()

# 10 Sukurkite koreliacijų matricą. Jos pagrindu atspausdinkite mozaikinę diagramą.
# matrix = mpg.corr(numeric_only=True)
# print(matrix.to_string())
# sns.heatmap(matrix, annot=True)
# plt.show()


# 11 Atspausdinkite sklaidos diagramų rinkinį, kuriame kiekviena lentelė
# pagal šalį rodytų 'acceleration' ir 'cylinders' sąntykį.
sns.relplot(data=mpg, x='acceleration', y='cylinders', hue='origin', col='origin')
plt.show()