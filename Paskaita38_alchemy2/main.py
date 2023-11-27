from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Float
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///banks.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Asmuo(Base):
    __tablename__ = 'Asmuo'
    id = Column(Integer, primary_key=True)
    f_name = Column('Vardas', String, nullable=False)
    l_name = Column('Pavardė', String, nullable=False)
    personal_code = Column('Asmens kodas', Integer, unique=True, nullable=False)
    phone_number = Column('Tel. Nr.', String, unique=True, nullable=False)
    Saskaitos = relationship('Saskaita', back_populates='asmuo')


class Bankas(Base):
    __tablename__ = 'Bankas'
    id = Column(Integer, primary_key=True)
    name = Column('Pavadinimas', String, nullable=False)
    address = Column('Adresas', String, nullable=False)
    bank_code = Column('Banko kodas', Integer, nullable=False)
    swift_code = Column('Swift kodas', String, nullable=False)
    Saskaitos = relationship('Saskaita', back_populates='bankas')

class Saskaita(Base):
    __tablename__ = 'Saskaita'
    id = Column(Integer, primary_key=True)
    account_number = Column('Sąskaitos numeris', String, unique=True, nullable=False)
    balance = Column('Balansas', Float)
    asmuo_id = Column(Integer, ForeignKey('Asmuo.id'))
    bankas_id = Column(Integer, ForeignKey('Bankas.id'))
    asmuo = relationship('Asmuo', back_populates='Saskaitos')
    bankas = relationship('Bankas', back_populates='Saskaitos')

Base.metadata.create_all(engine)

def add_person():
    print('Pridėti asmenį: ')
    f_name = input("Vardas: ")
    l_name = input("Pavardė: ")

    while True:
        personal_code = input("Asmens kodas (11 skaitmenų): ")
        if personal_code.isdigit() and len(personal_code) == 11:
            break
        else:
            print("Asmens kodas turi būti tiksliai 11 skaitmenų.")

    phone_number = input("Tel. Nr.: ")

    try:
        person = Asmuo(f_name=f_name, l_name=l_name, personal_code=personal_code, phone_number=phone_number)
        session.add(person)
        session.commit()
        print("Asmuo sėkmingai pridėtas į duomenų bazę.")
    except ValueError:
        print("Nepavyko pridėti asmens į duomenų bazę.")


def add_bank():
    print('Pridėti banką: ')
    name = input("Banko pavadinimas: ")
    address = input("Adresas: ")
    bank_code = int(input("Banko kodas: "))
    swift_code = input("Swift kodas: ")

    try:
        bank = Bankas(name = name, address = address, bank_code = bank_code, swift_code = swift_code)
        session.add(bank)
        session.commit()
        print("Bankas sėkmingai pridėtas į duomenų bazę.")
    except ValueError:
        print("Nepavyko pridėti banko į duomenų bazę.")


def add_account():
    print("Pridėti naują saskaitą: ")
    account_number = input("Sąskaitos numeris: ")
    balance = float(input("Balansas: "))
    owner_id = int(input("Saviniko ID: "))

    owner = session.query(Asmuo).filter_by(id=owner_id).first()
    if not owner:
        print("Asmuo su tokiu ID nerastas. Patikrinkite asmens ID")
        return

    bank_id = int(input("Banko ID: "))
    bank = session.query(Bankas).filter_by(id = bank_id).first()
    if not bank:
        print("Bankas su tokiu ID nerastas. Patikrinkite banko ID.")
        return

    new_account = Saskaita(account_number = account_number, balance=balance, asmuo = owner, bankas = bank)

    try:
        session.add(new_account)
        session.commit()
        print("Sąskaita sėkmingai prideta.")
    except Exception as e:
        session.rollback()
        print(f"Klaida pridedant sąskaita: {e}")
        print("Transakcija atšaukta.")


def view_own_accounts():
    owner_id = input("Iveskite asmens ID: ")
    person = session.query(Asmuo).filter_by(id = owner_id).first()

    if person:
        accounts = session.query(Saskaita).filter_by(asmuo=person).all()

        if accounts:
            print(f"Saskaitos: {person.f_name} {person.l_name} ID: {owner_id}")
            for account in accounts:
                print(f"Sąskaitos numeris: {account.account_number}, Bankas: {account.bankas.name}. Balansas: {account.balance}")
        else:
            print(f"{person.f_name} {person.l_name} ({id}) neturi jokių sąskaitų.")
    else:
        print(f"Asmuo su ID: {id} nerastas. Patikrinkite ID.")


def view_all_users():
    users = session.query(Asmuo).all()

    if users:
        print("Visi vartotojai:")
        for user in users:
            print(
                f"ID: {user.id}, "
                f"Vardas: {user.f_name}, "
                f"Pavardė: {user.l_name}, "
                f"Asmens kodas: {user.personal_code}, "
                f"Tel. Nr.: {user.phone_number}")
    else:
        print("Nėra įrašų apie vartotojus duomenų bazėje.")


def view_all_banks():
    banks = session.query(Bankas).all()

    if banks:
        print("Visi bankai:")
        for bank in banks:
            print(
                f"Pavadinimas: {bank.name}, "
                f"Adresas: {bank.address}, "
                f"Banko kodas: {bank.bank_code}, "
                f"Swift kodas: {bank.swift_code}"
            )
    else:
        print("Nėra įrašų apie bankus duomenų bazėje.")

def view_all_accounts():
    accounts = session.query(Saskaita).all()

    if accounts:
        print("Visos saskaitos: ")
        for account in accounts:
            person = session.query(Asmuo).filter_by(id=account.asmuo_id).first()
            person_name = f"{person.f_name} {person.l_name}" if person else "Nerastas"

            bank = session.query(Bankas).filter_by(id=account.bankas_id).first()
            bank_name = bank.name if bank else "Nerastas"

            print(
                f"Saskaitos numeris: {account.account_number}, "
                f"Balansas: {account.balance}, "
                f"Asmuo: {person_name}, "
                f"Bankas: {bank_name}"
            )

def add_money():
    account_number = input("Įveskite sąskaitos numerį: ")
    account = session.query(Saskaita).filter_by(account_number=account_number).first()

    if account:
        print(f"Sąskaitos informacija: Sąskaitos numeris: {account.account_number}, Balansas: {account.balance:.2f}€")
        amount = float(input("Iveskite kiek pinigų norite pridėti: "))
        account.balance += amount
        session.commit()
        print(f"Pridėta {amount:.2f}€. Naujas balansas: {account.balance:.2f}€")
    else:
        print(f"Sąskaita su numeriu {account_number} nerasta. Patikrinkite sąskaitos numerį.")

def withdraw_money():
    account_number = input("Įveskite sąskaitos numerį: ")
    account = session.query(Saskaita).filter_by(account_number=account_number).first()

    if account:
        print(f"Sąskaitos informacija: Sąskaitos numeris: {account.account_number}, Balansas: {account.balance:.2f}€")
        amount = float(input("Iveskite kiek pinigų norite išsiimti: "))
        if amount <= account.balance:
            account.balance -= amount
            session.commit()
            print(f"Nuimta {amount:.2f}€. Naujas balansas: {account.balance:.2f}€")
        else:
            print("Nepakankamas balansas sąskaitoje.")
    else:
        print(f"Sąskaita su numeriu {account_number} nerasta. Patikrinkite sąskaitos numerį.")
