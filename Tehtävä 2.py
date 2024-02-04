"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""
import random
def heita(tahkot):
    tulos = random.randint(1, tahkot)
    return tulos

tahkojen_lkm = int(input("Anna tahkojen määrä: "))
max_luku = tahkojen_lkm

while True:
    tulos = heita(tahkojen_lkm)
    if tulos == max_luku:
        print(f"Sait tulokseksi {max_luku}!")
        break
    else:
        print(f"Heiton tulos: {tulos}")