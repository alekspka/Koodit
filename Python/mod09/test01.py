"""""
class LuokanNimi:


    def __init__(self, parametri1, paramteri2):
        self.atribuutti1 = parametri1
        self.atribuutti2 = paramteri2

    def metodi(self):
        return

    def metodi2(self):
        return


class Koira:

    def __init__(self, nimi, syntymäuosi, väri, koko, haukahdus):
        self.nimi = nimi
        self.syntymävuosi = syntymäuosi
        self.väri = väri
        self.koko = koko
        self.haukahus = haukahdus

    def printtaa_tiedot(self):
        print(f"Koiran nimi on {self.nimi} ja syntymävuosi on {self.syntymävuosi}")
        return


    def hauku(self, kerrat):
        print(f"Koiran nimi on {self.nimi} ja haukkuu näin monta kertaa: {kerrat}")
        for i in range(kerrat):
            print(self.haukahus)
        return


k1 = Koira("Siru",2012, "musta", "keskikokoinen","hau hau")
k2 = Koira("Rosa",2013,"beige","pieni", "slatt")
k3 = Koira("Toni",1999, "pinkki","massiivinen","moi")


k2.hauku(5)
k1.hauku(3)

Koira.printtaa_tiedot(k1)

"""""
class Kuljettaja:
    def __init__(self, nimi, ika, auto):
        self.nimi = nimi
        self.ika = ika
        self.auto = auto

    def aja(self):
        print(f"Olen{self.nimi}, {self.ika} ja ajan autoa {self.auto.rekkari}")
        self.auto.kiihdytys(40)
        print(self.auto.nopeus)
        self.auto.kiihdytys(140)

class Auto:
    def __init__(self, rekkari, nopeus):
        self.rekkari = rekkari
        self.nopeus = 0
        self.huippunopeus = 100
        self.kuljettaja = "Räikkönen"

    def tulosta_rekkari(self):
        print(f"Auton rekkari on: {self.rekkari}")

    def kiihdytys(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0



a1 = Auto("ABC-123", 142)
a2 = Auto("DEF-123", 250)
kuski = Kuljettaja("Räikkönen",44,a1)

kuski.aja()