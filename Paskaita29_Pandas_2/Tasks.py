import numpy as np
import pandas as pd

#  1 Sulipdykite iš 4 fragmentų vieną lentelę:
top_left = pd.read_csv('top1-25-1.csv')
top_right = pd.read_csv('top1-25-2.csv')
bottom_left = pd.read_csv('top26-50-1.csv')
bottom_right = pd.read_csv('top26-50-2.csv')

bot_df = pd.concat([bottom_left, bottom_right], axis=1)
top_df = pd.merge(top_left, top_right, on=['Track.Name', 'Popularity'])
all_data = pd.concat([top_df, bot_df])
print(all_data.to_string())

# 2 Sutvarkykite indeksą - padarykite, kad prasidėtų nuo 1.
print('-----------------------2-------------------------')
original_data = all_data.reset_index().drop(columns='index')
original_data.index = original_data.index + 1
print(original_data.to_string())

# 3 Sukurkite grupavimo pagal žanrą objektą.
print('-----------------------3-------------------------')
genre = original_data.groupby('Genre')
print(genre)

# 4 kokie žanrai lentelėje pasitaiko daugiau negu 3 kartus?
print('-----------------------4-------------------------')
same_genre = original_data['Genre'].value_counts()
more_than_3 = same_genre[same_genre > 3]
print(more_than_3)

# 5 Koks žanras pats populiariausias? Koks mažiausiai populiarus?
print('-----------------------5-------------------------')
most_popular = original_data['Popularity'].max()
most_popular_genre = original_data.loc[original_data['Popularity'].idxmax(), 'Genre']
least_popular = original_data['Popularity'].min()
least_popular_genre = original_data.loc[original_data['Popularity'].idxmin(), 'Genre']
print(f'{most_popular_genre} {most_popular}')
print(f'{least_popular_genre} {least_popular}')

# 6. Sukurkite lentelę, kurioje matytųsi, koks žanras turi aukščiausią vidurkį kiekviename indikatoriuje, bei pats vidurkis.
print('-----------------------6-------------------------')
columns = all_data.columns[3:]

indicators = []
genres = []
averages = []

for indicator in columns:
    max_genre = all_data.groupby('Genre')[indicator].mean().idxmax()
    max_value = all_data.groupby('Genre')[indicator].mean().max()
    indicators.append(indicator)
    genres.append(max_genre)
    averages.append(max_value)

result = pd.DataFrame({'Indikatorius': indicators, 'Žanras': genres, 'Balai': averages})
print(result)

#7 Grįžkime prie sulipdytos lentelės. Ištraukite visas eilutes, kurios turi NaN reikšmių
print('-----------------------7-------------------------')
x = all_data[all_data['Genre'].isnull() | all_data['Popularity'].isnull()]
print(x.to_string())

# 8 Stulpelyje 'Genre' NaN reikšmes pakeiskite į 'pop'
print('-----------------------8-------------------------')
change_to_pop = all_data['Genre'].fillna('pop')
print(change_to_pop)

# 9 Stulpelyje 'Popularity' trūkstamas reikšmes pakeiskite į stulpelio vidurkį
change_popularity = all_data['Popularity'].fillna(value=all_data['Popularity'].mean())
print(change_popularity)