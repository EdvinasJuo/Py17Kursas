import operator


# • Turėtų klasę Zmogus, su savybėmis vardas ir amzius
class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    # • Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
    def __repr__(self):
        return f"Zmogaus vardas: {self.vardas}. Jo amzius: {self.amzius}"


# • Inicijuoti kelis Zmogus objektus su vardais ir amžiais
zmogus1 = Zmogus("Paulius", 25)
zmogus2 = Zmogus("Edgaras", 21)
zmogus3 = Zmogus("Algirdas", 19)
zmogus4 = Zmogus("Ignas", 29)

# • Įdėti sukurtus Zmogus objektus į naują sąrašą
zmones = [zmogus1, zmogus2, zmogus3, zmogus4]


# • Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
def rusiavimas(zmogus):
    return zmogus.vardas


sort_by_name = sorted(zmones, key=rusiavimas)
print("Isrikiuoti pagal vardus:")
for zmogus in sort_by_name:
    print(zmogus)
print()

sort_by_age = sorted(zmones, key=operator.attrgetter("amzius"))
print("Isrikiuoti pagal amziu:")
for zmogus in sort_by_age:
    print(zmogus)
print()

sort_reversed = sorted(zmones, key=rusiavimas, reverse=True)
print("Isrikiuoti atbulai:")
for zmogus in sort_reversed:
    print(zmogus)