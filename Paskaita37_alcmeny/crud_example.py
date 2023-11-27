from sqlalchemy.orm import sessionmaker
from main import Projektas, engine

Session = sessionmaker(bind=engine) #susikuriam session ir skliaustuose nurodom su kokiu dalyku norim susieti
session = Session()

# CREATE --------------------------------------------------------------------------------
# projektas1 = Projektas("Naujas pr.", 20000)
# session.add(projektas1)
# session.commit()
#
# projektas2 = Projektas("Mazas", 750)
# session.add(projektas2)
# session.commit()

# READ --------------------------------------------------------------------------------
# projektas1 = session.get(Projektas, 1) # KREIPIAMES I KLASE !!
# projektas2 = session.query(Projektas).filter_by(name="2 projektas").one()
#
# print(projektas1)
# print(projektas2.name)

# search = session.query(Projektas).filter(Projektas.name.ilike("2%")).all() #.all grazina visas reiksme liste
# search2 = session.query(Projektas).filter(Projektas.price > 1000).all()
# search3 = session.query(Projektas).filter(Projektas.price > 1000, Projektas.name.ilike("2%")).all()
#
# print(search2)

# UPDATE --------------------------------------------------------------------------------
#reikia pirma issitraukti ir tik tada pakeisti
#
# projektas1 = session.get(Projektas, 4)
# projektas1.price = 22000
# projektas1.name = "Naujausias"
# session.commit()

# kitas variantas kuris daro update pagal price
# projektas2 = session.query(Projektas).filter_by(price=22000.0).one()
# projektas2.name = "2 projektas tikrai"
# session.commit()


# DELETE --------------------------------------------------------------------------------
# projektas1 = session.query(Projektas).filter_by(name="Mazas").one()
# session.delete(projektas1)
# session.commit()


# --------------------------------- PAVYZDYS-------------------------------
while True:
    pasirinkimas = int(input("Pasirinkite veiksmą: \n1 - atvaizduoti projektus \n2 - sukurti projektą \n3 - pakeisti projektą \n4 - ištrinti projektą\n"))

    if pasirinkimas == 1:
        projektai = session.query(Projektas).all()
        print("-------------------")
        for projektas in projektai:
            print(projektas)
        print("-------------------")

    if pasirinkimas == 2:
        name = input("Įveskite projekto pavadinimą")
        price = float(input("Įveskite projekto kainą"))
        projektas = Projektas(name, price)
        session.add(projektas)
        session.commit()

    if pasirinkimas == 3:
        projektai = session.query(Projektas).all()
        print("-------------------")
        for projektas in projektai:
            print(projektas)
        print("-------------------")
        keiciamo_id = int(input("Pasirinkite norimo pakeisti projekto ID"))
        keiciamas_projektas = session.query(Projektas).get(keiciamo_id)
        pakeitimas = int(input("Ką norite pakeisti: 1 - pavadinimą, 2 - kainą"))
        if pakeitimas == 1:
            keiciamas_projektas.name = input("Įveskite projekto pavadinimą")
        if pakeitimas == 2:
            keiciamas_projektas.price = float(input("Įveskite projekto kainą"))
        session.commit()

    if pasirinkimas == 4:
        projektai = session.query(Projektas).all()
        print("-------------------")
        for projektas in projektai:
            print(projektas)
        print("-------------------")
        trinamo_id = int(input("Pasirinkite norimo ištrinti projekto ID"))
        trinamas_projektas = session.query(Projektas).get(trinamo_id)
        session.delete(trinamas_projektas)
        session.commit()