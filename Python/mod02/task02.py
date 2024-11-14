# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
import math

r = float(input("Mikä on ympyrän säde?(m): "))

pinta_ala = math.pi * r **2

print(f"Ympyrä, jonka säde on {r}, pinta-ala on: {pinta_ala:.1f} neliömetriä.")
