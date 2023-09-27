# Parašyti programą, kuri:
# • Leistų vartotojui įvesti skaičių.
# • Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# • Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
# Patarimas: Naudoti ciklą while, sąlygą if, break

positive_numbers = []

while True:
    input_number = int(input("Iveskite skaiciu: "))
    if input_number >= 0:
        positive_numbers.append(input_number)
    else:
        break

if positive_numbers:
    total_sum = sum(positive_numbers)
    print(f"Ivestu skaiciu suma yra: {total_sum}")
else:
    print("Neivestas teigiamas skaicius")