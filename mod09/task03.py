# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Kuljettaja:
    def __init__(self, nimi, ika, auto):
        self.nimi = nimi
        self.ika = ika
        self.auto = auto

    def aja(self, nopeuden_muutos, aika):
        print(f"Olen {self.nimi}, {self.ika}-vuotias ja ajan autoa {self.auto.rekkari}")
        self.auto.kiihdytys(nopeuden_muutos)  # Kiihdytetään tai hidastetaan
        print(f"Auton nopeus nyt: {self.auto.nopeus} km/h")

class Auto:
    def __init__(self, rekkari, nopeus):
        self.rekkari = rekkari
        self.nopeus = nopeus
        self.matka = 2000
        self.huippunopeus = 100
        self.kuljettaja = "Räikkönen"

    def kulje(self, aika):
        self.matka += aika * self.nopeus
        print(f"Autolla {self.rekkari} ajettu yhteensä: {self.matka} km")


    def tulosta_ominaisuudet(self):
        print(f"{self.rekkari}, {self.huippunopeus} km/h")

    def kiihdytys(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0



a1 = Auto("ABC-123", 142)
a2 = Auto("DEF-123", 250)

kuski = Kuljettaja("Räikkönen",44,a1)

a1.kulje(2)

