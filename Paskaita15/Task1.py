import re

# parašykite funkciją, kuri įvestą datą (formatas dd.mm.yyyy) keistų į yyyy mm dd.
# Dėl datų logikos nesirūpinkite, dirbame grynai su tekstu.

def change_data_format(date):
    pattern = re.compile(r'^(?P<dd>\d{2})\.(?P<mm>\d{2})\.(?P<yyyy>\d{4})')
    result = pattern.search(date)
    if result:
        print(f'Visa eilute: {result.group(0)}')
        print(f'Pakeistas formatas: {result.group("yyyy")} {result.group("mm")} {result.group("dd")}')
    else:
        print("Ivestis neatitinka sablono")

change_data_format('12.25.2020')