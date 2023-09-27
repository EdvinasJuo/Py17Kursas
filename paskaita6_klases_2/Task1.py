# Sukurti programą, kuri:
# • Turėtų klasę Automobilis
# • Automobilis turėtų savybes: metai, modelis, kuro_tipas
# • Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu, kurie atitinkamai atspausdintų „Važiuoja“,
# „Priparkuota“, „Degalai įpilti“
# • Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą
# • Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)
# • Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad jis atspausdintų „Baterija įkrauta“
# • Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“
# • Sukurti norimą Automobilio objektą
# • Sukurti norimą Elektromobilio objektą
# • Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu
# • Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu, vaziuoti_autonomiskai

class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(self.metai, self.modelis, self.kuro_tipas)

    def vaziuoti(self):
        print("Vaziuoti")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")

    def __str__(self):
        return f"Automobilio metai: {self.metai}, modelis: {self.modelis}, kuro tipas: {self.kuro_tipas}"


class Elektromobilis(Automobilis):
    def __init__(self, metai, modelis, kuro_tipas):
        super().__init__(metai, modelis, kuro_tipas)
    
    def pildyti_degalu(self):
        super().pildyti_degalu()
        print("Baterija ikrauta")

    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")


automobilis1 = Automobilis(2015, "Corola", "Dyzelis")
automobilis3 = Elektromobilis(2023, "Tesla Model Y", "Elektra")


print(automobilis3)
automobilis3.vaziuoti()
automobilis3.stoveti()
automobilis3.pildyti_degalu()
automobilis3.vaziuoti_autonomiskai()
