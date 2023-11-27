from Task1 import *

while True:
    choice = int(input("Pasirinkite veiksmą: "
                       "\n1 - Atvaizduoti darbuotojus "
                       "\n2 - Sukurti darbuotoją "
                       "\n3 - Atnaujinti darbuotoją "
                       "\n4 - Ištrinti darbuotoją "
                       "\n5 - Išjungti programą\n"))

    if choice == 1:
        display_employees()

    if choice == 2:
        create_employees()

    if choice == 3:
        update_employees()

    if choice == 4:
        delete_employees()

    if choice == 5:
        print("Programa baigė veikti")
        break