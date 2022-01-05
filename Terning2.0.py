import random as r
from typing import TextIO

terning = r.randint(1,6)

EN = '\u2680'
TO = '\u2681'
TRE = '\u2682'
FIRE = '\u2683'
FEM = '\u2684'
SEKS = '\u2685'

""" print(EN, TO, TRE, FIRE, FEM, SEKS) """


def omformer(tall):
    if int(tall)==1:
        print(EN)
    elif int(tall)==2:
        print(TO)
    elif int(tall)==3:
        print(TRE)
    elif int(tall)==4:
        print(FIRE)
    elif int(tall)==5:
        print(FEM)
    else:
        print(SEKS)

""" denne henter ut det tilfeldige tallet fra terning-variablen og 
skriver ut symbolet som viser samme tall i terningformat """


def kast():
    kaste = input("Enter for å kaste:")
    if kaste == "":
        omformer(terning)


kast()
    


