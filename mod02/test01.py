age = input("Anna ikäsi:")
name = "Aleksi"
print("ikäsi on:" + age)

age = int(age) + 1
age_string = str(age)

print("ikäsi on vuoden päästä " + age_string)
age = age + 1
print("Ikäsi on kahden vuoden päästä " + str(age))

# Käyttäjän pituus metreinä
age = 25
height = 1.78

print(f"Nimesi on {name} " + "ja sinä olet " + str(height)  + "cm pitkä. " + "Olet myös " + str(age) + "vuotta vanha.")

height = float(input("anna pituus(m): "))
height = height + 0.1

print(height)