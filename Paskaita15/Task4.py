# Parašykite funkciją, kuri į parametrus priimtų tekstą ir žodžių,
# kuriuos reikia jame išcenzūruoti sąrašą. Pvz, žodis "kvaraba" yra baisus keiksmažodis,
# ir mums reikia duotame tekste pakeisti k*****a. Pradėkite maždaug taip:
import re

def cenzura(tekstas, *keiksmai):
    pattern = re.compile(r'[A-Za-zĄČĘĖĮŠŲŪŽąčęėįšųūž]+')
    print(pattern.findall(tekstas))
    for x in keiksmai:
        tekstas = tekstas.replace(x, x[0] + '*' * (len(x) -1 ) + x[1])
    print(tekstas)

cenzura("Baisūs žodžiai, tokie kaip kvaraba, žaltys.. ", "kvaraba", "žaltys")



