# Sukurti minibiudžeto programą, kuri:
# • Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
# • Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
# • Atvaizduotų jau įvestas pajamas ir išlaidas
# • Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)
# Patarimas:
import pickle
class Biudzetas:
    def __init__(self):
        self.zurnalas = self._nuskaityti_zurnala() # atkuriama informacija is ankstesnio issaugoto pickle failo

    def _issaugoti_zurnala(self):
        with open("biudzetas.pkl", "wb") as pickle_out:
            pickle.dump(self.zurnalas, pickle_out)
    def _nuskaityti_zurnala(self):
        with open("biudzetas.pkl", "rb") as pickle_in:
            return pickle.load(pickle_in)

    def prideti_irasa(self, suma):
        if suma < 0:
            tipas = "Islaidos"
            irasas = suma * -1
        else:
            tipas = "Pajamos"
            irasas = suma

        print(f"{tipas}: {irasas}")

        self.zurnalas.append({"tipas": tipas, "suma": irasas})
        self._issaugoti_zurnala()

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            balansas += irasas['suma']
        print(f"Bendras balansas: {balansas}")

    def atvaizduoti_irasus(self):
        for irasas in self.zurnalas:
            print(f"{irasas['tipas']}: {irasas['suma']}")

biudzetas = Biudzetas()

while True:
    try:
        pasirinkimas = int(input("1 - įvesti pajamas, "
                                 "\n2 - įvesti išlaidas, "
                                 "\n3 - gauti balansą, "
                                 "\n4 - parodyti ataskaitą, "
                                 "\n9- issaugoti ir uzdaryti programa"))
        if pasirinkimas == 1:
            suma = float(input("Iveskite pajamu suma: "))
            biudzetas.prideti_irasa(suma)
        elif pasirinkimas == 2:
            suma = float(input("Iveskite islaidu suma su - zenklu: "))
            biudzetas.prideti_irasa(suma)
        elif pasirinkimas == 3:
            biudzetas.gauti_balansa()
        elif pasirinkimas == 4:
            biudzetas.atvaizduoti_irasus()
        elif pasirinkimas == 9:
            print("Viso gero")
            biudzetas._issaugoti_zurnala() # issaugoti duomenis pries baigiant programa
            break
    except ValueError:
        print("BLOGA IVESTIS. BANDYKITE DAR KARTA")