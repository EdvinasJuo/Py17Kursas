from IslaiduIrasas import *
from PajamuIrasas import *
class Biudzetas:
    def __init__(self):
        self.zurnalas = []
    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_informacija):
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamos)
    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidos = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidos)

    def gauti_balansa(self):
        pajamos = 0
        islaidos = 0

        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                pajamos += irasas.suma
            elif isinstance(irasas, IslaiduIrasas):
                islaidos += irasas.suma

        balansas = pajamos - islaidos
        print("Bendras balansas: ", balansas)
    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamu suma: {irasas.suma}. "
                      f"Siuntejas: {irasas.siuntejas}. "
                      f"Papildoma informacija: {irasas.papildoma_informacija}")
            elif isinstance(irasas, IslaiduIrasas):
                print(f"Islaidu suma: {irasas.suma}. "
                      f"Atsiskaitymo budas: {irasas.atsiskaitymo_budas}. "
                      f"Isigyta preke arba paslauga: {irasas.isigyta_preke_paslauga}")

biudzetas = Biudzetas()