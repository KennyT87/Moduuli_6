"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
(eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""
import math
def laske_hinta(halkaisija_cm, hinta_euro):
    sade_cm = halkaisija_cm / 2
    sade_m = sade_cm / 100
    ala_m2 = math.pi * sade_m**2
    suht_hinta = hinta_euro / ala_m2
    return suht_hinta


halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))
halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

suht_hinta1 = laske_hinta(halkaisija1, hinta1)
suht_hinta2 = laske_hinta(halkaisija2, hinta2)

if suht_hinta1 < suht_hinta2:
    print("Ensimmäinen pizza on suhteessa edullisempi.")
elif suht_hinta1 > suht_hinta2:
    print("Toinen pizza on suhteessa edullisempi.")
else:
    print("Molemmat pizzat ovat suhteessa yhtä edullisia.")