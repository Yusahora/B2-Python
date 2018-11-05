#!/usr/bin/env python3

#1a-add
#additionne deux chiffres
#15/10/2018
#Felix Ollivier Drolshagen

import re

#on creer une regex pour verifier les entrees utilisateurs
reg = re.compile('^[0-9]+')

#on demande les nombres
print("entrer les deux nombre à additionner")
nombre1 = input()
nombre2 = input()
#on creer notre fonction
def add(nb1, nb2):
    if reg.match(str(nb1)) and reg.match(str(nb2)):
        res = int(nb1) + int(nb2)
        print(res)
    else:
        print("ce n'est pas un nombre")
  
#on appelle la fonction
add(nombre1, nombre2)
