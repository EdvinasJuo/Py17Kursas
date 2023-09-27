# Sukurkite ir išsibandykite funkcijas, kurios:

# 1. Gražinti trijų paduotų skaičių sumą.
def adding_three_numbers(number1 = 15, number2 = 12, number3 = 5):
    sum = number1 + number2 + number3
    return sum

# 2. Gražintų paduoto sąrašo iš skaičių, sumą.
numbers_list = [1, 1, 2, 3, 3, 12, 52, 44, 85, 43]

def sum_of_numbers_list():
    total_sum = sum(numbers_list)
    return total_sum

# 3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
def find_highest_number(*args):
    highest_number = max(*args)
    return highest_number

# 4. Gražintų paduotą stringą atbulai.

sentence = "Python Programming 2 "
def reversed_word():
    return sentence[::-1]

# 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.

def count_string_info():
    count_words = len(sentence)
    find_uppercase_letters = sum(1 for uppercase in sentence if uppercase.isupper()) # bykdomas ciklas kuris praeina kiekviena sakinio simboli. Prideda kiekviena simboli +1 kuris yra didziaja raide
    find_lowercase_letters = sum(1 for lowercase in sentence if lowercase.islower())
    find_numbers = sum(map(str.isdigit, sentence))
    return (f"Simboliu kiekis: {count_words}, didziuju raidziu : {find_uppercase_letters}, "
            f"mazuju raidziu : {find_lowercase_letters}, skaiciu kiekis: {find_numbers}")


# 6. Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.

def unique_elements_of_list():
    # filter() tikrina kiekvieno saraso elementa ir issaugo i nauja list tik tada kai atitinka kriterijus.
    # siuo atveju numbers_list.count(x) == 1, imamas tik vienas skaicius
    unique_elements_list = list(filter(lambda x: numbers_list.count(x) == 1, numbers_list))
    return unique_elements_list

# 7. Gražintų, ar paduotas skaičius yra pirminis.

def prime_numbers(n):
    if n < 1:
        return "Nera pirminis"
    for i in range(2, n):
        if(n % i) == 0:
            return "Nera pirminis"
    return "Pirminis"

# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
def reversing_sentence():
    reversed_sentence = sentence[-2:] + sentence[:-2]
    return reversed_sentence

# 9. Gražina, ar paduoti metai yra keliamieji, ar ne.
def calculating_leap_year(years):
    if years % 4 == 0 and (years % 100 != 0 or years % 400 == 0):
        return "Keliamieji metai"
    else:
        return "Nekeliamieji metai"

# 10. Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.
import math
import datetime
def calculate_birthday_time(born):
    days_to_month = 0.03287671
    seconds_to_hours = 0.00027778
    seconds_to_minutes = 0.01666667

    birthday = datetime.datetime.strptime(born, "%Y-%m-%d %H:%M:%S")
    todays_date = datetime.datetime.now()
    years_difference = todays_date - birthday
    counting_years = int(years_difference.days / 365)
    counting_months = years_difference.days * days_to_month
    counting_days = years_difference.days
    counting_hours = years_difference.total_seconds() * seconds_to_hours
    counting_minutes = years_difference.total_seconds() * seconds_to_minutes
    counting_seconds = years_difference.total_seconds()

    return (f"You are {math.floor(counting_years)} years old. "
            f"You are {math.floor(counting_months)} months old. "
            f"You are {counting_days} days old. "
            f"You are {math.floor(counting_hours)} hours old. "
            f"You are {math.floor(counting_minutes)} minutes old. "
            f"You are {math.floor(counting_seconds)} seconds old. ")


print(f"Pridetu skaiciu suma = {adding_three_numbers()}")
print(f"Pridetu skaiciu suma is saraso = {sum_of_numbers_list()}")
print(f"Didziausias skaicius is *args = {find_highest_number(0, 15, 32, 45, 12)}")
print(f"Zodis atbulai = {reversed_word()}")
print(f"Simboliu kiekis: = {count_string_info()}")
print(f"Unikalus elementai naujam sarase: = {unique_elements_of_list()}")
print(f"Ar skaicius yra pirminis: = {prime_numbers(6)}")
print(f"Sakinys atbulai: = {reversing_sentence()}")
print(f"Ar keliamieji metai: = {calculating_leap_year(2004)}")
print(f"Gimtadienio informacija: = {calculate_birthday_time('2000-07-28 12:00:00')}")