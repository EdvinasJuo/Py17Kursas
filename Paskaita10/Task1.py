# Parašyti klasę "Namas", kuri turėtų savybę "plotas" ir "verte".
# Padaryti taip, kad savybė "verte" koreguojama tik
# įvedus skaičių. Programoje naudoti dekoratorių @property.

class Namas:
    def __init__(self, plotas, verte):
        self.plotas = plotas
        self.__verte = verte

    @property
    def verte(self):
        return self.__verte

    @verte.setter
    def verte(self, nauja_verte):
        if nauja_verte < 0:
            print("Verte negali buti minusine")
        else:
            self.__verte = nauja_verte


namas1 = Namas("150kv", 75000)
print(namas1.verte)

namas1.verte = 100000
print(namas1.verte)
