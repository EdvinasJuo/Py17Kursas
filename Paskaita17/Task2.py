# Parašykite generatorų , kuris kas kartą generuotų po vieną Fibonačio sekos skaičių.
# (Seka prasideda šiais skaičiais: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233.
# Kiekvienas šios sekos skaičius lygus dviejų prieš jį einančių skaičių sumai, daugiau google:)

def fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

generator = fibonacci_numbers()

count = 1
for x in range(15):
    print(f"{count}. {next(generator)}")
    count += 1