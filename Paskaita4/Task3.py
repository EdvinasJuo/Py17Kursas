# Sukurti funkciją, kuri patikrintų,
# ar paduotas Lietuvos piliečio asmens kodas yra validus.
import datetime


# def validate_personal_code():
#     personal_code_input = input("Iveskite asmens koda: ")
#
#     if len(personal_code_input) == 11:
#         personal_code_list = list(map(int, str(personal_code_input[0:])))
#
#         if personal_code_list[0] >= 1 and personal_code_list[0] <= 6:
#             print("Asmens kodas validus")
#         else:
#             print("Asmens kodas nera validus")
#     else:
#         return "Kodas turi buti 11 skaitmenu"
#
# result = validate_personal_code()
# print(result)

def gender_selector():
    gender_input = input("Iveskite 1 - jeigu esate vyras. 2 - jeigu esate moteris: ")
    if gender_input == "1":
        return 1
    elif gender_input == "2":
        return 2
    else:
        return 0

gender_selector()

def birthday_year_male():
    birthday_male_input = int(input("Iveskite savo gimimo metus: "))

    if birthday_male_input >= 1801 and birthday_male_input <= 1900:
        return 1
    elif birthday_male_input >= 1901 and birthday_male_input <= 2000:
        return 3
    elif birthday_male_input >= 2001 and birthday_male_input <= 2100:
        return 5
    else:
        return 0

birthday_year_male()

def birthday_year_female():
    birthday_female_input = int(input("Iveskite savo gimimo metus: "))

    if birthday_female_input >= 1801 and birthday_female_input <= 1900:
        return 2
    elif birthday_female_input >= 1901 and birthday_female_input <= 2000:
        return 4
    elif birthday_female_input >= 2001 and birthday_female_input <= 2100:
        return 6
    else:
        return 0

def total_info():
    gender = gender_selector()
    male_birthday = birthday_year_male()
    female_birthday = birthday_year_female()
    if gender == 1 and male_birthday == 1:
        print("VYRAS, 19 amzius, test")

total_info()
