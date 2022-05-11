import tkinter as tk 
import random as rd
from random import randint, choice, random


#definition du canvas
COTE = 600
GRILLE = 30
CARRE = COTE//GRILLE

#definition du chrono
CHRONO = 500
var_chrono = 0

#definition des differentes listes
grille  = []
proies =  []
predateurs = []


#definition des regles de vie 
life = 20 #nombre de tour auxquels l'animal va survivre
Nproie = 100 #nombre de proie initaux
Npreda = 3 #nombre de predateur initaux
ENERGIE = 15 #energie du predateur
MIAM = 5 #energie regagner par le predateur lorsqu"il mange une proie
Rproie = 20 #nombre de nouvelle proies par tour
Rpreda = 20 #nombre d'energie qu'il faut à un predateur pour se reproduire 

            
def mouvement_mort_proies() : 
    """permet a la proies de bouger autour d'elle"""
    mv = [[0,-1],[0,1],[-1,0],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]] #listes des differentes position pouvant etre prise
    a_delete = []
    a_ajouter = []
    for p in proies : #pour chaque proies, on ajoute aux coordonnée + ou - 1 pour les deplacer 

        move = canvas.find_overlapping(p[0][0]*CARRE,p[0][1]*CARRE,p[0][0]*CARRE+CARRE,p[0][1]*CARRE+CARRE) 
        canvas.delete(move[0]) #on supprime le canvas de l'ancienne position
        a_delete.append(p) #on ajoute a une liste ou on stock les anciennes positions de la proies
        
        if p[1] != 0 : #si la vie n'est pas egal a 0 alors on choisie de nouvelle position
            p[1] -= 1
            MV = rd.choice(mv)
            a,b = MV[0], MV[1]
            coord = [[p[0][0]+a,p[0][1]+b],p[1]] 

            while coord[0] not in grille : #si les coordonées ne sont pas dans la liste des position libre on refait un tirage aleatoire
                MV = rd.choice(mv)
                a,b = MV[0], MV[1]
                coord = [[p[0][0]+a,p[0][1]+b],p[1]]


            a_ajouter.append([coord, p[1]]) #on stock dans une liste les coordonée a rajouté dans la liste des proies

            canvas.create_rectangle(coord[0][0]*CARRE,coord[0][1]*CARRE,coord[0][0]*CARRE+CARRE,coord[0][1]*CARRE+CARRE, fill = "blue") #on creer le canvas aux nouvelle positions

    for p in a_delete :
        proies.remove(p) #on retire les anciennes coordonnées de la proie
        grille.append(p[0]) #on ajoute les anciennes coordonnées a la liste des positions libres

    for p in a_ajouter :
        proies.append([p[0][0],p[0][1]]) #on ajoute aux proies les nouvelles coordonnées

   


def mouvement_mort_Preda() :
    """ permet au predateur de bouger autour de lui """
    mv = [[0,-1],[0,1],[-1,0],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]] 
    mv = [[0,-1],[0,1],[-1,0],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]] #listes des differentes position pouvant etre prise
    a_delete = []
    a_ajouter = []
    for p in predateurs : #pour chaque predateur, on ajoute aux coordonnée + ou - 1 pour les deplacer 

        move = canvas.find_overlapping(p[0][0]*CARRE,p[0][1]*CARRE,p[0][0]*CARRE+CARRE,p[0][1]*CARRE+CARRE)
        canvas.delete(move[0])
        a_delete.append(p) 
        if p[2] != 0 :  #si la vie ou l'energie n'est pas egal a 0 alors on choisie de nouvelle position
            p[2] -= 1
            if p[1] != 0 :
                p[1] -= 1
                MV = rd.choice(mv)
                a,b = MV[0], MV[1]
                coord = [[p[0][0]+a,p[0][1]+b],p[1],p[2]] 

                while coord[0] not in (grille or proies[0][0]): #si les coordonées ne sont pas dans la liste des position libre on refait un tirage aleatoire
                    MV = rd.choice(mv)
                    a,b = MV[0], MV[1]
                    coord = [[p[0][0]+a,p[0][1]+b],p[1],p[2]]


                a_ajouter.append([coord]) #on stock dans une liste les coordonée a rajouté dans la liste des predateurs
                canvas.create_rectangle(coord[0][0]*CARRE,coord[0][1]*CARRE,coord[0][0]*CARRE+CARRE,coord[0][1]*CARRE+CARRE, fill = "red")  #on creer le canvas aux nouvelle positions


    for p in a_delete :
        predateurs.remove(p) #on retire les anciennes coordonnées de la predateur
        grille.append(p[0]) #on ajoute les anciennes coordonnées a la liste des positions libres

    for p in a_ajouter :
        predateurs.append([p[0][0],p[0][1],p[0][2]]) #on ajoute aux predateurs les nouvelles coordonnées
            
        

