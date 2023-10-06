# Parašykite generatoriaus funkciją, kuri atidarytų nurodytą failą, ir grąžintų po vieną eilutę
# (tiesiog yield'inti reikės ne skaičių o kitą duomenų tipą.). Reikės prisiminti darbą su failais :

def open_file():
    with open("info.txt", 'r') as failas:
        for line in failas:
            yield line

generator = open_file()

count = 1
for line in generator:
    print(f'{count}. {line}')
    count += 1
