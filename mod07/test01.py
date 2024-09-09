"""""
minun_lista = [1,2,3,4,5,6]
print(minun_lista)

minun_monikko = (1,2,3,4,5,6)
print(minun_monikko)

minun_monikko2 = (1,2,(3,4),5,"kuusi")
print(minun_monikko2)

print(minun_lista[0])
print(minun_monikko2[0])

# yritetään muokata

minun_lista[0] = 0
minun_lista.append(7)
print(f"Muokattu lista {minun_lista}")

# Monikon sisältöä EI voi muokata, immutable

viikonpaivat = ("maanantai","tiistai","keskiviikko","torstai","perjantai","lauantai","sunnuntai")
jarjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
print(viikonpaivat[jarjestysnumero-1])
viikonpaiva = viikonpaivat[jarjestysnumero-1]
print(f"{jarjestysnumero} viikonpäivä on {viikonpaiva}.")

# Monikon läpikäynti kuten listan
# minun_monikko = (1,2,3,4,5,6)
nimilista = ("eka","toka","kolmas","neljäs")

for alkio in nimilista:
    print(alkio)
    if alkio == "eka":
        print("eka löytyi!")
print(nimilista)

# Monikon arvojen purku muuttujiin

hedelmat = ("kumkvatti","mandariini","yuzu")
# (eka,toka,kolmas) = ("kumkvatti","mandariini","yuzu")
(eka,toka,kolmas) = hedelmat
print(kolmas)


def tulosta_monikko(nimilista):
    for i in nimilista:
        print(i)

tulosta_monikko(nimilista)
tulosta_monikko(hedelmat)

# perinteinen print ilman paluuarvoa
import random

def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    print(f"Nopista tuli {eka} ja {toka}.")

heitä()

# monikko funtkion paluuarvona

def heitä2():
    eka, toka = random.randint(1,6), random.randint(1,6)
    return (eka, toka)

# (eka, toka) = (noppa1,noppa2)

noppa1, noppa2 = heitä2()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

#JOUKKO eli set {}

# Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä

# Koska joukon alkioille ei ole määritelty järjestystä, ei alkioihin voi myöskään viitata indeksillä.

# Toisin kuin listassa tai monikossa, sama alkio voi esiintyä joukossa vain kertaalleen, eli joukossa ei voi olla kahta samansisältöistä alkiota.

joukko = {1,2,3,4,5,6}
print(joukko)

print(f"Numero kuusi ei voi esiintyä joukossa useasti: ")
minun_joukko = {6,2,3,4,5,6}
print(minun_joukko)

# koodiesimerkki, järjestys voi muuttua printatessa

pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)
pelit.add("yatzy")
print(pelit)

for p in pelit:
    print(p)
if "yatzy" in pelit:
    print("yatzy löytyi!!")

autojoukko = []
autojoukko.append("Mersu")
print(autojoukko)

autojoukko = {}
print(type(autojoukko)) # tämä on <class ´dict´>

autojoukko = set()
autojoukko.add("mersu")
print(type(autojoukko)) # tämä on <class ´set´>
print(autojoukko)
"""""


print("\nSanakirja{}\n")

# Sanakirja (dictionary) on Pythonin käytetyimpiä tietorakenteita.
# Sanakirjaan voidaan tallentaa avain-arvopareja.
# Kun sanakirja alustetaan arvot luettelemalla, annetaan kukin avain-arvopari seuraavasti: avain : arvo. Peräkkäiset avain-arvoparit erotellaan toisistaan pilkulla.

oppilaat = {"Albert": 25,"Kofi": 23, "Rita": 30,"Kimi": 19}
print(oppilaat)

# mitä ovat tietueet / items
print(oppilaat.items())

# mitä ovat avaimet sanakirjassa?
print(oppilaat.keys())

# mitä ovat arvoja sanakirjassa?
print(oppilaat.values())

# kun sanakirjaa käydän läpi for/in rakenteella:

# tietueet eli avain-arvoparit
for i in oppilaat.items():
    print(i)

for i in oppilaat:
    print(i)

#yksittäisen arvon haku avaimen avulla
avain = "Kofi"
print(oppilaat[avain]) # etsii avaimella Kofi sen arvoa joka on 23

# etsi kaikki arvot

for i in oppilaat:
    print(oppilaat[i])
"""""
# if / in rakenteella voidaan myös hakea sanakirjasta tietoa
nimi = input("Anna nimi, niin etsin tietoa sanakirjasta jos löytyy: ")
if nimi in oppilaat:
    print(f"Löytyi oppilas {nimi} ikä hänellä on {oppilaat[nimi]}")
"""""

# Kun olemassa olecaan sanakirjaan lisätään arvo, käytetään sanakirja[avain) = arvo
# Lisätään uusi oppilas mikäli ei löydy
# jos avain löytyy, se muokkaa olemassa olevaa, muuten luodaan uusi.

oppilaat["Allu"] =  22
print(oppilaat)