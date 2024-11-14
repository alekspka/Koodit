from typing import Collection

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

def fetch_airport_by_icao(code):
    sql = (f"SELECT name, municipality "  
           f"FROM airport WHERE ident='{code}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    print(result_row)
    return result_row

user_input = input("Anna ICAO-koodi: ")
airport = fetch_airport_by_icao(user_input)

if airport != None:
    print(f"Haettu lentokenttä: {airport[0], airport[1]}.")
else:
    print("Lentokenttää ei löydetty annetulla koodilla.")