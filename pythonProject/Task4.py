number1 = int(input("Iveskite pirmaji sveikaji skaiciu : "))
number2 = int(input("Iveskite antraji sveikaji skaiciu : "))
condition = str(input("Koki veiksma norite atlikti ? (+ , -, * , / "))

if condition == "+":
    print(f"{number1} + {number2} = {number1 + number2}")
elif condition == "-":
    print(f"{number1} - {number2} = {number1 - number2}")
elif condition == "*":
    print(f"{number1} * {number2} = {number1 * number2}")
elif condition == "/":
    print(f"{number1} / {number2} = {number1 / number2}")
else:
    print("Veiksmas negalimas")