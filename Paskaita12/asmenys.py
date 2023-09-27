import logging


logging.basicConfig(level=logging.INFO, filename="asmenys.log", format="%(asctime)s:%(levelname)s:%(message)s")



class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logging.info(f"Sukurtas darbuotojas: {self.vardas} {self.pavarde}")  # KVIEST IS MAZOSIOS< KAD PAIMTU FUNKCIJA O NE KONSTANTA


tadas = Asmuo("Tadas", "Tadukas")
jonas = Asmuo("Jonas", "Jonukas")