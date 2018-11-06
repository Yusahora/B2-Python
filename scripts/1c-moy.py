#!/usr/bin/env python3

# 1c-moy
# creer un dictionnaire de nom/note et ressort les 5 meilleurs note
# 15/10/2018
#  Felix Ollivier Drolshagen
import re
import operator

# on creer une regex pour verifier les entrees utilisateurs
reg = re.compile('^[a-zA-Z]+$')
reg2 = re.compile('^[0-9]+')

Dict = {}
best = []
loop = 0
sum = 0
while loop == 0:
    print("saisissez un prenom")
    nom = input()
    if reg.match(nom):
        if nom == "q":
            for liste in sorted(Dict):
                best = Dict[liste]
                sum += int(best)
            print("moyenne est égale a ")
            moy = round(sum / len(Dict), 2)
            print(moy)
            print("liste des notes")
            print(sorted(Dict.items(), key=operator.itemgetter(1), reverse=True)[:5])
            break

        else:

            print("saisissez votre note")
            note = input()
            if reg2.match(note):
                try:
                    note = int(note)
                except ValueError:
                    pass
                Dict[nom] = note
            else:
                print("n'est pas un nombre")
    else:
        print("n'est pas un")
