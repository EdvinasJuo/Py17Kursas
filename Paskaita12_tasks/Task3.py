# Perdaryti 2 užduoties programą, kad:
# • Būtų sukurtas savo logeris, kuris fikstuotus visus anksčiau aprašytus pranešimus
# • Sukurtas logeris ne tik išsaugotų pranešimus faile, bet ir atvaizduotų juos konsolėje

import logging
import math

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("Task3.log")
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def numbers_sum(*args):
    total = sum(args)
    return total

myArgs = (1, 4, 2, 5, 7, 8)
result = numbers_sum(*myArgs)
logger.info(f"Visu skaiciu {myArgs} suma: {result}")

# • Į šaknies funkciją padavus string tipo argumetrą, į log failą būtų išsaugoma išimties klaida su norimu tekstu
def root_of_number():
    try:
        result = (math.sqrt(number))
    except TypeError:
        logger.exception(f"Ivestis turi buti sveikasis skaicius..")
    else:
        logger.info(f"Skaiciaus {number} saknis: {result}")

number = 9
result = root_of_number()

def count_symbols():
    sentence = "Labas, kaip tau sekasi?"
    return len(sentence)

symbols_result = count_symbols()
logger.info(f"Simboliu sakinyje: {symbols_result}")

def dividing_result():
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Dalyba is nulio negalima")
    else:
        logger.info(f"Dalyba 10 / 5 = {result}")
x = 10
y = 0

div_result = dividing_result()