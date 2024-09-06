# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random


n = int(input("Anna arpakuutioiden määrä: "))

summa = 0

for i in range(n):
    heitto = random.randint(1,6)
    print(f"Arpakuuttio {i+1}: {heitto}")

    summa += heitto

print(f"Arpakuutioiden heittojen summa: {summa}")



