# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def nopanheitto():
    return random.randint(1,6)

while True:
    noppaluku = nopanheitto()
    print(f"Heitin: {noppaluku}")

    if noppaluku == 6:
        break

