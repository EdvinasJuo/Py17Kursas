from modules.kursas import *

class PythonKursas(Kursas):
    def __init__(self, pavadinimas, destytojas, trukme):
        super().__init__(pavadinimas, destytojas, trukme)

    def destyti(self):
        print("Vyksta programavimas!")

    def __str__(self):
        return (f"Kurso pavadinimas: {self.pavadinimas}."
              f" Destytojas: {self.destytojas}."
              f" Trukme savaitemis: {self.trukme}."
              f" Kursas: {self.destyti()}")