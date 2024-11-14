# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.


def is_prime_number(num):
    if num < 1:
        return False

    for i in range(2,num):
        print(i)
        if num % i == 0:
            # jos jaollinen jollain i:n arvolla, palautetaan False ja funktion suoritus loppuu siihen.
            return False
        # jos funktion suoritus on jatkunut tänne asti, niin palautetaan True
        return True

user_input = int(input("Syötä testattava kokonaisluku (>0): "))

if is_prime_number(user_input):
    print(f"Luku {user_input} on alkuluku.")
else:
    print(f"Luku {user_input} ei ole alkuluku.")