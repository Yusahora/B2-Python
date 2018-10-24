#!/usr/bin/env python3

#1d-mol
#jeu du plus ou moins dans un fichier
#23/10/2018
#Felix Ollivier Drolshagen

#on importe le module signal
import signal

#on import le module random
import random

#on import le module re
import re

#on créé les variables nécessaires
reg = re.compile('^[0-9]+')
solution = random.randint(0, 100)
print(solution)
fichierW = open("jeu.txt", "w")
fichierW.write("bienvenue dans le jeu du plus ou moins")
fichierW = open("jeu.txt", "r")
#on créé la boucle dans lequel sera le jeu
print(fichierW.read())
#while fichier.read() != solution:
#    fichier.write(input)
#fichier.close