# ABSOLIUTINIS importas
from moduliai.mano_modulis2 import kintamasis2
# SALYGINIS importas
# from .mano_modulis2 import kintamasis2

kintamasis = "Cia yra testinis kintamasis"
k2 = kintamasis2

print("Mano_modulis sekmingai importuotas")

def parasyti_atbulai(sakinys):
    print(sakinys[::-1])

if __name__ == "__main__":  # NEATSPAUSDINS MAIN, Nes cia ima failo pavadinima.
    parasyti_atbulai("Testas")