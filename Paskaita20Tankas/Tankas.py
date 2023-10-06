import random


class Tankas:
    def __init__(self):
        # pradines X,Y koordinates
        self.x = 0
        self.y = 0
        # pradine kryptis
        self.kryptis = "siaure"
        self.suviu_sk = {"siaure": 0, "rytai": 0, "pietus": 0, "vakarai": 0}
        self.taikinys_x = random.randint(-5, 5)
        self.taikinys_y = random.randint(-5, 5)
        self.taikinys_numustas = False
        # pradiniai taskai
        self.taskai = 100

    def pamazinti_taskai(self):
        self.taskai -= 10
        if self.taskai == 0:
            print("\nBaigesi taskai.. Pralaimejote")
            exit()

    def pirmyn(self):
        if self.kryptis == "siaure":
            self.y += 1
        elif self.kryptis == "rytai":
            self.x += 1
        elif self.kryptis == "pietus":
            self.y -= 1
        elif self.kryptis == "vakarai":
            self.x -= 1
        self.pamazinti_taskai()


    def atgal(self):
        if self.kryptis == "siaure":
            self.y -= 1
        elif self.kryptis == "rytai":
            self.x -= 1
        elif self.kryptis == "pietus":
            self.y += 1
        elif self.kryptis == "vakarai":
            self.x += 1
        self.pamazinti_taskai()

    def kairen(self):
        if self.kryptis == "siaure":
            self.x -= 1
        elif self.kryptis == "pietus":
            self.x += 1
        elif self.kryptis == "vakarai":
            self.y -= 1
        elif self.kryptis == "rytai":
            self.y -= 1
        self.pamazinti_taskai()

    def desinen(self):
        if self.kryptis == "siaure":
            self.x += 1
        elif self.kryptis == "pietus":
            self.x += 1
        elif self.kryptis == "vakarai":
            self.y -= 1
        elif self.kryptis == "rytai":
            self.y -= 1
        self.pamazinti_taskai()

    def suvis(self):
        atstumas = ((self.taikinys_x - self.x) ** 2 + (self.taikinys_y - self.y) ** 2) ** 0.5

        # Tikriname, ar taikinys yra pakankamai arti (pvz., atstumas mažesnis nei 2 vienetai)
        if atstumas < 2:
            print("Taikinys numustas!")
            self.taikinys_numustas = True
            self.taskai += 50
        else:
            print("Taikinys nepasiekiamas. Turite priarteti arciau taikinio.")

    def informacija(self):
        print(f'\nTaikinio koordinates: ({self.taikinys_x}, {self.taikinys_y})')
        print(f'Tanko koordinates: x: {self.x} y: {self.y}')
        print(f'Jusu taskai: {self.taskai}')