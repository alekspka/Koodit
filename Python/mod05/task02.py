# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

nrolista = []

while True:
    nro = (input("Syötä joku numero: "))

    if nro == "":
        print("Lopetetaan")
        break
    nrolista.append(int(nro))
nrolista.sort(reverse=True)
print("Listan suurimmat luvut ovat: ")
for i in nrolista[:5]:
        print(i)



