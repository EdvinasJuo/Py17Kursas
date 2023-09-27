# # 1
# # Write a Python program to find those
# # numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
#
# numbers = []
#
# for number in range(1500, 2701):
#     if (number % 7 == 0) and (number % 5 == 0):
#         numbers.append(number)
#
# print(numbers)
#
# #2
# #  Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# # [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# # Expected Output :
# # 60°C is 140 in Fahrenheit
# # 45°F is 7 in Celsius
#
# temp_input = int(input("Iveskite temperatura: "))
#
# fahrenheit = round((temp_input * 9) / 5 + 32)
# celcius = round((temp_input - 32) * 5 / 9)
#
# print(f"{temp_input}°C yra {fahrenheit} Fahrenheitu\n"
#       f"{fahrenheit}°F yra {celcius} Celsijaus")
#
# #3
# # Write a Python program to guess a number between 1 and 9.
# # Note : User is prompted to enter a guess.
# # If the user guesses wrong then the prompt appears again until the guess is correct,
# # on successful guess, user will get a "Well guessed!" message, and the program will exit.
#
# import random
# random_number = random.randint(1, 9)
#
# while True:
#     input_number = int(input("Iveskite skaiciu nuo 1 iki 9: "))
#     if input_number == random_number:
#         print("Laimejote")
#         break
#     else:
#         print("Pralaimejote")

# 4. Write a Python program to construct the following pattern, using a nested for loop.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *

symbol = (input("Iveskite norima simboli: "))
num_rows = int(input("Iveskite kiek norite eiliu: "))

for i in range(num_rows):
    for j in range(i + 1):
        print(symbol, end="")
    print('')

for i in range(num_rows, 0, -1):
    for j in range(i):
        print(symbol, end="")
    print('')