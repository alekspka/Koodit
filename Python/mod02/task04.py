#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

# kolme numeroa

luku1= int(input("Ensimmäinen kokonaisluku"))
luku2= int(input("Toinen kokonaisluku"))
luku3= int(input("Kolmas kokonaisluku"))

summa = luku1 + luku2 + luku3

tulo = luku1 * luku2 * luku3

keskiarvo = summa/3

print(f"lukujen summa= {summa}")
print(f"lukujen tulo= {tulo}")
print(f"lukujen keskiarvo= {keskiarvo:.2f}")

