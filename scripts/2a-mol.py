#!/usr/bin/env python3

# 1d-mol
# jeu du plus ou moins dans un fichier
# 23/10/2018
# Felix Ollivier Drolshagen

# on importe le module signal
import signal

# on import le module random
import random

# on import le module re
import re

# on créé les variables nécessaires
reg = re.compile('^[0-9]+')
solution = random.randint(0, 100)
end = False
# on créé la fonction de fin


def fin():
    print("Au revoir, merci d'avoir jouer")
    exit()
# on créé la fonction pour écrire dans un fichier


def write_file(msg):
    file = open("jeu.txt", "w")
    file.write(msg)
    file.close()
# on créé la fonction pour lire dans le fichier


def read_file():
    file = open("jeu.txt", "r")
    msg = file.read()
    file.close()
    return msg
# fonction anti ctrlC


def stop_ctrlC(sig, frame):
    write_file("Pas ouf de CTRL+C ")
    exit()


signal.signal(signal.SIGINT, stop_ctrlC)

write_file("Veuillez entrez un chiffre entre 0 et 100")
print(solution)

# on initialise la boucle pour le jeu
while end is False:
    # On va lire dans le file
    saisi = read_file()
    # On vérifie la saisie utilisateur
    if reg.match(saisi):
        saisi = int(saisi)
        if saisi > solution:
            write_file("Trop grand !")
        elif saisi < solution:
            write_file("Trop petit !")
        # Fin du jeu et fin de la boucle
        else:
            write_file("Bien jouer")
            end = True
            fin()
