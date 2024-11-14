# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

def kysy_nimet():
    nimet = set()

    while True:
        nimi = input("Anna nimi (tyhjä syöte lopettaa): ")

        if nimi == "":
            break
        if nimi in nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet.add(nimi)

    return nimet


def tulosta_nimet(nimet):
    print("\nSyötetyt nimet:")
    for nimi in nimet:
        print(nimi)

syötetyt_nimet = kysy_nimet()
tulosta_nimet(syötetyt_nimet)

