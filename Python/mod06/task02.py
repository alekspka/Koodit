# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def nopanheitto(max_noppa):
    return random.randint(1,max_noppa)
user_input = int(input("Anna nopan maksimisilmäluku: "))
max_noppa = user_input

while True:
    noppaluku = nopanheitto(max_noppa)
    print(f"Heitin: {noppaluku}")

    if noppaluku == max_noppa:
        break
