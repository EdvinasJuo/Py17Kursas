# Sukurti naują projektą Mokymas
# • Projekto kataloge sukurti katalogą modules
# • Kataloge modules sukurti failą kursas.py
# • Faile kursas.py sukurti objekto klasę Kursas, kuri turėtų savybes pavadinimas, destytojas, trukme, taip pat metodą
# destyti(), kuris spausdintų „Vyksta mokymas!“
# • Kataloge modules sukurti antrą failą python_kursas.py
# • Faile python_kursas.py sukurti objekto klasę PythonKursas, kuri paveldėtų viską iš klasės Kursas, bei perrašytų
# metodą destyti() taip, kad jis spausdintų „Vyksta programavimas!“
# • Pagrindiniame projekto kataloge sukurti failą main.py
# • Faile main.py importuoti PythonKursas modulį (failą)
# • Faile main.py inicijuoti Kursas objektą su norimomis savybėmis
# • Faile main.py inicijuoti PythonKursas objektą su norimomis savybėmis
# • Paleisti abiejų objektų metodą destyti()

from modules.python_kursas import *

mokymas1 = Kursas("UI/UX mokymai", "Juozas Juozaitis", 5)
mokymas2 = PythonKursas("Python programavimas", "Petras Petraitis", 9)

mokymas1.destyti()
mokymas2.destyti()

# print(mokymas1)
# print(mokymas2)

