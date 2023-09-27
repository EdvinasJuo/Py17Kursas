class Kursas():
    def __init__(self, pavadinimas, destytojas, trukme):
        self.pavadinimas = pavadinimas
        self.destytojas = destytojas
        self.trukme = trukme

    def destyti(self):
        print("Vyksta mokymas!")

    def __str__(self):
        return (f"Kurso pavadinimas: {self.pavadinimas}."
              f" Destytojas: {self.destytojas}."
              f" Trukme savaitemis: {self.trukme}."
              f" Kursas: {self.destyti()}")