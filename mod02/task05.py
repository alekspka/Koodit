# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa. (8 512g)
# Yksi naula on 32 luotia. (425,6g)
# Yksi luoti on 13,3 grammaa.

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Naulojen määrä
naulatot = leiviskat * 20 + naulat

# Luotien määrä
luotitot = naulatot * 32 + luodit

# massa grammoina

grammatot = luotitot * 13.3

kilot = grammatot // 1000
grammat = grammatot % 1000

print(f"Massa nykymittojen mukaan: {kilot} kilogrammaa ja {grammat:.2f} grammaa")