# Sukurti funkciją, kuri grąžintų True reikšmę, jei įvesto skaičiaus pirma skaitmenų pusė
# yra lygi antrąjai, priešingu atveju grąžintų False.
def first_half_digits_equals_to_second():
    input_number = input("Iveskite sveikaji skaiciu: ")
    input_numbers_digits_sum = 0

    for digit in input_number:
        if digit.isdigit():
            input_numbers_digits_sum += int(digit)

    if input_numbers_digits_sum % 2 == 0:
        first_half = input_number[0:len(input_number) // 2]
        second_half = input_number[-(len(input_number) // 2):]
        if first_half == second_half:
            return True
        else:
            return False
    else:
        print("Ivesto skaiciaus skaitmenu suma nera lygine, todel palyginti ar pirma su antra pusemis yra vienodos.")


# result = first_half_digits_equals_to_second()
# print(result)

# 2. Parašyti funkciją, kuri grąžintų, kiekvieno elemento gretimą skaičių. Pvz:
# Input: 5678
# Output: 5 – 46, 6 – 57, 7 – 68, 8 - 79

def returns_number_neighbour():
    input_number2 = input("Iveskite sveikaji skaiciu: ")
    numbers_list = list(map(int, str(input_number2[0:])))

    for number in range(len(numbers_list)):
        current_number = numbers_list[number]

        before = numbers_list[number - 1] if number > 0 else numbers_list[0]
        after = numbers_list[number + 1] if number < len(numbers_list) - 1 else numbers_list[-1]

        print(f"{current_number} - {before}{after}", end=", ")


returns_number_neighbour()