nimi1 = "Aleksi"
nimi2 = "Petteri"
nimi3 = "Rita"

age1 = 25
age2 = 50
age3 = 20

print(f"Hei {nimi1}, ikäsi on {age1}.")
print(f"Hei {nimi2}, ikäsi on {age2}.")
print(f"Hei {nimi3}, ikäsi on {age3}.")
print("--------")

nimet = ("Aleksi", "Petteri", "Rita", "Tuomo", "Tapani")
nimet2 = (nimi1, nimi2, nimi3)
ages = (age1, age2, age3, 27, 69)

#listan pituus
length = len(nimet)
print(f"Listan pituus on: {length} ")

# Alkioon viitataan indekisnumerolla

"""""
print(f"Hei {nimet[2]}! Ikäsi on {ages[0]}.")

# listan läpikäynti while, silmukan avulla.

iterator = 0
while iterator < len(nimet):
    print(f"Hei {nimet[iterator]}! Ikäsi on {ages[iterator]}.")
    iterator += 1


# tapoja viitata listan alkioihin

lista = ("Juho", "Kiri", "Leo", "Kofi","Matilda", "Pablo", "Ada")
print(lista[-1:-6:-2])

# listaan voi yhdistää ja siellä voi olla erilaisia tietorakenteita

lista1 = ("Albert", "Töpö", "Iisu")
lista2 = (23, 66, 10, 77, lista1)
print(lista2)
print(lista2[4][2])
"""""

print("\n----------")
print("LISTAOPERAATIOT")

lista = ["Juho", "Kiri", "Leo", "Kofi", "Matilda", "Pablo", "Ada", "Ismo"]

if "Leo" in lista:
    print("Leo löytyy listalta, poistetaan")
    lista.remove("Leo")
    print(lista)

lista.insert(2,"Seppo")
print(lista)


print(lista.index("Kofi"))

lisaa_nimia =["Joonas","Jehova", "Akira"]
uusi_lista = lista + lisaa_nimia # lisätään nimiä
print(uusi_lista)

uusi_lista[2] = "Sebbo" # muokataan olemassa olevaa alkiota
print(uusi_lista)

uusi_lista.sort()
print(uusi_lista)
"""""
for alkio in "abcde":
    print(alkio)

for nimi in uusi_lista:
    print(nimi)

for numero in range (500,5,-50):
    print(numero)
"""""
# käytetään edellä olevia iteroimaan nimilistaa läpi

print(uusi_lista)
for i in range (len(uusi_lista)):
    print(f"Terve {uusi_lista[i]} ")