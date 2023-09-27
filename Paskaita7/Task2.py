# Sukurti programą, kuri:
# • Leistų vartotojui įvesti norimą eilučių kiekį
# • Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# • Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
# Patarimai:
# • Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)



while True:
    try:
        input_colums = int(input("Iveskite kiek eiluciu vesite: "))
        sentences = []
        for i in range(input_colums):
            sentence_input = input(f"Iveskite {i+1} sakini: ")
            sentences.append(sentence_input)
        file_name = input("Iveskite failo pavadinima: ")
        with open(file_name, "w") as failas:
            for eilute in sentences:
                failas.write(f"{eilute}\n")
        choice = input("Ar norite testi Y/N ?")
        if choice.upper() == "Y":
            continue
        elif choice.upper() == "N":
            break
    except ValueError:
        print("Bloga ivestis. Programa baige darba")
    except FileNotFoundError:
        print("Bloga failo ivestis.")
    break



# OPTIMIZUOTAS
# pavadinimas = input("Iveskite kuriamo failo pavadinima: ")
# with open(f'{pavadinimas}.txt', 'w', encoding='UTF-8') as failas:
#     kiekis = int(input("Iveskite norima eiluciu kieki: "))
#     for eilute in range(kiekis):
#         eilute = input('Iveskite teksto eilute:') + '\n'
#         failas.write(eilute)
#     input('Norint uzbaigti programa, spauskite Enter')