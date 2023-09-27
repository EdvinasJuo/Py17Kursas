import os

# current_path = os.getcwd() # PARODO KURIOJ DIREKTORIJOJ YRA FAILAS
# print(current_path)


# os.chdir('C:\\Users\\edvin\\OneDrive\\Desktop') # PERKELIAMA DIREKTORIJA
# new_path = os.getcwd() # PARODO KURIOJ DIREKTORIJOJ YRA FAILAS
# print(new_path)


# print(os.listdir('C:\\Users\\edvin\\OneDrive\\Desktop')) #Atprintina aplanke esancius failus, galima paduoti path


# os.mkdir("naujas_aplankas/naujas") # SUKURIA DIREKTORIJA, Jeigu nenurodom path tai sukurs darbiniam aplankale. per slasha galima prideti nauja folderi


#Sukuriami iskart visi aplankai, kad nereiketu po viena. sukurs kiek parasysim. Exist_ok = True, nemeta klaidos, kad jau toks folderis yra
# os.makedirs("naujas_aplankas2/naujas/naujas2", exist_ok=True)



# import datetime
#
# modify_time = os.stat("naujas_aplankas2/naujas/naujas2/random_file").st_mtime # GAUNAM FAILO INFORMACIJA. per . galima nurodyti kokia funckija norime passiimti
# print(modify_time)
# print(os.stat("naujas_aplankas2/naujas/naujas2/random_file").st_size)
#
# print(datetime.datetime.fromtimestamp(modify_time))
#

# Sukuriamas failas
# failas = open("failas.txt", "w")
# failas.write("Sveiki visi!\n")
# failas.write("Sveiki visi!\n")
# failas.close()


# # IRASINEJIMO BUDAS
# with open("failas2.txt", "w") as failas: # NEREIKIA RASYTI failas.close(). Uzsidaro automatiskai. SITA NAUDOSIM!
#     failas.write("Labas")
#
# # READINIMO BUDAS
# with open("failas.txt", "r") as failas: #
#     print(failas.read())
#
#
# # READINIMO su IRASINEJIMO BUDAS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# with open("failas.txt", "r+") as failas: #
#     print(failas.read())
#     failas.write("Labas\n")
#     failas.write("Labas\n")
#     failas.write("Labas\n")
#

# READINIMO su IRASINEJIMO BUDAS KURIS ISKARTRO PRIDEDA PRIE GALO
# with open("failas.txt", "a", encoding="UTF-8") as failas: #
#     failas.write("ąčęėąęčį")

# PRADEDA RSYTI NUO KURSORIAUS
# with open("failas.txt", "w", encoding="UTF-8") as failas:
#     failas.write("Test")
#     failas.seek(0)
#     failas.write("BE")


# GRAZINA EILUTES SU READLINE
# with open("failas.txt", "r", encoding="UTF-8") as failas:
#     print(failas.readline())
#     print(failas.readline())
#

# # NUSKAITO VISAS EILUTES
# with open("failas.txt", "r", encoding="UTF-8") as failas:
#     print(failas.readlines())


# NUSKAITO VISKA SU FOR CIKLU
# with open("failas.txt", "r", encoding="UTF-8") as failas:
#     for eilute in failas:
#         print(eilute, end="")


# NUSKAITO TIEK DUOMENU KIEK MUMS REIKIA
# with open("failas.txt", "r", encoding="UTF-8") as failas:
#     print(failas.read(49))      # NURODOM KIEK SIMBOLIU TURI NUSKAITYTI
#     print(failas.read(20))      # NURODOM KIEK SKAITYTI TOLIAU


# PERKOPIJUOTI DUOMENIS IS VIENO FAILO I KITA
# with open("failas.txt", "r", encoding="UTF-8") as failas_read:
#     with open("failas3.txt", "w", encoding="UTF-8") as failas_write:
#         for eilute in failas_read:
#             failas_write.write(eilute)


# GALIM PERKOPIJUOTI NUOTRAUKAS
with open("foto.jpg", "rb", encoding="UTF-8") as failas_read:
     with open("foto2.jpg", "wb", encoding="UTF-8") as failas_write:
         for eilute in failas_read:
             failas_write.write(eilute)