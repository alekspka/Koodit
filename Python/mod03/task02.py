# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#
# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

user_input = input("Syötä hyttiluokkasi: (LUX, A, B, C) ")

if user_input == "LUX":
    print("LUX on parcelkkeellinen hytti yläkannella.")

elif user_input == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif user_input == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif user_input == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")