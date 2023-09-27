# Sukurti programą, kuri:
# • Leistų vartotojui įvesti 5 žodžius
# • Pridėtų įvestus žodžius į sąrašą
# • Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
# Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
# Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index

words = []

while True:
    try:
        list_size = int(input("Nurodykite saraso dydi: "))
        if list_size > 0:
            break
        else:
            print("Skaicius turi buti didesnis uz 0.")
    except ValueError:
        print("Ivestas ne skaicius. Bandykite dar karta.")

for word in range(list_size):
    input_word = input("Iveskite zodi: ").upper()
    words.append(input_word)

for word in words:
    index = words.index(word)
    print(f"Zodzio: '{word}' ilgis yra {len(word)} jo eiles numeris yra : {index + 1}")


