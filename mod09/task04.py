#autokilpailu
import random

class Autotalli:
    def __init__(self):
        self.autot = []
    def autot_sisaan(self, auto):
        for a in self.autot:
            if a == auto:
                return
        self.autot.append(auto)

    def auto_ulos(self, auto):
        self.autot.remove(auto)

    def tulosta_inventaario(self):
        print("Autot tallissa:")
        for auto in self.autot:
            auto.tulosta_ominaisuudet()

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
        return


for i in range(10):
    uusi_auto = Auto(f"ABC-{i+1}", random.randint(100,200))
    talli.auto_sisaan(uusi_auto)
    talli.tulosta_inventaario()