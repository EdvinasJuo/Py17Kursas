# Parašykite dekoratorių, kuris atideda funkcijos vykdymą 3s
import time

def delay(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)
    return wrapper

@delay
def max_two_parameters(func):
    def wrapper(*args):
        if len(args) <= 2:
            return func(*args)
        else:
            return ValueError("Funkcija gali tureti ne daugiau kaip 2 parametrus")
    return wrapper

@max_two_parameters
@delay
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(2,5, 8))