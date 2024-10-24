class Hissi:
    def __init__(self,alin_kerros, yli_kerros):
        self.alin_kerros = alin_kerros
        self.yli_kerros = yli_kerros

        self.kerros = alin_kerros

    def siirry_kerrokseen(self,kohdekerros):
        if kohdekerros > self.kerros:
            while kohdekerros > self.kerros:
                self.kerros_ylos()


    def kerros_ylos(self):
        self.kerros += 1

    def kerros_alas(self):
        # TODO totetuta elif-haara alaspäin
        return


h = Hissi(2,10)

h.siirry_kerrokseen(4)
print(h.kerros)
h.siirry_kerrokseen(1) # ei toimi vielä
print(h.kerros)