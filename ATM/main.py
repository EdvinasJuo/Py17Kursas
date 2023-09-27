# ATM sistema turėtų pradėti nuo naudotojo autentiškumo patvirtinimo.
# Paprastai prašoma įvesti PIN kodą arba kitą autentiškumo patvirtinimo būdą.
# Įgyvendinkite logiką, leidžiančią patikrinti naudotojo PIN kodą
# pagal saugomą autorizuotų naudotojų duomenų bazę.

def users():
    users_logins = {
        'JOHN': '1234',
        'DOE': '4321',
        'EDVINAS': '9999'
    }

def user_authentification(users_logins):
    user_input = input("Enter your username/account number: ").upper()
    pin_input = input("Enter your PIN: ")

    if user_input in users_logins:
        stored_pin = users_logins[user_input]
        if pin_input == stored_pin:
            return True
    return False

def main_menu_ui():
    print("Pasirinkite veiksmą")
    print("1 - Patikrinti likutį")
    print("2 - Išimti lėšas")
    print("3 - Įnešti lėšas")
    print("Q - Išeiti iš bankomato")

def atm_system():
    login_successful = user_authentification(users())

    if login_successful:
        print("Autentifikacija pavyko. Prisijungta į ATM")
        main_menu_ui()
    else:
        print("Autentifikacija nepavyko. Negalima atvaizduoti pagrindinio meniu")

atm_system()