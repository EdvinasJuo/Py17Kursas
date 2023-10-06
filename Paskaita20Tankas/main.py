from Tankas import *
tankas = Tankas()

while True:
    print("\nTanko valdymas:")
    print("1. Pirmyn | 2. Atgal | 3. Kairen | 4. Desinen | 5. Sauti | 6. Informacija | 7. Iseiti")

    choice = input("Pasirinkite veiksma: ")
    if choice == "1":
        tankas.pirmyn()
        tankas.informacija()
    elif choice == "2":
        tankas.atgal()
        tankas.informacija()
    elif choice == "3":
        tankas.kairen()
        tankas.informacija()
    elif choice == "4":
        tankas.desinen()
        tankas.informacija()
    elif choice == "5":
        tankas.suvis()
    elif choice == "6":
        tankas.informacija()
    elif choice == "7":
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kart.")
