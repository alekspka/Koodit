class Työntekijä:
    def __init__(self,nimi):
        self.nimi = nimi

class Tuntipalkkalainen(Työntekijä):
    def __init__(self,nimi,palkka):
        super().__init__(nimi)
        self.palkka = palkka