def passage_tours():
    """permet le passage de tour tout les x temps """
    global var_chrono
    var_chrono = canvas.after(CHRONO, tour) #tout les x temps la fonction tour est lancé
    

#definitiopn de la reproduction
def tour():
    """permet de lancer toutes le definition a chaque tour """
    passage_tours()
    reproduction_proies()
    mouvement_mort_proies() 
    mouvement_mort_Preda()
    energie()

 
#creer proies et des predateur
def creer_animaux():
    """ creer les proies et predateurs initiaux """
    for p in range(Nproie): #creation des proies inital
        coord = choice(list(grille)) #on choisit aleatoirement des positions dans la liste des positions libre
        canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "blue") #on creer un canvas aux coordonnées choisit
        proies.append([coord,life]) #on ajoute a la liste des proies les coordonnées selectionné et la variable vie
        grille.remove(coord) #on retire de la liste des positions libre la position selectionnée

    
    for p in range(Npreda) : #creations des predateurs inital
        coord = choice(list(grille)) #on choisit aleatoirement des positions dans la liste des positions libre
        canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "red") #on creer un canvas aux coordonnées choisit
        predateurs.append([coord,life,ENERGIE]) #on ajoute a la liste des predateurs les coordonnées selectionné, la variable vie et la variable ENERGIE
        grille.remove(coord) #on retire de la liste des positions libre la position selectionnée


def reproduction_proies() :
    """ permet la reproduction de N proies """
    for p in range(Rproie): #reproduction des proies a chaque tours
        coord = [choice(list(grille)), life] #on choisit aleatoirement des positions dans la liste des positions libre
        canvas.create_rectangle(coord[0][0]*CARRE,coord[0][1]*CARRE,coord[0][0]*CARRE+CARRE,coord[0][1]*CARRE+ CARRE, fill = "blue") #on creer un canvas aux coordonnées choisit
        proies.append(coord) #on ajoute a la liste des proies les coordonnées selectionné et la variable vie
        grille.remove(coord[0]) #on retire de la liste des positions libre la position selectionnée



def energie() :
    for p in predateurs :
        for k in proies :
            if p[0] == k[0] : #condition si une proies et un predateur on la même position
                p[2] += MIAM #ajouter la variable MIAM à l'energie du predateur
                mort = canvas.find_overlapping(p[0][0]*CARRE,p[0][1]*CARRE,p[0][0]*CARRE+CARRE,p[0][1]*CARRE+ CARRE)
                canvas.delete(mort[0])
                canvas.create_rectangle(p[0][0]*CARRE,p[0][1]*CARRE,p[0][0]*CARRE+CARRE,p[0][1]*CARRE+ CARRE, fill = "red")

    for p in predateurs :
        if p[2] > Rpreda :  #condition si un predateur atteint une certain seuil d'energie 
            coord = choice(list(grille)) #on choisit aleatoirement des positions dans la liste des positions libre
            canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "red") #on creer un canvas aux coordonnées choisit
            predateurs.append([coord,life,ENERGIE]) #on ajoute a la liste des predateurs les coordonnées selectionné, la variable vie et la variable ENERGIE
            grille.remove(coord) #on retire de la liste des positions libre la position selectionnée
            p[2] = ENERGIE #on remet le compteur d'energie a la valeur de base




#definition de toute les positions
def creer_grille():
    """ creer une liste de 30x30 position """
    for i in range(30):
        for j in range(30):
            grille.append([i,j])



#Creation du canvas#
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=COTE, height=COTE)
canvas.grid()

#bouton commencer
racine.title("PROIE_PREDATEUR")
bouton_start = tk.Button(racine, text = "Commencer", command = passage_tours, font = ("times new roman", 12))
bouton_start.grid()

creer_grille()

creer_animaux()

racine.mainloop()