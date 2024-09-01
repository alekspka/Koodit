# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).


user = "python"
passu = "rules"

yri = 0
max_yri = 5


while yri < max_yri:

    user_input = input("Syötä käyttäjätunnus: ")
    user_input1 = input("syötä salasana: ")
    if user_input == user and user_input1 == passu:
        print("Pääsy sallittu.")
        break
    else:
        print("Virheelliset kirjautumistiedot, yritä uudelleen.")
        yri += 1
    if yri == max_yri:
        print("Pääsy kielletty.")

