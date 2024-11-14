# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

# connect() -funktio palauttaa tietokantayhteyden, joka sijoitetaan muuttujiin.
connection = mysql.connector.connect(
         host='127.0.0.1', # localhost
         port= 3306,
         database='flight_game',
         user='root',
         password='ALe19KSi99',
         autocommit=True,
         collation='utf8mb4_general_ci'
         )

def lentoasemat(code):
    sql = (f" SELECT type, COUNT(*) as count "
        f" FROM airport "
        f" WHERE iso_country = '{code}' "
        f" GROUP BY type ")

    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchall()
    return result_row

user_input = input("Anna maakoodi: ")

lentokentat_tyypeittain = lentoasemat(user_input)


if lentokentat_tyypeittain:
    print(f"Lentokentät maassa {user_input}:")
    for row in lentokentat_tyypeittain:
        kentan_tyyppi, maara = row
        print(f"{kentan_tyyppi.capitalize()}: {maara} kappaletta")
else:
    print("Maakoodilla ei löytynyt lentokenttiä.")