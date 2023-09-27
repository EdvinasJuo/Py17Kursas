# Sukurti programą, kuri:
# • Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
# • Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
# • Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
# Patarimai:
# • Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_ctime
import os
import datetime
todays_date = datetime.datetime.today()

os.chdir("C:\\Users\\edvin\\OneDrive\\Desktop\\Naujas Katalogas")
# os.mkdir("Naujas Katalogas")


with open("TekstinisFailas.txt", "w") as failas:
    failas.write(f"{todays_date}")

modify_size = os.stat("TekstinisFailas.txt").st_size
print(modify_size)