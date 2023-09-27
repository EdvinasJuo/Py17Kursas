# def funkcija (sk1, sk2):
#     """
#     Funkcija grazina dvieju skaiciu suma
#     :param sk1: pirmas sveikas skaicius
#     :param sk2: antras sveikas skaicius
#     :return: dvieju skaiciu suma
#     """
#     suma = sk1 + sk2
#     return suma
#
# funkcija()

#       ANONIMINES ARBA LAMBDA FUNKCIJOS KURIOS NAUDOJAMOS VIENA KARTA!!!!!

def kvadratu(x):
    return x ** 2  #VIETOJ SITOS FUNKCIJOS GALIMA PARASYTI LAMBDA

kv = lambda x: x ** 2  #LAMBDA EKSRESIJA
print(kv(2))
ž
# KITAS PAVYZDYS
square_sum = lambda x, y, z: x ** 2 + y + z
print(square_sum(2, 1, 10))


sarasas = [2, 4, 5, 6, 7, 5, 8, 10, 2]

sarasas2 = map(lambda x: x ** 2, sarasas) # SUKURIA KITA LISTA SU PAKELTAIS SKAICIAIS
for x in sarasas2:
    print(x)


# DAR KITAS PAVYZDYS

# daugyba_is_saves = [lambda i = skaicius: i * i for skaicius in range(1, 6)]
# for vienas in daugyba_is_saves:
#     print(vienas())

keliamieji = [lambda i = metai: i for metai in range(1900,2021) if(metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0)]

for v in keliamieji:
    print(v())