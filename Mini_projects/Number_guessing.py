import random

random_number = random.randint(1, 5)

while True:
    for i in range(3):
        input_guess = int(input("Iveskite skaiciu tarp 1 - 5: "))
        if input_guess == random_number:
            print("Laimejai ! ")
            break
        else:
            print(f"Neatspejai..")
    break

