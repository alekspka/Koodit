# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

def uusi_asema(lentoasemat):
    icao = input("Anna lentoaseman ICAO-koodi: ")
    nimi = input("Anna lentoaseman nimi: ")
    lentoasemat[icao] = nimi

def hae_asema(lentoasemat):
    icao = input("Anna lentoaseman ICAO-koodi: ")
    if icao in lentoasemat:
        print(f"Lentoaseman {icao} nimi on {lentoasemat[icao]}.")
    else:
        print("Lentoasemaa ei löytynyt.")


def main():
    lentoasemat = {}
    while True:
        valinta = input("Mikäli halautte lisätä uuden aseman, paina 1. "
                        "Mikäli haluatte etsiä asemaa, paina 2. "
                        "Mikäli haluatte lopettaa, paina 3.: ")
        if valinta == "1":
          uusi_asema(lentoasemat)
        elif valinta == "2":
         hae_asema(lentoasemat)
        elif valinta == "3":
            print("ohjelma lopetaan.")
            break
        else:
            print("Virheellinen valinta, syötä uudelleen.")

main()
