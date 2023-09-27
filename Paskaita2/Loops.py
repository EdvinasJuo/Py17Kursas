import random
# FOR CIKLAS FOR CIKLAS FOR CIKLAS FOR CIKLAS

# Iteracija per zodyna
elements = [45, 152, 7, 58, 45, 89]

sum = 0

for element in elements:
    sum += element

print(sum)

# Iteracaija per sarasa
amzius = {"Rokas": 20, "Andrius": 34, "Laura": 25}

for key, values in amzius.items(): #Items grazina key ir value
    print(key, values)

# atspausdina kiek kartu nurodoma  su range(skaicius kiek kartu spausdinti) ir galiima susigeneruoti List'a

for element in range(6, 11, 2):
    print(element)

# WHILE CIKLAS WHILE CIKLAS WHILE CIKLAS

a = 5

while a < 100:
    print(a)
    a += 5


sarasas = range(0, 10, 2)

for one in sarasas:  #Pavyzdys su break, nutraukia visa cikla
    print(one)
    if one == 4:
        print("Skaicius 4 yra sarase")
        break


# pavyzdys su continue, nutraukia tik iteracija bet ne visa cikla

for one in sarasas:
    if one == 4:
        print("Skaicius 4 yra sarase")
        continue
    print(one)

# pavyzdys su else

for one in sarasas:
    if one == 10:
        print("Skaicius 10 yra sarase")
        break
    print(one)
else:           #Siuo atveju else ivykdomas kai ciklas praeina visas sekmingas be jokiu kliuciu
    print("Ciklas uzbaigtas")

# UZDUOTELE

numbers = [15, 2, 65, 84, 15, 231, 45, 19, 20, 17]
number = int(input("Iveskite ieskoma skaiciu: "))

for one in numbers:
    if number == one:
        print(f"Skaicius {number} rastas sarase")
        break
else:
    print("Skaicius nerastas")

print("Programos pabaiga")


# SUKURIAMAS TUSCIAS LIST I KURI PRIDEDAMI RANDOM 5 SKAICIAI KURIUOS NURODO RANGE FUNKCIJA
list = []

for c in range(5):
    a = random.randint(2, 15)
    print(a)
    list.append(a)
print(list)