import tkinter as tk
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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
    results.delete(0, tk.END)  # Clear the results box
    for employee in employees:
        results.insert(tk.END, str(employee))

def create_employees():
    f_name = first_name_entry.get()
    l_name = last_name_entry.get()
    birthday_str = birthday_entry.get()
    responsibilities = responsibilities_entry.get()
    salary = salary_entry.get()

    try:
        birthday = datetime.strptime(birthday_str, '%Y-%m-%d')
        employee = Employees(f_name, l_name, birthday, responsibilities, salary, datetime.utcnow())
        session.add(employee)
        session.commit()
        status_label.config(text="Darbuotojas sėkmingai pridėtas į duomenų bazę")
    except ValueError:
        status_label.config(text="Netinkamas datos formatas. Prašome įvesti tokiu formatu: (YYYY-MM-DD)")

def update_employees():
    employee_id = int(update_employee_entry.get())
    update_employee_id = session.query(Employees).get(employee_id)

    if update_employee_id:
        new_f_name = update_employee_f_name_entry.get()
        new_l_name = update_employee_l_name_entry.get()
        new_birthday_str = update_employee_birthday_entry.get()
        new_responsibilities = update_employee_responsibilities_entry.get()
        new_salary = update_employee_salary_entry.get()

        try:
            new_birthday = datetime.strptime(new_birthday_str, '%Y-%m-%d')
            update_employee_id.f_name = new_f_name
            update_employee_id.l_name = new_l_name
            update_employee_id.birthday = new_birthday
            update_employee_id.responsibilities = new_responsibilities
            update_employee_id.salary = new_salary

            session.commit()
            status_label.config(text="Darbuotojo informacija sėkmingai atnaujinta")
        except ValueError:
            status_label.config(text="Netinkamas datos formatas. Prašome įvesti tokiu formatu: (YYYY-MM-DD)")
    else:
        status_label.config(text="Darbuotojas su tokiu ID nerastas.")

def delete_employees():
    delete_id = int(delete_employee_entry.get())
    delete_employee = session.query(Employees).get(delete_id)

    if delete_employee:
        session.delete(delete_employee)
        session.commit()
        status_label.config(text="Darbuotojas sėkmingai ištrintas")
    else:
        status_label.config(text="Darbuotojas su tokiu ID nerastas.")

app = tk.Tk()
app.title("Employee Management")

icon_path = "user.ico"

app.iconbitmap(default = icon_path)

section_title = tk.Label(app, text="DARBUOTOJO PRIDĖJIMAS", font=("Helvetica", 8))
section_title.pack()

#laukai darbuotojo pridejimui
tk.Label(app, text="Vardas:").pack()
first_name_entry = tk.Entry(app)
first_name_entry.pack()

tk.Label(app, text="Pavardė:").pack()
last_name_entry = tk.Entry(app)
last_name_entry.pack()

tk.Label(app, text="Gimimo data (YYYY-MM-DD):").pack()
birthday_entry = tk.Entry(app)
birthday_entry.pack()

tk.Label(app, text="Pareigos:").pack()
responsibilities_entry = tk.Entry(app)
responsibilities_entry.pack()

tk.Label(app, text="Atlyginimas:").pack()
salary_entry = tk.Entry(app)
salary_entry.pack()

# Mygtukas prideti darbutoja
add_employee_button = tk.Button(app, text="Pridėti darbuotoją", command=create_employees)
add_employee_button.pack()

section_title = tk.Label(app, text="DARBUOTOJO REDAGAVIMAS", font=("Helvetica", 8))
section_title.pack()

#Laukai atnaujinimui darbuotojo
tk.Label(app, text="ID:").pack()
update_employee_entry = tk.Entry(app)
update_employee_entry.pack()

tk.Label(app, text="Naujas vardas:").pack()
update_employee_f_name_entry = tk.Entry(app)
update_employee_f_name_entry.pack()

tk.Label(app, text="Nauja pavardė:").pack()
update_employee_l_name_entry = tk.Entry(app)
update_employee_l_name_entry.pack()

tk.Label(app, text="Nauja gimimo data (YYYY-MM-DD):").pack()
update_employee_birthday_entry = tk.Entry(app)
update_employee_birthday_entry.pack()

tk.Label(app, text="Naujos pareigos:").pack()
update_employee_responsibilities_entry = tk.Entry(app)
update_employee_responsibilities_entry.pack()

tk.Label(app, text="Naujas atlyginimas:").pack()
update_employee_salary_entry = tk.Entry(app)
update_employee_salary_entry.pack()

# mygtukas atnaujinimui
update_employee_button = tk.Button(app, text="Atnaujinti darbuotoją", command=update_employees)
update_employee_button.pack()

section_title = tk.Label(app, text="DARBUOTOJO IŠTRYNIMAS", font=("Helvetica", 8))
section_title.pack()

# laukas : istrinimas pagal ID
tk.Label(app, text="Ištrinti pagal ID:").pack()
delete_employee_entry = tk.Entry(app)
delete_employee_entry.pack()

# mygtukas istrinti darbuotoja
delete_employee_button = tk.Button(app, text="Ištrinti darbuotoją", command=delete_employees)
delete_employee_button.pack()


status_label = tk.Label(app, text="")
status_label.pack()

# atvaizdavimas darbuotoju
results = tk.Listbox(app)
results.pack(fill=tk.BOTH, expand=True)

# Mygtukas rodyti darbuotojus
display_button = tk.Button(app, text="Rodyti darbuotojus", command=display_employees)
display_button.pack()

app.mainloop()