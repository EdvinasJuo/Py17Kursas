from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///employees.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Employees(Base):
    __tablename__ = 'Employees'
    id = Column(Integer, primary_key=True)
    f_name = Column('Vardas', String)
    l_name = Column('Pavardė', String)
    birthday = Column('Gimimo data', DateTime)
    responsibilities = Column('Pareigos', String)
    salary = Column('Atlyginimas', Float)
    working_since = Column('Dirba nuo', DateTime, default=datetime.utcnow)

    def __init__(self, f_name, l_name, birthday, responsibilities, salary, working_since):
        self.f_name = f_name
        self.l_name = l_name
        self.birthday = birthday
        self.responsibilities = responsibilities
        self.salary = salary
        self.working_since = working_since

    def __repr__(self):
        return (f"{self.id}. {self.f_name} {self.l_name}, {self.birthday.strftime('%Y-%m-%d')}. "
                f"Pareigos - {self.responsibilities}. Atlyginimas - {self.salary}. "
                f"Dirba nuo - {self.working_since.strftime('%Y-%m-%d')}")

Base.metadata.create_all(engine)

def display_employees():
    employees = session.query(Employees).all()
    print('----------------------------')
    for employee in employees:
        print(employee)
    print('----------------------------')

def create_employees():
    f_name = input("Įveskite darbuotojo vardą: ")
    l_name = input("Įveskite darbuotojo pavardę: ")
    birthday_str = input("Įveskite darbuotojo gimimo datą (YYYY-MM-DD): ")
    responsibilities = input("Įveskite darbuotojo pareigas: ")
    salary = input("Įveskite darbuotojo atlyginimą: ")

    try:
        birthday = datetime.strptime(birthday_str, '%Y-%m-%d')
        employee = Employees(f_name, l_name, birthday, responsibilities, salary, datetime.utcnow())
        session.add(employee)
        session.commit()
        print("Darbuotojas sėkmingai pridėtas į duomenų bazę")
    except ValueError:
        print("Netinkamas datos formatas. Prašome įvesti tokiu formatu: (YYYY-MM-DD).")

def update_employees():
    display_employees()
    employee_id = int(input("Pasirinkite norimo atnaujinti darbuotojo ID: "))
    update_employee_id = session.query(Employees).get(employee_id)

    if update_employee_id:
        update_employee_id.first_name = input(f"Įveskite naują vardą: ")
        update_employee_id.last_name = input(f"Įveskite naują pavardę: ")
        update_employee_id.birthday = datetime.strptime(input(f"Įveskite naują gimimo datą (YYYY-MM-DD): "), '%Y-%m-%d')
        update_employee_id.responsibilities = input(f"Įveskite naujas pareigas: ")
        update_employee_id.salary = input(f"Įveskite naują atlyginimą: ")

        session.commit()
        print("Darbuotojo informacija sėkmingai atnaujinta")
    else:
        print("Darbuotojas su tokiu ID nerastas.")


def delete_employees():
    display_employees()
    delete_id = int(input("Pasirinkite norimo istrinti darbuotojo ID: "))
    delete_employee = session.query(Employees).get(delete_id)
    session.delete(delete_employee)
    session.commit()