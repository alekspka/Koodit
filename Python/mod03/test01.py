rahat = float(input(" Anna rahamääräsi: "))
if rahat >= 5:
    print("Voit ostaa latten, sinulla on tarpeeksi rahaa.")
else:
    print("Voi ei! oot persaukinen.")

suutari = input("Anna suutarin nimi: ")
raatali = input("Anna räätälin nimi: ")

if suutari==raatali:
    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")



luku = int(input("Kerro numero: "))

if luku <0:
    print("Luku on negatiivinen")

if luku ==0:
    print("Luku on nolla")

if luku >0:
    print("Luku on positiivinen")


# monta eri vaihtoehtoa

user_input = input("valitse a, b, tai c: ")
if user_input == "a":
    print("Menkäämme kauppaan")
elif user_input == "b":
    print("Tehdään elokuva")
elif user_input == ("c"):
    print("Lauletaan oopperaa")
else:
    print("Opettele kirjoittamaan")

print("Ohjelma loppuu, moikku.")