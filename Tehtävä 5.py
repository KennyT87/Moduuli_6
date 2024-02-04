"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
"""
def anna_parilliset(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

luvut = []
while True:
    luku = input("Lisää kokonaisluku listaan.\n(Enter palauttaa alkuperäiset ja parilliset luvut):\n")
    if luku == "":
        print("Ohjelma loppuu.")
        break
    else:
        luvut.append(int(luku))

parilliset = anna_parilliset(luvut)
print(f"Alkuperäiset luvut: {luvut}\nParilliset luvut: {parilliset}")