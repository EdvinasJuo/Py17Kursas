# Sukurti programą, kuri:
# • Leistų vartotojui įvesti metus
# • Atspausdintų „Keliamieji metai“, jei taip yra
# • Atspausdintų „Nekeliamieji metai“, jei taip yra
# Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų

years = int(input("Iveskite metus: "))

if years % 4 == 0 and (years % 100 != 0 or years % 400 == 0):
    print("Keliamieji metai")
else:
    print("Nekeliamieji metai")
