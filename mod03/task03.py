# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Kerro sukupuolesi: (mies/nainen) ")

hgarvo = float(input("Mikä on sinun hemoglobiiniarvo?: (g/l)"))

#normi hg-arvot

m_norm_min = 134
m_norm_max = 195
n_norm_min = 117
n_norm_max = 175

if sukupuoli == "mies":
    if hgarvo < m_norm_min:
        print("sinulla on alhaiset hemoglobiiniarvot.")
    elif hgarvo > m_norm_max:
        print("Sinulla on korkeat hemoglobiiniarvot.")
    else:
        print("Hemoglobiiniarvosi ovat normaalit.")

if sukupuoli == "nainen":
    if hgarvo < n_norm_min:
        print("sinulla on alhaiset hemoglobiiniarvot.")
    elif hgarvo > n_norm_max:
        print("Sinulla on korkeat hemoglobiiniarvot.")
    else:
        print("Hemoglobiiniarvosi ovat normaalit.")


