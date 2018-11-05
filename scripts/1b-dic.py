#!/usr/bin/env python3

#1b-dic
#creer une liste des prenoms rentrer
#15/10/2018
#Felix Ollivier Drolshagen

import re

#on creer une regex pour verifier les entrees utilisateurs
reg = re.compile('^[a-zA-Z]+$')

#on creer notre fonction
def dic():
    prenoms = []
    prenom = input("lol entre tes trucs 1 par ligne\n")
    while prenom != "q":
        if reg.match(prenom):
          prenoms.append(prenom)
        else:
            print("n'est pas un prenom")
        prenom = input("")
    prenoms.sort()
    print(", ".join(prenoms))

dic()