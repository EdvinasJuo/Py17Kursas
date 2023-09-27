# Perdaryti 1 užduoties programą, kad:
# • Į šaknies funkciją padavus string tipo argumetrą, į log failą būtų išsaugoma išimties klaida su norimu tekstu
# • Į dalybos funkciją antrą argumentą padavus 0, į log failą būtų išsaugoma išimties klaida su norimu tekstu
# Patarimas: panaudoti try/except/else, logging.exception()

import math
import logging

logging.basicConfig(level=logging.INFO, filename="task2.log", format="%(asctime)s:%(levelname)s:%(message)s")
logging.basicConfig(level=logging.ERROR, filename="task2.log", format="%(asctime)s:%(levelname)s:%(message)s")

def numbers_sum(*args):
    total = sum(args)
    return total

myArgs = (1, 4, 2, 5, 7, 8)
result = numbers_sum(*myArgs)
logging.info(f"Visu skaiciu {myArgs} suma: {result}")

# • Į šaknies funkciją padavus string tipo argumetrą, į log failą būtų išsaugoma išimties klaida su norimu tekstu
def root_of_number():
    try:
        result = (math.sqrt(number))
    except TypeError:
        logging.exception(f"Ivestis turi buti sveikasis skaicius..")
    else:
        logging.info(f"Skaiciaus {number} saknis: {result}")

number = "asd"
result = root_of_number()

def count_symbols():
    sentence = "Labas, kaip tau sekasi?"
    return len(sentence)

result = count_symbols()
logging.info(f"Simboliu sakinyje: {result}")

def dividing_result():
    try:
        result = x / y
    except ZeroDivisionError:
        logging.exception("Dalyba is nulio negalima")
    else:
        logging.info(f"Dalyba 10 / 5 = {result}")
x = 10
y = 0

result = dividing_result()
