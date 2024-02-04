"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
"""
import random
def heita():
    tulos = random.randint(1, 6)
    return tulos

while True:
    tulos = heita()
    if tulos == 6:
        print("Sait kuutosen!")
        break
    else:
        print(f"Heiton tulos: {tulos}")