# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def laske(lista):
    summa = sum(lista)
    return summa

def listaohjelma():
    lista = []
    while True:
        syote = input("Syötä nro: (lopeta vastaamatta jättämällä) ")
        if syote == "":
            break
        numero = int(syote)
        lista.append(numero)

    tulos = laske(lista)
    print(f"Listan lukujen summa: {tulos}")

listaohjelma()
