# π≈4n/N, jossa N on kaikien pisteiden lukumäärä ja n yksikköympyrän sisällä oleva määrä.
# jos pisteiden koordinaatit toteuttavat epäyhtälön x^2+y^2<1, piste on ympyrässä.
import random


N = 100 # pisteiden kokonaismäärä
n = 0 # ympyrään osuvien pisteiden lukumäärä
iterator = 0

input("Syötä pisteiden kokonaismäärä: ")

while iterator < N:
    iterator += 1

    #arvotaan yksi piste
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvottu piste: {x}, {y}")
    print(x**2 + y**2 < 1)

    if x**2 + y**2 < 1:
        print("Piste on yksikköympyrässä.")
