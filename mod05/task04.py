# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

citylist = []

for i in range(5):
    kaupunki = input(f"Anna kaupungin nimi: ")
    citylist.append(kaupunki)
print("Kaikki antamanne kaupungit:")
for kaupunki in citylist:
    print(kaupunki)