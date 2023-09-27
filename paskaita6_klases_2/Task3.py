# Patobulinti 5 pamokos biudžeto programą:
# • Sukurti tėvinę klasę Irasas, kurioje būtų savybės suma , iš kurios klasės PajamuIrasas ir IslaiduIrasas paveldėtų
# visas savybes.
# • Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija, kurias vartotojas galėtų
# įrašyti.
# • Į klasę IslaiduIrasas papildomai pridėti savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias vartotojas
# galėtų įrašyti.
# • Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa ir gauti_ataskaita kad pasiėmus įrašą iš žurnalo,
# atpažintų, ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą) ir atitinkamai atliktų veiksmus.
# • Padaryti, kad vartotojui (per konsolę) būtų leidžiama įrašyti pajamų ir išlaidų įrašus, peržiūrėti balansą ir ataskaitą.

class Irasas:
    def __init__(self, suma):
        self.suma = suma

    def __str__(self):
        return f" {self.suma}"

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
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

while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n9 - išeiti iš programos"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Iveskite siunteja: ")
        papildoma_informacija = input("Iveskite papildoma informacija: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Iveskite atsiskaitymo buda: ")
        isigyta_preke_paslauga = input("Iveskite isigyta preke: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
    if pasirinkimas == 3:
        biudzetas.gauti_balansa()
    if pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
    if pasirinkimas == 9:
        print("Viso gero")
        break