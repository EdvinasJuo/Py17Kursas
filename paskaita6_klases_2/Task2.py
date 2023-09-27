# Sukurti programą, kuri:
# • Turėtų klasę Darbuotojas
# • Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
# • Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki
# šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
# • Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą
# atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
# • Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant
# darbuotojui 5 dienas per savaitę
# • Sukurti norimą Darbuotojo objektą
# • Sukurti norimą NormalusDarbuotojas objektą
# • Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima

import datetime
import pandas as pd

class Darbuotojas():
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo

    def _skaiciuoti_dienas(self):
        todays_date = datetime.date.today()
        pradirbtos_dienos = todays_date - self.dirba_nuo
        return pradirbtos_dienos.days

    def skaiciuoti_atlyginima(self):
        pradirbtos_dienos = self._skaiciuoti_dienas()
        atlyginimas = pradirbtos_dienos * 8 * self.valandos_ikainis
        return atlyginimas

    def __str__(self):
        return (f"Darbuotojo vardas: {self.vardas}. Atlyginimas: {self.skaiciuoti_atlyginima()} Eur. Uz {self._skaiciuoti_dienas()} dienas")


class NormalusDarbuotojas(Darbuotojas):
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        super().__init__(vardas, valandos_ikainis, dirba_nuo)

    def _skaiciuoti_dienas(self):
        todays_date = datetime.date.today()
        skaiciuoti_dienas = len(pd.bdate_range(self.dirba_nuo, todays_date)) # Gaunu darbo dienas importines Pandas
        return skaiciuoti_dienas

    def __str__(self):
        return (f"Darbuotojo vardas: {self.vardas}. Atlyginimas: {self.skaiciuoti_atlyginima()} Eur. Uz {self._skaiciuoti_dienas()} dienas")


darbuotojas1 = Darbuotojas("Paulius", 8.30, datetime.date(2023, 7, 16))
darbuotojas2 = NormalusDarbuotojas("Edgaras", 10.50, datetime.date(2023, 9, 18))

print(darbuotojas1)
print(darbuotojas2)