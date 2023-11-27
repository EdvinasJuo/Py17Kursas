# # KONSTANTOS
#
# PI = 3.14
# GRAVITACIJA = 9.8  # IS DIDZIUJU RAIDZIU RASOMOS KONSTANTOS KURIU PROGARMOJE NESIKEICIA REIKSME
#
# print(PI)

from enum import Enum

# class Savaitė(Enum):
#     PIRMADIENIS = 1
#     ANTRADIENIS = 2
#     TRECIADIENIS = 3
#     KETVIRTADIENIS = 4
#     PENKTADIENIS = 5
#     ŠEŠTADIENIS = 6
#     SEKMADIENIS = 7

# diena = Savaitė.SEKMADIENIS
# print(diena)
# print(diena.name)
# print(diena.value)

# print(list(Savaitė))
#
# for day in Savaitė:
#     print(day.name, day.value)

# for key, value in Savaitė.__members__.items():
#     print(key, value.value)

#----------------------------------------------------------------------------
# class Menuo(Enum):
#     SAUSIS = "Sausis", 1
#     VASARIS = "Vasaris", 2
#     KOVAS = "Kovas", 3
#     BALANDIS = "Balandis", 4
#     GEGUŽĖ = "Gegužė", 5
#     BIRŽELIS = "Birželis", 6
#     LIEPA = "Liepa", 7
#     RUGPJŪTIS = "Rugpjūtis", 8
#     RUGSĖJIS = "Rugsėjis", 9
#     SPALIS = "Spalis", 10
#     LAPKRITIS = "Lapkritis", 11
#     GRUODIS = "Gruodis", 12
#
# menuo = Menuo.BIRŽELIS
# print(menuo)
# print(menuo.name)
# print(menuo.value) ## GRAZINA TUPLE ELEMENTA
# print(menuo.value[0])
# print(menuo.value[1])

#----------------------------------------------------------------------------

# from enum import Enum, auto
# class Spalva(Enum):
#
#     JUODA = auto()
#     BALTA = auto()
#     RAUDONA = auto()
#     ŽALIA = auto()
#     GELTONA = auto()
#     MĖLYNA = auto()
#
# spalva = Spalva.RAUDONA
# print(spalva)
# print(spalva.name)
# print(spalva.value)


#----------------------------------------------------------------------------
#
# from enum import Enum, auto, unique
#
# @unique
# class Neunikalus(Enum):
#     VIENAS = 1
#     DU = 2
#     DARDU = 2
#
# print(2)


#----------------------------------------------------------------------------
class Veiksmas(Enum):
    ĮVESTI = 1
    ATSPAUSDINTI = 2
    IŠEITI = 3


def atlikti_veiksma(veiksmas: Veiksmas):
    print(f"Veiksmas įvykdytas: {veiksmas.name}")


# Įvedimas ir funkcijos kvietimas:
for veiksmas in Veiksmas:
    print(f"{veiksmas.value} - {veiksmas.name}")

ivesta = int(input("Pasirinkite veiksmą: "))
atlikti_veiksma(Veiksmas(ivesta))