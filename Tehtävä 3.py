"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
"""

def muunna(gallonat):
    litrat = 3.785 * gallonat
    return litrat

litrat = 0
while litrat >= 0:
    litrat = muunna((float((input("Anna gallonat:\n")))))
    if litrat < 0:
        print("Ohjelma loppuu.")
        break
    print(f"Se on {litrat:.3f} litraa.")