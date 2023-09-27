# MASYVAI IR SARASAI

sarasas = []
skaiciai = [1, 2, 3, 4, 5, 6]
zodziai = ["Labas", "Vakaras", "Visiems"]
miksuotas = [5, 2.3, "Visi", True, [5, 6, 8]]

print(miksuotas[4][1]) # pasiekti list'a list'e

skaiciai.append(99) # APPEND prideda i List
print(skaiciai)

skaiciai[1] = 100 # Pakeisti reiksme nurodzius Indexa
print(skaiciai)

skaiciai.pop(2) # POP funkcija pasalina reiksme pagal indexa
print(skaiciai)

print(len(skaiciai)) # Parodo kiek yra elementu sarase su funkcija len()

longest_word = "Nebeprisivaizdotinklaraštininkaujantiesiems"
print(len(longest_word))