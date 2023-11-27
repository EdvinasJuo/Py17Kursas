import pickle
from enum import Enum

class IrasoTipas(Enum):
    PAJAMOS = "Pajamos"
    ISLAIDOS = "Išlaidos"

class Biudzetas:
    def __init__(self):
        self.zurnalas = self._nuskaityti_zurnala()

    def _issaugoti_zurnala(self):
        with open("biudzetas.pkl", "wb") as pickle_out:
            pickle.dump(self.zurnalas, pickle_out)

    def _nuskaityti_zurnala(self):
        try:
            with open("biudzetas.pkl", "rb") as pickle_in:
                return pickle.load(pickle_in)
        except FileNotFoundError:
            return []

    def prideti_irasa(self, suma, tipas):
        if isinstance(tipas, IrasoTipas):
            tipas = tipas.value

        if tipas not in [IrasoTipas.PAJAMOS.value, IrasoTipas.ISLAIDOS.value]:
            print("Neteisingas įrašo tipas.")
            return

        if suma < 0:
            suma = abs(suma)

        self.zurnalas.append({"tipas": tipas, "suma": suma})
        self._issaugoti_zurnala()

    def gauti_balansa(self):
        pajamos = sum(irasas['suma'] for irasas in self.zurnalas if irasas['tipas'] == IrasoTipas.PAJAMOS.value)
        islaidos = sum(irasas['suma'] for irasas in self.zurnalas if irasas['tipas'] == IrasoTipas.ISLAIDOS.value)
        balansas = pajamos - islaidos
        print(f"Pajamos: {pajamos}")
        print(f"Išlaidos: {islaidos}")
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
                                 "\n9 - išsaugoti ir uždaryti programą"))
        if pasirinkimas == 1:
            try:
                suma = float(input("Įveskite pajamų sumą: "))
                biudzetas.prideti_irasa(suma, IrasoTipas.PAJAMOS)
            except ValueError:
                print("NETEISINGA ĮVESTIS. BANDYKITE DAR KARTĄ")
        if pasirinkimas == 2:
            suma = int(input("Įveskite išlaidų sumą su minuso ženklu: "))
            biudzetas.prideti_irasa(suma, IrasoTipas.ISLAIDOS)
        elif pasirinkimas == 3:
            biudzetas.gauti_balansa()
        elif pasirinkimas == 4:
            biudzetas.atvaizduoti_irasus()
        elif pasirinkimas == 9:
            print("Viso gero")
            biudzetas._issaugoti_zurnala()
            break
    except ValueError:
        print("NETEISINGA ĮVESTIS. BANDYKITE DAR KARTĄ")
