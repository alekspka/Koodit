class LuokanNimi:

    def __init__(self, parametri1, paramteri2):
        self.atribuutti1 = parametri1
        self.atribuutti2 = paramteri2

    def metodi(self):
        return

    def metodi2(self):
        return


class Koira:

    def __init__(self, nimi, syntymäuosi, väri, koko):
        self.nimi = nimi
        self.syntymävuosi = syntymäuosi
        self.väri = väri
        self.koko = koko

    def printtaa_tiedot(self):
        print(f"Koiran nimi on {self.nimi} ja syntymävuosi on {self.syntymävuosi}")
        return


k1 = Koira("Siru",2012, "musta", "keskikokoinen")
k2 = Koira("Rosa",2013,"beige","pieni")

print(k1.koko)
print(k2.väri)

k1.printtaa_tiedot()
k2.printtaa_tiedot()

