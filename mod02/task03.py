# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan. Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = float(input("mikä on suorakulmion kanta?(m)"))
korkeus = float(input("Mikä on suorakulmion korkeus?(m)"))

piiri = kanta * 2 + korkeus * 2
pinta_ala = kanta * korkeus

print(f"Suorakulmion piiri on: + {piiri:.0f} metriä + ja pinta-ala: + {pinta_ala:.0f} neliömetriä")



