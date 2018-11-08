#!/usr/bin/env python3

# 1d-mol
# jeu du plus ou moins
# 23/10/2018
# Felix Ollivier Drolshagen

# on importe le module signal
import signal

# on import le module random
import random

# on import le module re
import re

# on créé la fonction pour empecher le ctr+c


def fin(sig, frame):
    au_revoir()


signal.signal(signal.SIGINT, fin)

# on créé les variables nécessaires
reg = re.compile('^[0-9]+')
solution = random.randint(0, 100)
rep = -1

# on créé la fonction de fin


def au_revoir():
    print("\b\bmerci d'avoir jouer la solution était ", solution)
    exit()

# on créé une boucle pour le jeu avec les tests nécessaire


while rep != str(solution):
    print('entrer un nombre')
    rep = input()
    if rep == 'q':
        au_revoir()
    elif reg.match(rep):
        if int(rep) > solution:
            print('trop grand')
        elif int(rep) < solution:
            print("trop petit")
    else:
        print("ce n'est pas un chiffre")
au_revoir()
