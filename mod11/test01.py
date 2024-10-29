class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi, ):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi


    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")


class Tuntipalkkalainen(Työntekijä):

    def __init__(self, etunimi, sukunimi,tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Tuntipalkka: {self.tuntipalkka}€/h")


class Kuukausipalkkalainen(Työntekijä):

    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        self.kuukausipalkka = kuukausipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kuukausipalkka: {self.kuukausipalkka}€")

työntekijät = []
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))
työntekijät.append(Tuntipalkkalainen("Aleksi", "Kaasalainen",25))
työntekijät.append(Kuukausipalkkalainen("Albert", "Järvinen",5000))

for t in työntekijät:
    t.tulosta_tiedot()

print("\n")


class Kulkuneuvo:
    def __init__(self, nopeus):
        self.nopeus = nopeus


class Urheiluväline:
    def __init__(self, paino):
        self.paino = paino


class Polkupyörä(Kulkuneuvo, Urheiluväline):
    def __init__(self, nopeus, paino, vaihteet):
        Kulkuneuvo.__init__(self, nopeus)
        Urheiluväline.__init__(self, paino)

        self.vaihteet = vaihteet


pp = Polkupyörä(45, 18.7, 3)
print(pp.vaihteet)
print(pp.nopeus)
print(pp.paino)
