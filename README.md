# Projet-S2
wow
ragondin
lol
mdr
##########################
# Auteur: Pierre Coucheney

########################
# import des librairies

import tkinter as tk
importer aléatoire en tant que rd


########################
# constantes

# hauteur du canvevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
# taille de la grille
N = 3

# paramètres de l’automate:
# probabilité d’être un mur à l’initialisation:
P = 0,5

# choix des couleurs

COUL_MUR = « gris »
COUL_LIBRE = « blanc »


############################
# variables globales
terrain = []
grille = []




####################
# fonctions

def init_terrain():
    « ""Initialiser le terrain:
    * initialiser la liste carrée terrain à 2D de taille N telle
    que la case de coordonnées (i,j) vaut 1 si il y a un mur
    dessus et 0 sinon
    * initialiser la liste carrée grille à 2D de taille N
 telle que la case de coordonnées (i,j) contient l’identifiant
    du carré dessiné sur le canevas 
    * Une case est un mur avec probabilité P
    """
    calandre globale, terrain
    pour i dans la plage (N):
        calandre. append([0]*N)
        terrain. append([0]*N)

    pour i dans la plage (N):
        pour j dans la plage (N):
            si rd. uniforme(0, 1) < P:
                terrain[i][j] = 1
                coul = COUL_MUR
            sinon:
                terrain[i][j] = 0
                coul = COUL_LIBRE
            largeur = LARGEUR // N
            hauteur = HAUTEUR // N
            x1 = largeur * i
            y1 = hauteur * j
            x2 = largeur * (i+1)
            y2 = hauteur * (j + 1)
            carré = toile. create_rectangle((x1, y1), (x2, y2), fill=coul)
            grille[i][j] = carré
        





#########################
# partie principale

# création des widgets
racine = tk. Tk()
racine. title(« Génération de terrain »)
toile = tk. Canvas(racine, height=HAUTEUR, width=LARGEUR)

# placement des widgets
toile. grille(colonne=1, ligne=0)


init_terrain()

# boucle principale
racine. boucle principale()