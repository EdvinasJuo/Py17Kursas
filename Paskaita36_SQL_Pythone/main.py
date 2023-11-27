import sqlite3

# conn = sqlite3.connect('zmones.db')

# c = conn.cursor() ## KAIP QUERY
#
# # query yra mūsų SQL užklausa.
# query = '''
# CREATE TABLE IF NOT EXISTS draugai (
#     f_name VARCHAR(50),
#     l_name VARCHAR(50),
#     email VARCHAR(100)
# );
# '''
#
# c.execute(query)
# conn.commit() # conn.commit() - išsaugo pakeitimus duomenų bazėje.
# conn.close() #conn.close() - uždarome atidarytą prisijungimą.


# --------------------- ANTRAS BUDAS SU WITH CONN: NEREIKES RANKINIU BUDU ISSAUGOTI IR UZDARINETI DB

conn = sqlite3.connect("draugai.db")
c = conn.cursor()

with conn:
    c.execute("INSERT INTO draugai VALUES ('Domantas', 'Rutkauskas', 'd.rutkauskas@imone.lt')")
    c.execute("INSERT INTO draugai VALUES ('Rimas', 'Radzevičius', 'RR@gmail.com')")

# --------------------- Įrašų paieška--------------------------------------

with conn:
    c.execute("SELECT * From darbuotojai WHERE pavarde='Rutkauskas'")
    print(c.fetchall())