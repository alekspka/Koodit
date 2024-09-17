import mysql.connector

# connect() -funktio palauttaa tietokantayhteyden, joka sijoitetaan muuttujiin.
mysql.connector.connect(
         host='127.0.0.1', # localhost
         port= 3306,
         database='ihmiset',
         user='username',
         password='password',
         autocommit=True,
         collation='utf8mb4_0900_ai_ci'
         )

# luodaan osoitin ja sijoitetaan muuttujaan
cursor = connection.cursor()
# ajetaan SQL-kielinen kysely osoittimen avulla
cursor.execute('select * from users')

# fetchone hakee rivi kerrallaan, palauttaa monikon
result = cursor.fetchone()
print(result)

# fetchmany() palauttaa halutun määrän rivejä (monikkko) kerrallaan listana
result = cursor.fetchmany()
print(result)

# fetchall palauttaa kaikki (loput) rivit listana
result = cursor.fetchall()
print(result)

#tuloslista käsitellään toistorakeneteella
for row in result:
    print(row[1])
