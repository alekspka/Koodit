# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus = huippunopeus

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


class Sähköauto(Auto):
    def __init__(self, rekkari, huippunopeus, akkukapasiteetti):
        super().__init__(rekkari, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippunopeus, bensatankki_koko):
        super().__init__(rekkari, huippunopeus)
        self.bensatankki_koko = bensatankki_koko





sahkoauto = Sähköauto("ABC-15",180,52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123",165,32.3)

sahkoauto.nopeus = 100
polttomoottoriauto.nopeus = 90

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)







