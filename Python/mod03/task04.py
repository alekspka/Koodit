# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Sano vuosiluku: "))

if vuosi % 4 == 0 or (vuosi % 400 == 0 and vuosi % 100 != 0):
    print("On karkausvuosi.")
else:
    print("Ei ole karkausvuosi.")

# bonus: tulosta kaikki karkausvuodet annettuun vuosilukuun asti

iterator = 0
while iterator < vuosi:
    iterator += 4
    if iterator  % 400 or iterator % 100 != 0:
        print(f"{iterator} on karkausvuosi.")

