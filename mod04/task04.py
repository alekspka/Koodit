# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random



oikea_numero = random.randint(1,10)


while True:
    arvaus = int(input("Arvaa numero: "))

    if arvaus < oikea_numero:
        print("Arvaus liian pieni.")
    elif arvaus > oikea_numero:
        print("Arvaus liian iso.")
    else:
        print("Arvasit oikein!")
        break

