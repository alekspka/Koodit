# jatkoa edelllisiin tehtäviin

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self,kohdekerros):
        while kohdekerros > self.kerros:
            self.kerros_ylos()
        while kohdekerros < self.kerros:
            self.kerros_alas()


    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

h = Hissi(2,10)

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissi_lkm = hissi_lkm
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissi_lkm)]

    def aja_hissiä(self, hissinumero, kohdekerros):
        if 0 <= hissinumero < self.hissi_lkm:
            print(f"Ajetaan hissiä {hissinumero + 1} kerrokseen {kohdekerros}.")
            self.hissit[hissinumero].siirry_kerrokseen(kohdekerros)
            self.hissit[hissinumero].siirry_kerrokseen(kohdekerros)
        else:
            print("Hissinumeroa ei ole.")

    def palohälytys(self):
        print("Palohälytys! Kaikki hissit pohjakerrokseen.")
        for i in range(self.hissi_lkm):
            print(f"Hissi {i + 1} palaa pohjakerrokseen.")
            self.hissit[i].siirry_kerrokseen(self.alin_kerros)


talo = Talo(1,10,3)

talo.aja_hissiä(0,6)
talo.aja_hissiä(1,4)
talo.aja_hissiä(2,8)

print("\n")
talo.palohälytys()