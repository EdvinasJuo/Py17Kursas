# 1 Importuokite pandas ir numpy
import pandas as pd
import numpy as np

#2 Nuskaitykite į DF failą 'miestai isvalyti.csv',
print("----------2------------")
df = pd.read_csv('miestai_isvalyti.csv')
print(df)

# 3. Atspausdinkite pirmas penkias df eilutes
print("----------3------------")
print(df.head(5))

# 4. Padarykite, kad indeksas būtų stulpelis 'Miestas', ir kad šis pasikeitimas išliktų originale
print("----------4------------")
df.set_index('Miestas', inplace=True)
print(df)

# 5. Ištraukite reikšmę, kiek gyventojų gyveno Marijampolėje 1923m.
print("----------5------------")
print(df.loc['Marijampolė', '1923'])

# 6. Ištraukite stulpelį '1897', pirmas penkias eilutes.
print("----------6------------")
print(df.loc[['Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai', 'Panevėžys'], ['1897']])

# 7. Ištraukite stulpelius '2019', '1970', '1923', pirmas 10 eilučių.
print("----------7------------")
print(df[['2019', '1970', '1923']][:10])

# 8. Su .shape patikrinkite, kiek eilučių turi lentelė (pamenat numpy? :)
print("----------8------------")
print(df.shape)

# 9. pridėkite stulpelį su numeracija.
print("----------9------------")
df['nr'] = [i + 1 for i in range(103)]
print(df)

# 10. Ištraukite miestus nuo 30 iki 39 pozicijos.
print("----------10------------")
print(df.iloc[29:39])

# 11. Ištrinkite numeracijos stulpelį.
print("----------11------------")
print(df.drop('nr', axis=1, inplace=True))
print(df)

# 12. Kurių miestų dar nebuvo 1959m.?
print("----------12------------")
print(df[df['1959'] == 0])

# 13. Kokie miestai 1897 turėjo daugiau gyventojų, negu 2019?
print("----------13------------")
print(df[df['1897'] > df['2019']])

# 14. Kuriuose miestuose padaugėjo gyventojų nuo 2011 iki 2019?
print("----------14------------")
print(df[df['2011'] < df['2019']][['2019', '2011']])

# 15. Kuriuose miestuose gyventojų skaičius nuosekliai mažėjo nuo pat 1897m.?
print("----------15------------")
print(df[(df['1897'] > df['1923']) &
         (df['1923'] > df['1959']) &
         (df['1959'] > df['1970']) &
         (df['1970'] > df['1979']) &
         (df['1979'] > df['1989']) &
         (df['1989'] > df['2001']) &
         (df['2001'] > df['2011']) &
         (df['2011'] > df['2019'])])

# 16 Suraskite labiausiai procentaliai gyventojų skaičiumi padidėjusį ir sumažėjusį miestus nuo 1989m.
print("----------16------------")
print(df.idxmax)

procentai = ((df['2019'] - df['1989']) / df['1989']) * 100

max_miestas = procentai.idxmax()
max_procentai = int(procentai.max())
min_miestas = procentai.idxmin()
min_procentai = int(procentai.min())

print(f'{max_miestas} {max_procentai}%')
print(f'{min_miestas} {min_procentai}%')

# 17. Nuresetinkite indeksą
print("----------17------------")
df.reset_index(inplace=True)
print(df)