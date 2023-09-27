number1 = int(input("Iveskite pirmaji sveikaji skaiciu: "))
number2 = float(input("Iveskite antraji skaiciu: "))

if number1 < number2:
    print(f"{number1} yra mazesnis uz {number2}")
elif number1 == number2:
    print(f"skaicius {number1} yra lygus skaiciui {number2}")
else:
    print(f"{number1} yra didesnis uz {number2}")