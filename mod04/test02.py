""""

print(1 == 1)
print(1<3 or 2>1)


max_count = int(input("Kuinka monta kertaa kukutaan? "))
counter = 0
while counter < max_count:
    counter= counter + 1
    print(f"{counter}. kerran kukkuu")
print(f"laskurin arvo lopuksi: {counter}")
"""
import random

# Ohjelma komentorivikäyttöliittymä
command = ""
while command != "lopeta":
    command = input("Syötä komento ")
    if command == "lopeta":
        print("Lopetetaan.")
        #break "heittää ulos" silmukasta.
    elif command == "kukkuu":
        max_count = int(input("Kuinka monta kertaa kukutaan? "))
        counter = 0
        while counter < max_count:
            counter = counter + 1
            print(f"{counter}. kerran kukkuu")
        print(f"laskurin arvo lopuksi: {counter}")
    elif command == "noppa":
        rounds = 1000
        round_counter = 0
        total_rolls = 0
        while round_counter < rounds:
            round_counter += 1
            die1 = die2 = roll_counter = 0
            while die1 < 6 or die2 < 6:
                roll_counter += 1
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                print(f"{roll_counter}. Heittojen silmäluvut: {die1} ja {die2}")
            print(f"Noppaa heitettiin {roll_counter} kertaa.")
            total_rolls = total_rolls + roll_counter
        print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla per kierros.")
    else:
        print("En ymmärrä komentoa. Yritä uudelleen.")

print("Ohjelma suljettu.")
