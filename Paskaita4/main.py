# def pasisveikinti():
#     print("Sveiki visi")    CIA YRA BE PARAMETRU PAVYZDYS
#
# pasisveikinti()

# Su kintamuoju
# def pasisveikinti(vardas):
#     print(f"Sveikas {vardas}")
#
# pasisveikinti("Jonai")

# funkcija su skaiciavimais  TURI BUTI RETURN, KAD GRAZINTU O NE ATSPAUDINTU
# def kvadratu(number):
#     square = number ** 2
#     return square
#
# a = kvadratu(4)
#
# a += 10
#
# print(a)



# # Galima nurodyti iskarto reiksme siuo atveju number3 = 5
# def numbers_sum(number1, number2, number3 = 5):
#     sum = number1 + number2 + number3
#
#     return sum
#
# # print(numbers_sum(1, 3)) # Galima ir netureti reiksmiu, bet jas reik nurodyti funkcijos skliaustuose()
# print(numbers_sum(number1=20)) # Galima priskirti konkreciam parametrui


# * - neribotas kiekis reiksmiu/ siuo metu *args
# def sk_sum(*args):
#     print(args) #Tuple elementas kaip LIST tik jo negalima keist.
#     for number in args:
#         print(number)
#
# sk_sum(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#  ** - dvi zvaizgzdutes duoda dictionary su key ir values
# def spausdinti(**kwargs):
#     print(kwargs)
#     for key, values in kwargs.items():
#         print(key, values)
#
# spausdinti(metai=15, vardas="Jonas", ugis=1.75) # PAduodami key su values


# KITAS PAVYZDYS SU ** dictionary kai pridedama PAVARDE. Taip pat gali buti ir su *args!
def spausdinti(pavarde, **kwargs):
    print(pavarde)
    for key, values in kwargs.items():
        print(key, values)

spausdinti("Jonaitis", metai=15, vardas="Jonas", ugis=1.75) # PAduodami key su values