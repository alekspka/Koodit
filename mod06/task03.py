# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def convert(gallon):
    return  gallon *3.785

while True:
    gallon = int(input("Syötä bensiinimäärä (gallon): "))
    litra=convert(gallon)
    print(f"Bensiinimäärä litroissa: {litra:.2f}")
    if gallon < 0:
        break

