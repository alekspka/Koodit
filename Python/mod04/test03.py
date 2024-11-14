# noppapeli
""""
import random

rounds = 1000
round_counter = 0
total_rolls = 0
while round_counter < rounds:
    round_counter += 1
    die1 = die2 = roll_counter = 0
    while die1 < 6 or die2 < 6:
        roll_counter += 1
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"{roll_counter}. Heittojen silmäluvut: {die1} ja {die2}")
    print(f"Noppaa heitettiin {roll_counter} kertaa.")
    total_rolls = total_rolls + roll_counter
print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla per kierros.")
"""