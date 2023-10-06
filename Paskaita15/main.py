import re

# pattern = re.compile(r"\+370\s\d{3}\s\d{5}") # PATTERN _ SABLONAS
#
# tekstas = "Pirmas telefono numeris yra +370 123 12321, antras +370 321 10101"
# res = pattern.search(tekstas) # PADUODAMAS I SEARCH FUNKCIJA ir randamas pirmas tel nr.
# print(res)
# print(res.group()) # grazina reiksmes kurios atititiko
#
# all_tlf = pattern.findall(tekstas) # FINDALL GRZINA VISAS REIKSMES IR SUDEDA I LISTA
# print(all_tlf)
#

#----------------------------------------------------------------------
# def split_names(name):
#     pattern = re.compile(r'^([A-Z]\w{1,3}.)\s([A-Z]\w+)\s([A-Z]\w+)$')
#     result = pattern.search(name)
#     if result:
#         print(f'Visa eilute: {result.group(0)}')
#         print(f'Kreipinys: {result.group(1)}')
#         print(f'Vardas: {result.group(2)}')
#         print(f'pavarde: {result.group(3)}')
#         print("-------------------------------")
#         print(result.group())
#         print(result.group())
#     else:
#         print("ivestis neatitinka sablono")
#
# split_names('Mr. Clint Eastwood')

#----------------------------------------------------------------------

# def validate_email(input):
#     emailregex = re.compile(r'^[azAZ0-9.%-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,6}$')
#     result = email_regex.search(input)
#     if result:
#         return True
#     return False


# card_number = "card1: 0452 6455 0004 4456, card2: 1234 4567 7891 1112"
# pattern = re.compile(r'\b(\d{4})\s\d{4}\s\d{4}\s\d{4}\b')
# res = pattern.sub('\g<1> **** **** ****', card_number)
# print(res)


# tekstas = """Trumpas tekstas
# apie beleka"""
# pattern = re.compile(r't\w+', re.IGNORECASE)  # GRAZINO ZODIS IS T RAIDES, nesvarbu ar didziojo ir mazoji
# res = pattern.findall(tekstas)
# print(res)



tekstas = """Trumpas tekstas
apie beleka"""

pattern = re.compile(r'^\w+')
res = pattern.findall(tekstas)

pattern2 = re.compile(r'^\w+', re.MULTILINE)  # MULTILINE KIEKVEINA EILUTE KAIP NAUJA EILUTE IR RANDA VISKA
res2 = pattern.findall(tekstas)

print(res)
print(res2)