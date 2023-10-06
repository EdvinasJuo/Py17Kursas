# Parašykite dekoratorių kuris riboja parametrų kiekį (tarkime, ne daugiau negu 2 parametrai funkcijai)

def max_two_parameters(func):
    def wrapper(*args):
        if len(args) <= 2:
            return func(*args)
        else:
            return ValueError("Funkcija gali tureti ne daugiau kaip 2 parametrus")
    return wrapper

@max_two_parameters
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(2,6,6))