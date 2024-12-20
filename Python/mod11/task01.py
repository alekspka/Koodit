# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    def __init__(self, nimi, vuosi):
        self.nimi = nimi
        self.julkaisuvuosi = vuosi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi} ja julkaisuvuosi: {self.julkaisuvuosi} ")


class Kirja(Julkaisu):

    def __init__(self,nimi, julkaisuvuosi, kirjoittaja, sivumäärä):
        super().__init__(nimi, julkaisuvuosi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja} ja sivumäärä: {self.sivumäärä}")


class Lehti(Julkaisu):

    def __init__(self,nimi, julkaisuvuosi, päätoimittaja):
        super().__init__(nimi,julkaisuvuosi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.päätoimittaja}")

k = Kirja("Hytti n:o 6", 2012,"Rosa Liksom", 200)

l = Lehti("Aku Ankka",2021,"Aki Hyyppä")

k.tulosta_tiedot()
l.tulosta_tiedot()