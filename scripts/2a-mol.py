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
end = False
print(solution)
#on créé la fonction de fin
def fin():
    print("Au revoir, merci d'avoir jouer")
    exit()
#on créé la fonction pour écrire dans un fichier
def write_file(msg):
  file = open("jeu.txt", "w")
  file.write(msg)
  file.close()
#on créé la fonction pour lire dans le fichier
def read_file():
  file = open("jeu.txt", "r")
  msg = file.read()
  file.close()
  return msg
#fonction anti ctrlC 
def stop_ctrlC(sig, frame):
    write_file('Pas ouf de CTRL+C ')
    exit()

signal.signal(signal.SIGINT, stop_ctrlC)

write_file("Bienvenue dans le jeu du plus ou moins, veuillez entrez un chiffre entre 0 et 100")

#on initialise la boucle pour le jeu
while end is False :
    #On va lire dans le file 
    saisi = read_file()
     #On vérifie la saisie utilisateur
    if re.match("^[0-9]+$", saisi):
        saisi = int(saisi)
        if saisi > 100:
            continue          
        if saisi > solution :
            write_file('Trop grand !')       
        elif saisi < solution :
            write_file('Trop petit !')
        #Sinon on affiche le message de victoire et on arrete la boucle avec end=True 
        else :
            write_file('Gg a toi ! ')
            end = True
            fin()