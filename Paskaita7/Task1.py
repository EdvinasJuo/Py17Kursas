# Sukurti programą, kuri:

# Patarimai:
# • Naudoti from datetime import datetime, datetime.today()
# • Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis
# • Kai kur galima panaudoti funkcijas iš praeitų pamok

import datetime
import this

zen_of_python = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# • Sukurtų failą „Tekstas.txt“ su pilnu tekstu "Zen of Python".
with open("Tekstas.txt", "w") as failas:
    failas.write(f"{zen_of_python}\n")

# • Atspausdintų tekstą iš sukurto failo
# with open("Tekstas.txt", "r") as failas:
#     print(failas.read())

# • Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
todays_date = datetime.datetime.today()
with open("Tekstas.txt", "a") as failas:
    failas.write(f"{todays_date}\n")

# • Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
with open("Tekstas.txt", "r+", encoding="UTF-8") as failas:
    sentence = failas.read()
    new_sentence = sentence.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")
    failas.seek(0)
    failas.write(f"{new_sentence}\n")
    # Truncate apkerpa failą, jei naujas sakinys yra trumpesnis uz senaji
    failas.truncate()


# • Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
with open("Tekstas.txt", "r+") as failas:
    visos_eilutes = failas.readlines()
    failas.seek(0) #Grizta i failo pradzia

    eilutes_numeris = 1
    for eilute in visos_eilutes:
        failas.write(f"{eilutes_numeris}. {eilute}")
        eilutes_numeris += 1

# Atspausdintų visą failo tekstą atbulai
with open("Tekstas.txt", "r", encoding="UTF-8") as failas:
    for eilute in failas:
        print(eilute[::-1])

# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
with open("Tekstas.txt", "r", encoding="UTF-8") as failas:
    uppercase = 0
    lowercase = 0

    visos_eilutes = failas.read()
    counting_words = len(visos_eilutes.split())
    counting_symbols = len(visos_eilutes)
    for symbol in visos_eilutes:
        if symbol.isupper():
            uppercase += 1
        elif symbol.islower():
            lowercase += 1

    print(f"Zodziu faile: {counting_words}")
    print(f"Simboliu faile: {counting_symbols}")
    print(f"Didziuju raidziu faile: {uppercase}")
    print(f"Mazuju raidziu faile: {lowercase}")

# • Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS
with open("Tekstas.txt", "r", encoding="UTF-8") as failas_read:
    with open("Tekstas2.txt", "w", encoding="UTF-8") as failas_write:
        for eilute in failas_read:
            failas_write.write(eilute.upper())
