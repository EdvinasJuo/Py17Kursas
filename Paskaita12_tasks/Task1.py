import math
import logging

# Saugotų pranešimus į norimą failą
# • Saugotų INFO lygio žinutes
# • Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė
logging.basicConfig(level=logging.INFO, filename="task1.log", format="%(asctime)s:%(levelname)s:%(message)s")

# • Gražintų visų paduotų skaičių sumą (su *args argumentu)
def numbers_sum(*args):
    total = sum(args)
    return total

myArgs = (1, 4, 2, 5, 7, 8)
result = numbers_sum(*myArgs)
logging.info(f"Visu skaiciu {myArgs} suma: {result}")


# • Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
def root_of_number():
    return (math.sqrt(9))

result = root_of_number()
logging.info(f"Skaiciaus 9 saknis: {result}")

#  • Gražintų paduoto sakinio simbolių kiekį (su len())

def count_symbols():
    sentence = "Labas, kaip tau sekasi?"
    return len(sentence)

result = count_symbols()
logging.info(f"Simboliu sakinyje: {result}")

# • Gražintų rezultatą, skaičių x padalinus iš y
def dividing_result():
    x = 10
    y = 5
    result = x / y
    return result

result = dividing_result()
logging.info(f"Dalyba 10 / 5 = {result}")