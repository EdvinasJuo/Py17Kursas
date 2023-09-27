# Sukurti norimą sąrašą ir žodyną ir juose:
# • Atspausdinti vieną norimą įrašą
# • Pridėti įrašą
# • Ištrinti įrašą
# • pakeisti įrašą
# Išbandyti kitas sąrašų ir žodynų funkcijas: clear(), index(), insert(), remove...

names = ["Jonas", "Paulius", "Lukas", "Edgaras", "Mantas", "Jonas", "Edvinas"]
print(names[6])

names.append("Ignas")
print(names)

names.pop(0)
print(names)

names[2] = "Kazimieras";
print(names)

print(len(names))

names.sort()
print(names)

index = names.index("Edvinas")
print(index)

names.clear()