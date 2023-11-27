import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///projektai.db') # SUkuriamas rysis su failu (duomenu baze/pavadinimas)
Base = declarative_base()

class Projektas(Base):
    __tablename__ = 'Projektas' # Turi buti butinai nurodomas lenteles pavadinima
    id = Column(Integer, primary_key=True) #stulpelio kintamasisi ID. Tai yra stulpelis
    name = Column("Pavadinimas", String) #"Pavadinimas" -  tiesiog stulpelio pavadinimas o name yra kintamasis
    price = Column("Kaina", Float)
    created_date = Column("Sukūrimo data", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"

if __name__ == '__main__':
    Base.metadata.create_all(engine)