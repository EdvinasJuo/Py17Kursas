class Zmogus:
    def __init__(self, vardas, amzius):
        if not isinstance(vardas, str):
            raise TypeError("vardas must be a string")
        if not isinstance(amzius, int):
            raise TypeError("amzius must be an integer")
        self.vardas = vardas
        self.amzius = amzius

    def gauti_informacija(self):
        return f'Žmogaus vardas: {self.vardas}, Amžius: {self.amzius}'


zmogus1 = Zmogus("Jonas", 30)


print(zmogus1.gauti_informacija())