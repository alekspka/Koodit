# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston avulla:
import mysql.connector
from geopy.distance import great_circle

connection = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'aleksi',
        password = 'passu123',
        autocommit = True,
        collation = 'utf8mb4_general_ci')

def koordinaatit(icao):
    sql = (f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def etäisyys(koord1, koord2):
    return great_circle(koord1, koord2).kilometers

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

koordinaatit1 = koordinaatit(icao1)
koordinaatit2 = koordinaatit(icao2)

if koordinaatit1 and koordinaatit2:
    etaisyys = etäisyys(koordinaatit1, koordinaatit2)
    print(f"Lentokenttien etäisyys: {etaisyys:.2f} kilometriä")
else:
    print("Yksi tai molemmat ICAO-koodit eivät ole voimassa.")

connection.close()