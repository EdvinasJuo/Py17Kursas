class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = atlyginimas

        # get su property
    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def set_atlyginimas(self, naujas_atlyginimas):
        if naujas_atlyginimas < 0:
            print("Atlyginimas negali buti neigiamas")
        else:
            self.__atlyginimas = naujas_atlyginimas

    # def get_atlyginimas(self):
    #     return self.__atlyginimas            Getteris


domas = Darbuotojas("Domas", "Rutkauskas", 1200)
# domas.set_atlyginimas(1500)   # Setteris  nustato
# print(domas.get_atlyginimas()) # Getteris    gauna
print(domas.atlyginimas)
domas.atlyginimas = 1500
print(domas.atlyginimas)