#autokilpailu
import random

class Auto:

    def __init__(self, rekkari, maxnopeus):
        self.rekkari = rekkari
        self.maxnopeus = maxnopeus
        self.nopeusatm = 0
        self.kuljettu_matka = 0

    def tulostus(self):
        print(f"Rekkari: {self.rekkari}, Huippunopeus: {self.maxnopeus} km/h,"
              f"Nopeus nyt: {self.nopeusatm}, km/h, Kuljettu matka: {self.kuljettu_matka} kilometriä.")

        return

    def kiihdyta(self, nopeuden_muutos):
        self.nopeusatm = self.nopeusatm + nopeuden_muutos

        if self.nopeusatm > self.maxnopeus:
            self.nopeusatm = self.maxnopeus

        if self.nopeusatm < 0:
            self.nopeusatm = 0

    def kulje(self, tunnit=1):

        self.kuljettu_matka += self.nopeusatm * tunnit

autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

kilpailu_kaynnissa = True

tunti = 0

while kilpailu_kaynnissa:
    tunti += 1
    print(f"Tunti {tunti}:")

    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje()

        if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False

    for auto in autot:
        auto.tulostus()
    print("\n")

print("Kilpailu päättyi!")
print("Lopputulokset:")
for auto in autot:
    auto.tulostus()