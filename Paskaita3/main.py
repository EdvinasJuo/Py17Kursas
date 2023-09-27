sarasas = ["Vienas", "Du", 1.5, 2, 3, 5, 4, True]

suma = 0
# Is saraso su type issirenkam teisinga duomenu tipa, siuo atveju INT
for x in sarasas:
    if type(x) is int or type(x) is float:
        suma += x

print(suma)