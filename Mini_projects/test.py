# import math
#
# class Matematika:
#     def kvadratas(self, num1):
#         return num1 ** 2
#
#     def saknis(self, num1):
#         return num1 ** 0.5
#
# a = Matematika()
# print(int(a.kvadratas(4)))
# print(int(a.saknis(144)))

#
# class Zmogus:
#     def __init__(self, vardas, pavarde, amzius):
#         self.amzius = amzius
#         self.pavarde = pavarde
#         self.vardas = vardas
#
#     def informacija(self):
#         print(f'{self.amzius} {self.pavarde} {self.vardas}')
#
#     def padidinti_amziu(self):
#
#
# zmg1 = Zmogus('Mantas', 'Serapinas', 2000)
#
# Zmogus.informacija(zmg1)
#
# # print(zmg1.informacija())

def skaiciavimai(skaiciai):
    return sum(skaiciai)

skaiciai = int(input("Iveskite skaiciu atskirtu tarpais: ").split())

a = skaiciavimai(skaiciai)
print(a)