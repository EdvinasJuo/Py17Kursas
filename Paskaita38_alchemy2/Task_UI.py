from main import *

while True:
    choice = int(input("Pasirinkite veiksmą: "
                       "\n1 - Pridėti asmenį "
                       "\n2 - Pridėti banką "
                       "\n3 - Pridėti sąskaitą "
                       "\n4 - Peržiūrėti asmens sąskaitas "
                       "\n5 - Peržiūrėti visus asmenis "
                       "\n6 - Peržiūrėti visus bankus "
                       "\n7 - Peržiūrėti visas sąskaitas "
                       "\n8 - Pridėti pinigų "
                       "\n9 - Nuimti pinigų "
                       "\n10 - Išeiti iš programos"))

    if choice == 1:
        add_person()
    if choice == 2:
        add_bank()
    if choice == 3:
        add_account()
    if choice == 4:
        view_own_accounts()
    if choice == 5:
        view_all_users()
    if choice == 6:
        view_all_banks()
    if choice == 7:
        view_all_accounts()
    if choice == 8:
        add_money()
    if choice == 9:
        withdraw_money()
    if choice == 10:
        break