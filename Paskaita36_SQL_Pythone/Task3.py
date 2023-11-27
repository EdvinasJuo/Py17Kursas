import sqlite3
from task3_database_info import paskaitos_db

conn = sqlite3.connect('paskaitos.db')
c = conn.cursor()

with conn:
    c.execute('''CREATE TABLE IF NOT EXISTS paskaitos (
        id INTEGER PRIMARY KEY,
        pavadinimas TEXT,
        destytojas TEXT,
        trukme INTEGER
    )''')

    # c.executemany("INSERT INTO paskaitos VALUES(?,?,?,?)", paskaitos_db)

def print_lectures_of_more_than_50():
    with conn:
        c.execute("SELECT * FROM paskaitos WHERE trukme > 50")
        paskaitos = c.fetchall()
        if paskaitos:
            print("Paskaitos didesnes uz 50")
            for paskaita in paskaitos:
                print("ID:", paskaita[0])
                print("Pavadinimas:", paskaita[1])
                print("Destytojas:", paskaita[2])
                print("Trukmė:", paskaita[3])
                print("-" * 30)
        else:
            print("Nėra irasu duomenu bazeje.")

def change_lecture_name():
    with conn:
        c.execute("UPDATE paskaitos SET pavadinimas = 'Python programavimas' WHERE pavadinimas = 'Python'")

def delete_lecture_by_name():
    with conn:
        c.execute("DELETE FROM paskaitos WHERE destytojas = 'Tomas'")

def print_all_lectures():
    with conn:
        c.execute("SELECT * FROM paskaitos")
        paskaitos = c.fetchall()
        if paskaitos:
            print("Paskaitos didesnes uz 50")
            for paskaita in paskaitos:
                print("ID:", paskaita[0])
                print("Pavadinimas:", paskaita[1])
                print("Destytojas:", paskaita[2])
                print("Trukmė:", paskaita[3])
                print("-" * 30)
        else:
            print("Nėra irasu duomenu bazeje.")

# print_lectures_of_more_than_50()
# change_lecture_name()
# delete_lecture_by_name()
print_all_lectures()