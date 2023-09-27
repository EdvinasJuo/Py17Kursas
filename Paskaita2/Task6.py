# Perdaryti 5 užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų

years = []

for year in range(1900, 2101):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        years.append(year)

print(years)