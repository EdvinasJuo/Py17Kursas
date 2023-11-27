import sqlite3
import csv
from task1_database_info import cars_db


# 1. Sukurkite duomenų bazę, kurioje būtų lentelė su automobilio marke, modeliu, spalva, pagaminimo metais, ir kaina.
# Lentelės sukūrimo ir užpildymo duomenimis užklausas galite pasigaminti mockaroo.com

conn = sqlite3.connect('cars.db')
c = conn.cursor()

with conn:
    c.execute('''CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY,
        make TEXT,
        model TEXT,
        year INTEGER,
        price INTEGER
    )''')

    # c.executemany("INSERT INTO cars VALUES(?,?,?,?,?)", cars_db)

# 2. Parašykite programą, kuri leistų vartotojui per konsolę:
# įvesti naują eilutę (automobilį su visais parametrais)
def inserting_new_auto():
    car_make = input("Iveskite automobilio marke: ")
    car_model = input("Iveskite automobilio modeli: ")
    car_year = input("Iveskite automobilio metus: ")
    car_price = input("Iveskite kaina: ")

    with conn:
        c.execute("INSERT INTO cars (make, model, year, price) VALUES(?,?,?,?)",
                  (car_make, car_model, car_year, car_price))
        print(f"Automobilis {car_make} {car_model} sekmingai iterptas")

#3. ieškoti įrašų pagal visus stulpelius.
# Vartotojas gali pasirinkti kuriuos parametrus paieškoje praleisti.
# Metus ir kainą vartotojas turėtų nurodinėti nuo -iki.

def find_car_by_info():
    try:
        car_make = input("Iveskite automobilio marke (palikti tuscia, jeigu nenorite ivesti): ")
        car_model = input("Iveskite automobilio modeli (palikti tuscia, jeigu nenorite ivesti): ")
        car_year_min  = input("Iveskite minimalius gamybos metus (palikti tuscia, jeigu nenorite ivesti): ")
        car_year_max = input("Iveskite maksimalius gamybos metus (palikti tuscia, jeigu nenorite ivesti): ")
        car_price_min = input("Iveskite minimalia kaina (palikti tuscia, jeigu nenorite ivesti): ")
        car_price_max = input("Iveskite maksimalia kaina (palikti tuscia, jeigu nenorite ivesti): ")

        query = "SELECT * FROM cars WHERE"
        parameters = []

        if car_make:
            query += " make = ? COLLATE NOCASE"
            parameters.append(car_make)

        if car_model:
            query += " model = ?"
            parameters.append(car_model)

        if car_year_min:
            query += " year >= ?"
            parameters.append(car_year_min)

        if car_year_max:
            query += " year <= ?"
            parameters.append(car_year_max)

        if car_price_min:
            query += " price >= ?"
            parameters.append(car_price_min)

        if car_price_max:
            query += " price <= ?"
            parameters.append(car_price_max)

        with conn:
            c.execute(query, parameters)
            cars = c.fetchall()

        if cars:
            print("Rasti automobiliai: ")
            for car in cars:
                print("ID:", car[0])
                print("Markė:", car[1])
                print("Modelis:", car[2])
                print("Metai:", car[3])
                print("Kaina:", car[4])
        else:
            print("Automobilis pagal jusu paieska nerastas.")
    except sqlite3.OperationalError:
        print("Automobilis pagal jusu paieska nerastas.")


def print_all_cars():
    with conn:
        c.execute("SELECT * FROM cars")
        cars = c.fetchall()
        if cars:
            print("Visi autmobiliai:")
            for car in cars:
                print("ID:", car[0])
                print("Markė:", car[1])
                print("Modelis:", car[2])
                print("Metai:", car[3])
                print("Kaina:", car[4])
                print("-" * 30)
        else:
            print("Nėra įrašų duomenų bazėje.")


def create_csv(filename):
    with conn:
        c.execute("SELECT * FROM cars")
        cars = c.fetchall()

    if cars:
        with open(filename, "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["ID", "Make", "Year", "Price"])
            csv_writer.writerows(cars)
        print(f"Duomenys issaugoti i '{filename}' faila.")
    else:
        print("Nera irasu duomenu bazeje")

while True:
    print("\nPasirinkite veiksma:")
    print("1. Iterpti automobili")
    print("2. Ieskoti automobilio")
    print("3. Atspausdinti visus automobilius")
    print("4. Issaugoti automobilius i CSV faila")
    print("5. Uzdaryti programa")
    choice = input("Iveskite pasirinkima: ")

    if choice == "1":
        inserting_new_auto()
    if choice == "2":
        find_car_by_info()
    if choice == "3":
        print_all_cars()
    if choice == "4":
        create_csv("cars.csv")
    if choice == "5":
        break
