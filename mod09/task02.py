# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

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

    def kiihdytys(self,muutos):
        uusi_nopeus = self.nopeusatm + muutos

        if uusi_nopeus > self.maxnopeus:
            self.nopeusatm = self.maxnopeus
        elif uusi_nopeus < 0:
            self.nopeusatm = 0
        else:
            self.nopeusatm = uusi_nopeus



auto1 = Auto("ABC-123",142)
auto2 = Auto("EDF-123",250)

auto1.kiihdytys(30)
auto1.kiihdytys(70)
auto1.kiihdytys(50)

auto2.kiihdytys(30)
auto2.kiihdytys(70)
auto2.kiihdytys(50)

auto1.tulostus()
auto2.tulostus()

print(f"Auton nopeus kiihdytyksen jälkeen: {auto1.nopeusatm} km/h.")
print(f"Auton nopeus kiihdytyksen jälkeen: {auto2.nopeusatm} km/h.")

auto1.kiihdytys(-200)
auto2.kiihdytys(-200)

auto1.tulostus()
auto2.tulostus()
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto1.nopeusatm} km/h.")
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto2.nopeusatm} km/h.")