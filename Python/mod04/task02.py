# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm


cm = 2.54
while True:
    tuuma = float(input("Syötä tuumamäärä: "))


    if tuuma < 0:
        print("Ohjelma lopetetaan.")
        break

    senttimetrit = tuuma * cm


    print(f"{tuuma} tuumaa on {senttimetrit:.2f} senttimetriä. ")
