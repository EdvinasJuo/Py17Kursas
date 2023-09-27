import random

random_number = random.randint(1, 10)

while True:
    for i in range(3):
        input_guess = int(input("Iveskite skaiciu tarp 1 - 20: "))
        if input_guess == random_number:
            print("Laimejai ! ")
        else:
            print(f"Neatspejai..")
    break

