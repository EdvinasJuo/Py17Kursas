# # KLASIU PAVELDEJIMAS !!!
# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def run(self):
#         print("Begu")
#
# class Cat(Animal):
#     def miaukseti(self):
#         print("Meow")
#
# class Dog(Animal):
#     def barking(self):
#         print("Au Au")
#
# class Vezlys(Animal):   # POLIMORFIZMAS kai perrsaomas metodas OVERRIDE
#     def begti(self):
#         super().run()  # super(). kreipiasi i tevine klase ir  gali issikviesti metodus is jos
#         print("Labai letai judu")
#
#
# arklys = Animal("Vezlius", "zalias")
# cat = Cat("Murkis", "juodas")
# dog = Dog("Amsius", "Rudas")
# vezlys = Vezlys("Letunas", "Zalias")
#
# arklys.run()
# cat.run()
# cat.miaukseti()
# dog.run()
# dog.barking()
# vezlys.begti()
#

# -------------------------------------------------------------------------
# class Tevas:
#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#
# class Vaikas(Tevas):
#     def __init__(self, vardas, pavarde, mokykla):
#         super().__init__(vardas, pavarde) # ISKVIECIA METODA IS TEVINES KLASES
#         self.mokykla = mokykla
#
# tevas = Tevas("Jonas", "Jonaitis")
# vaikas = Vaikas("Petras", "Jonaitis", "Varpo gimnazija")
#
# print(vaikas.mokykla)

# -------------------------------------------------------------------------
# PAVYZDYS KAIP GALIMA PANAUDOTI TEVINES IR VAIKINES KLASES

class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    pass

class IslaiduIrasas(Irasas):
    pass

biudzetas = []
irasas = PajamuIrasas(200)
irasas2 = IslaiduIrasas(300)

biudzetas.append(irasas)
biudzetas.append(irasas2)

for x in biudzetas:
    if isinstance(x, PajamuIrasas):
        print(x.suma, "Cia yra pajamos")
    elif isinstance(x, IslaiduIrasas):
        print(x.suma, "Cia yra islaidos")
