#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

pituus = float(input("Mikä on kuhan pituus? (cm) "))

alin_pituus = 37

if pituus < alin_pituus:
    puuttuva_pituus = alin_pituus - pituus
    print(f"Kuha on {puuttuva_pituus} centtimetriä liian lyhyt. Laske kuha takaisin järveen.")
else:
    print("Voit viedä kuhan kotiin.")


