# ITERATORIAI  SU ITERATORIUM VISADA NAUDOTI NEXT FUNKCIJA

# iteratorius = iter("Kėdė")
# print(type(iteratorius))
#
# print(next(iteratorius))
# a = 5
# b = a + 10
# c = a + b
# print(next(iteratorius))
# print(next(iteratorius))
# print(next(iteratorius))
# -------------------------------------------------------
# iteratorius = list(iter("Kėdė"))
# print(iteratorius[3])


# -------------------------------------------------------
# numeriai = [1, 2, 3]
# for num in numeriai:   # GAUNAM TAPATI VEIKSMA TIK SITAS ARCIAU KA MES JAU DAREM
#     print(num)
#
#
# iteratorius = iter(numeriai)
#
# while True:
#     try:
#         print(next(iteratorius))
#     except StopIteration:
#         break

# -------------------------------------------------------
# def iteruoklis(objektas, funk):
#     iteratoius = iter(objektas)
#     while True:
#         try:
#             item = next(iteratoius)
#         except StopIteration:
#             break
#         else:
#             funk(item)
#
#
# def kubu(x):
#     print(x ** 3)
#
# broliai = ['jurgis', 'antanas', 'aloyzas', 'martynas']
# numbers = [1,2,3,4]
# iteruoklis(broliai, print)
# iteruoklis(numbers, kubu)
# ------------------------------------------------------- GENERATORIAI========================================

# def skaiciuojam_iki(iki):
#     count = 1
#     while count <= iki:
#         yield count          #Kiekvienas next gauna kita yield
#         count += 1
#
# counter = list(skaiciuojam_iki(5)) #PAVERCIAM I LIST
#
# for x in counter:
#     print(x)



# GENERATOR EXPRESION
g = (num**2 for num in range(1, 50))
print(type(g))

print(next(g))
print(next(g))
print(next(g))
