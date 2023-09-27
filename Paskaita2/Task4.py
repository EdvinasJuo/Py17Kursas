# Sukurti programą, kuri:
# • Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# • Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# • Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break

import random

numbers = []

for number in range(3):
    random_numbers = random.randint(1,6)
    numbers.append(random_numbers)

for number in numbers:
    print(number)

if number != 5:
    print("WINNER")
else:
    print("LOOSER")