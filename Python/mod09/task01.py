# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

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


auto1 = Auto("ABC-123","142 km/h")
auto1.tulostus()
