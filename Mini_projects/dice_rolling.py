import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

if dice1 == dice2:
    print(f"Pirmas kauliukas: {dice1}")
    print(f"Antras kauliukas: {dice2}")
    print(f"Kauliuko suma: {dice1 + dice2}")
    print("Turite antra metima")
else:
    print(f"Pirmas kauliukas: {dice1}")
    print(f"Antras kauliukas: {dice2}")
    print(f"Kauliuko suma: {dice1 + dice2}")