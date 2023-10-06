# Parašykite generatorių, kuris kaskartą inicijuotas su funkcija next
# grąžintų sekantį porinį skaičių. Pirmas sk. 2, toliau 4 ir taip be pabaigos.

def poriniai_skaiciai():
    count = 2
    while True:
        yield count
        count += 2

generator = poriniai_skaiciai()

for x in range(20):
    print(next(generator))