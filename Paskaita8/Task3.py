sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, False, "Vakaras"]

# • Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
skaicius_sarasas = [x for x in sarasas if type(x) is int or type(x) is float]
print(f"Skaiciai esantys sarase: {skaicius_sarasas}")
skaiciu_sarase_suma = sum([x for x in sarasas if type(x) is int or type(x) is float])
print(f"Visu skaiciu suma: {skaiciu_sarase_suma}")

# • Sudėtų ir atspausdintų visus sąrašo žodžius
zodziai_sarase = [w for w in sarasas if type(w) is str]
print(f"Zodziai sarase: {zodziai_sarase}")
zodziu_sarase_suma = sum(type(x) is str for x in sarasas)
print(f"Zodziu sarase yra: {zodziu_sarase_suma}")

# • Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme
boolean_sarase = [b for b in sarasas if type(b) is bool and b == True]
print(f"Boolean'ai sarase: {boolean_sarase}")
boolean_sarase_suma = sum(type(b) is bool for b in sarasas if b == True)
print(f"Sarase boolean yra: {boolean_sarase_suma}")
