print("Teksto zaidimas: ELEKTRA\n")
print("""Zaidimo taisykles:
turite pasirinkti norimas duris.\n""")

print("""Žiema. Šalta. Esate pasimetes vidurį miško.
Pradėjo šalti kojos, jaučiamas neapsakomas alkis
Ieškote kur galite sustosi ir pasišildyti
ir staiga miško gilūmoje pamatote apleista namą.
Užėjus į namą iškart galime pamatyti jog elektros laidai nutraukti.
atvėrę pagrindines duris pamatote dar 3 skirtingas duris.
Pasirinkite į kurias duris norite eiti:
Zalias - z, Raudonos - r, Melynos - m""")

choice = input("IVESKITE KURIAS DURIS ATIDAROTE: ")
if choice == "z":
    print("Pasirinkote zalias duris")
elif choice == "r":
    print("Pasirinkote raudonas duris")
elif choice == "m":
    print("Pasirinkote melynas duris")