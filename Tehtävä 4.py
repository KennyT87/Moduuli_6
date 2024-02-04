"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
"""
def laske_summa(lista):
    return sum(lista)

lista = []
while True:
    luku = input("Lisää kokonaisluku listaan.\n(Enter palauttaa lukujen summan):\n")
    if luku == "":
        print("Ohjelma loppuu.")
        break
    else:
        lista.append(int(luku))

summa = laske_summa(lista)
print(f"Listan lukujen summa on {summa}")