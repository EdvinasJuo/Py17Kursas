# DEKORATORIAI. VIENA FUNKCIJA GRAZINA KITA FUNKCIJA

# def return_string(some_string):
#     return  some_string
#
# def returns_reversed_string(string):
#     return string[::-1]
#
# def returns_upper_string(text, func):
#     if type(text) != str:
#         return 'input must be a type of string'
#     some_text = func(text)
#     return some_text.upper()
#
# print(returns_upper_string("Higher order functions!", return_string))
# print(returns_upper_string("Higher order functions!", returns_reversed_string))

# --------------------------------------------------------------------------------------------------------

# def upper_decorator(func):
#     def wrapper(our_text):
#         if type(our_text) != str:
#             return 'input must be a type of string'
#         some_text = func(our_text)
#         return some_text.upper()
#     return wrapper
#
# @upper_decorator
# def returns_string(some_string):
#     return some_string
#
# @upper_decorator
# def returns_reversed_string(string):
#     return string[::-1]
#
# print(returns_string("Decorated!"))
# print(returns_reversed_string("Decorated!"))


# --------------------------------------------------------------------------------------------------------
#
# def lyginis_nelyginis(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, *kwargs)
#         if (result % 2) != 0:
#             return result, "Nelyginis!"
#         return result, "Lyginis!"
#     return wrapper
#
# @lyginis_nelyginis
# def give_me_10():
#     return 10
#
# @lyginis_nelyginis
# def multiply(x, y):
#     return x * y
#
# @lyginis_nelyginis
# def sum_all(*args):
#     return sum(args)
#
# print(give_me_10())
# print(multiply(5,5))
# print(sum_all(10, 6, 7, 8))