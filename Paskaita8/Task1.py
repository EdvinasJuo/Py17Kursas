# Sukurti programą, kuri:
# • Prie kiekvieno sakinio su jūsų pasirinktu tekstu, pridėtų šauktuką ir atspausdintų naują sakinį.
# Patarimai:
# • Naudoti map (su lambda) arba comprehension, " ".join()

sarasas = ["As esu is Kauno", "Man yra 23 metai", "Megstu aktyvu laisvalaiki", "Labas"]
perdarytas_sarasas = [x + "!" for x in sarasas]
for tektas in perdarytas_sarasas:
    print(tektas)

