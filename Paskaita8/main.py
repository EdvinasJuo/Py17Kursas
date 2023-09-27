# ------------------------------------- TRIUKAI SU SARASAIS------------------------------
# sarasas = [4, 2, 3, 22, 11]
# # 1 VARIANTAS
# sarasas_2 = []
#
# for x in sarasas:
#     sarasas_2.append(x ** 2)
# print(sarasas_2)
#
# #2 CARIANTAS SU MAP FUNKCIJA
#
# naujas = list(map(lambda x: x**2, sarasas))   # PIRMOJ VIETOJ FUNKCIJA, ANTROJ PADUODAMAS ELEMENTAS SIUO METU sarasas
# print(naujas)

# PAVYZDYS SU DATA, GRAZINA METUS, MENESIU, DATAS ATSKIRTAS
# data = "2001-11-15"
#
# y, m, d, = map(int, data.split("-"))  # SU SPLIT GAUNAM LIST
# print(y)
# print(m) # SU SITAIS KINTAMAISIAIS GALIM DARYT KA NORIM. PVZ KEISTI
# print(d)

# PVZ KAIP PASIVERSTI I FLOAT
# skaiciai = "4, 3, 2, 1"
# pirmas, antras, trecias, ketvirtas = map(float, skaiciai.split(","))  # SU SPLIT GAUNAM LIST
# print(pirmas)
# print(antras)
# print(trecias)
# print(ketvirtas)


# PVZ SU FILTER
# sarasas = [10, 9, 8, 7, 6, 4, 3, 2, 1]
# # PIRMAS VARIANTAS
# def daugiau_nei_du(sarasas_lokalus):
#     sarasas2 = []
#     for element in sarasas_lokalus:
#         if element > 2:
#             sarasas2.append(element)
#     return sarasas2
#
# print(daugiau_nei_du(sarasas))
#
# # ANTRAS VARIANTAS SU FILTER
# naujas = filter(lambda x: x > 2, sarasas) # SU FILTER GAUNAME BOOLEAN. TRUE ARBA FALSE. PVZ JEIGU TRUE SIUO ATVEJU GAUNAM I FILTER IR JI KONVERTUOJAM I LISTA
# print(naujas)
# print(list(naujas))


# # PVZ KURIE DALINASI IS DVIEJU
# sarasas = [10, 9, 8, 7, 6, 4, 3, 2, 1]
# naujas = filter(lambda x: x % 2 == 0, sarasas)
# print(list(naujas))

# PVZ SU KELIAMAISIAS METAIS
# import calendar
#
# metai = list(range(1900, 2150))
#
# naujas = filter(calendar.isleap, metai)
# print(list(naujas))


#PVZ SU FUNCTOOLS
# import functools
#
# sarasas = [4, 3, 2, 1]
#
# naujas = functools.reduce(lambda x,y: x + y, sarasas)
# print(naujas)


# SURANDA SUM, MIN, MAX,

# sarasas = [4, 3, 2, 1]
# string = "Labas"
# print(sum(sarasas))
# print(min(sarasas)) # TAIP PAT VEIKIA IR SU STRINGU
# print(max(sarasas)) # TAIP PAT VEIKIA IR SU STRINGU


# # STATISTICS BIBLIOTEKA
# import statistics
#
# sarasas = [4, 3, 2, 1, 5]
# print(statistics.mean(sarasas))
# print(statistics.median(sarasas))


# list comprehension
# sarasas = [4, 3, 2, 1]
#
# naujas = [x ** 2 for x in sarasas] # PADARO IS VIENO SARASO I KITA
# print(naujas)
#
# # PVZ KAD VISI SKAICIAU BUTU DAUGIAU UZ 2
# naujas2 = [x for x in sarasas if x > 2]
# print(naujas2)
#
# # PVZ KAIP SURAST LYGINIUS SKAICIUS
# sarasas2 = list(range(20))
# lyginiai = [x for x in sarasas2 if x % 2 == 0]
# print(lyginiai)

# PVZ KAIP PRAFILTRUOTI
# sarasas = [4, 3.0, "Labas", True, 20, 111]
#
# int_kiekis = sum(type(x) is int for x in sarasas)
# # PAVIRTO I [True, False, False, False, True, True] SUSKAICIAVO TRUE REIKSMES
# print(int_kiekis)
# string_kiekis = sum(type(x) is str for x in sarasas)
# print(string_kiekis)


# LIST RIKIAVIMAS
# sarasas = [2, 5, 4, 6, 7, 5, 62, 12, 0, 11]
# sarasas.sort() # NUO MAZIAUSIOS IKI DIDZIAUSIOS
# print(sarasas)
# sarasas.sort(reverse=True) # NUO DIDZIAUSIOS IKI MAZIAUSIOS
# print(sarasas)
#
# naujas = sorted(sarasas) # PAIMA LISTA, JI NUSKAITO, SURUSIUOJA IR PRISKIRIA KITAM KINTAMAJAM
# print(naujas)
#
# naujas2 = sorted(sarasas, reverse=True) # NUO MAX IKI MIN
# print(naujas2)


# DICTIONARY RIKIAVIMAS
# zodynas = {"Vardas": "Jonas", "Pavarde": "Jonaitis", "Amzius": 20}
#
# naujas = sorted(zodynas, reverse=True) # RIKIUOJA PAGAL KEY REIKSMES
# print(naujas)

# sarasas = [-5, -10, 5, 0, 2, 1]
# # print(abs(-5))  # GRAZINA ABSOLIUTINE REIKSME (BE ZENKLO)
# naujas = sorted(sarasas, key=abs, reverse=True)
# print(naujas)


# KLASIU RIKIAVIMAS

import operator

class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas

    def __repr__(self):
        return f"{self.vardas} {self.pavarde} - {self.atlyginimas}"

d1 = Darbuotojas("Tadas", "Madaitis", 1000)
d2 = Darbuotojas("Jonas", "Jonaitis", 1200)
d3 = Darbuotojas("Paulius", "Baulauskas", 800)

darbuotojai = [d1, d2, d3]
print(darbuotojai)

# SURUSIUOTI DARBUOTOJUS PAGAL VARDA
def rusiavimas(darbuotojas):
    return darbuotojas.vardas

sort1 = sorted(darbuotojai, key=rusiavimas)
print(sort1)

sort2 = sorted(darbuotojai, key=lambda e: e.atlyginimas)
print(sort2)

sort3 = sorted(darbuotojai, key = operator.attrgetter("pavarde"))
print(sort3)