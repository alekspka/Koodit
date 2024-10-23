class Auto:

    def __init__(self, rekkari, maxnopeus):
        self.rekkari = rekkari
        self.maxnopeus = maxnopeus
        self.nopeusatm = 0
        self.kuljettu_matka = 0

    def tulostus(self):
        print(f"Rekisteritunnus: {self.rekkari}")
        print(f"Auton huippunopeus: {self.maxnopeus}")
        print(f"Tämänhetkinen nopeus: {self.nopeusatm}")
        print(f"Kuljettu matka: {self.kuljettu_matka}")


auto1 = Auto("ABC-123","142 km/h")
Auto.tulostus()
