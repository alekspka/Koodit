# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

talvi = ["joulukuu","tammikuu","helmikuu"]
kevät = ["maaliskuu","huhtikuu","toukokuu"]
kesä = ["kesäkuu", "heinäkuu", "elokuu"]
syksy = ["syyskuu", "lokakuu", "marraskuu"]

kuukausi = input("Anna joku kuukausi: ")

if kuukausi in talvi:
    print("Vuodenaika on talvi")
elif kuukausi in kevät:
    print("Vuodenaika on kevät")
elif kuukausi in syksy:
    print("Vuodenaika on syksy")
elif kuukausi in kesä:
    print("Vuodenaika on kesä")
else:
    print("Antamanne kuukausi ei ole kelvollinen")