#                                      OBJEKTINIS PROGRAMAVIMAS
#                                      OBJEKTINIS PROGRAMAVIMAS
#                                      OBJEKTINIS PROGRAMAVIMAS
class Kate:
    def __init__(self, spalva="juoda", kojos=4): # __INIT__ METODAS YRA KONSTRUKTORIUS. (metodas taspats kaip funkcija, taciau metodas priklauso objektui.
        self.spalva = spalva  #Sukuriamas naujas klases kintamasis vadinamas klases savybe. angl. Property
        self.kojos = kojos    #Sukuriamas naujas klases kintamasis vadinamas klases savybe. angl. Property

    # KLASES METODAS !
    def miaukseti(self):
        print("Miau")

    def _judinti_kojas(self):
        print("judinu kojas")

    def _ziureti_kur_begi(self):
        pass

    def begti(self):
        self._judinti_kojas()                    #siuo self. kreipiasi tiesiai i metoda
        self._ziureti_kur_begi()
        print("Begu")

    def __str__(self):
        return f"Koju skaicius: {self.kojos}, kaciuko spalva: {self.spalva}"

    def __repr__(self):
        return f"Cia buvo padaryta su REPR metodu - Koju skaicius: {self.kojos}, kaciuko spalva: {self.spalva}"

# kate1 = Kate()
# kate2 = Kate("juoda", 5)
# kate3 = Kate("zalia", 3)
#
# # kates = []
# #
# # kates.append(kate1)
# # kates.append(kate2)
# # kates.append(kate3)
# #
# # for kate in kates:
# #     print(kate.spalva)

kates = []

while True:
    pasirinkimas = int(input("1 - Iveskite kate\n2 - Perziureti kates\n3 - Iseiti is programos"))
    if pasirinkimas == 1:
        spalva = input("Iveskite kates spalva: ")
        kojos = int(input("Iveskite kates koju skaiciu: "))
        kate = Kate(spalva, kojos)
        kates.append(kate)
    if pasirinkimas == 2:
        for kate in kates:
            print(f"Kates spalva: {kate.spalva}. Koju skaicius: {kate.kojos}")
    if pasirinkimas == 3:
        print("Viso gero")
        break

print(kates)