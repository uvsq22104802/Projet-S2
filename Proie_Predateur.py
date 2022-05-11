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
life = 20
Nproie = 30
Npreda = 3
ENERGIE = 15
MIAM = 3
Rproie = 0
Rpreda = 95

            
def mouvement_proies() : 
    """permet a la proies de bouger autour d'elle"""
    mv = [[0,-1],[0,1],[-1,0],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]] #listes des differentes position pouvant etre prise
    a_delete = []
    a_ajouter = []
    for p in proies : # pour chaque proies, on ajoute aux coordonnée + ou - 1 pour les deplacer 

        move = canvas.find_overlapping(p[0][0]*CARRE,p[0][1]*CARRE,p[0][0]*CARRE+CARRE,p[0][1]*CARRE+CARRE)
        canvas.delete(move[0])
        a_delete.append(p)

        MV = rd.choice(mv)
        a,b = MV[0], MV[1]
        coord = [[p[0][0]+a,p[0][1]+b],p[1]] 
        for k in grille : #si les coordonnées d'une proies ne sont pas dans la liste, elle recherche une nouvelle position
            if coord[0] not in grille :
                MV = rd.choice(mv)
                a,b = MV[0], MV[1]
                coord = [[p[0][0]+a,p[0][1]+b],p[1]]


        a_ajouter.append([coord, p[1]])

        canvas.create_rectangle(coord[0][0]*CARRE,coord[0][1]*CARRE,coord[0][0]*CARRE+CARRE,coord[0][1]*CARRE+CARRE, fill = "blue")



    for p in a_delete :
        proies.remove(p)
        grille.append(p[0])

    for p in a_ajouter :
        proies.append([p[0][0],p[0][1]])

   

            
        

def mouvement_Preda() :
    """ permet au predateur de bouger autour de lui """
    mv = [[0,-1],[0,1],[-1,0],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]] 
    #mouvement des predateur
    mv = [[0,-1],[0,1],[-1,0],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]] #listes des differentes position pouvant etre prise
    a_delete = []
    a_ajouter = []
    for p in predateurs : # pour chaque proies, on ajoute aux coordonnée + ou - 1 pour les deplacer 

        move = canvas.find_overlapping(p[0][0]*CARRE,p[0][1]*CARRE,p[0][0]*CARRE+CARRE,p[0][1]*CARRE+CARRE)
        canvas.delete(move[0])
        a_delete.append(p)

        MV = rd.choice(mv)
        a,b = MV[0], MV[1]
        coord = [[p[0][0]+a,p[0][1]+b],p[1],p[2]] 
        for k in grille : #si les coordonnées d'une proies ne sont pas dans la liste, elle recherche une nouvelle position
            for k in proies :
                if coord[0] not in (grille or k[0]):
                    MV = rd.choice(mv)
                    a,b = MV[0], MV[1]
                    coord = [[p[0][0]+a,p[0][1]+b],p[1],p[2]]


        a_ajouter.append([coord])
        canvas.create_rectangle(coord[0][0]*CARRE,coord[0][1]*CARRE,coord[0][0]*CARRE+CARRE,coord[0][1]*CARRE+CARRE, fill = "red")


    for p in a_delete :
        predateurs.remove(p)
        grille.append(p[0])

    for p in a_ajouter :
        predateurs.append([p[0][0],p[0][1],p[0][2]])
            
        

def passage_tours():
    """permet le passage de tour tout les x temps """
    global var_chrono
    var_chrono = canvas.after(CHRONO, tour) 
    

#definitiopn de la reproduction
def tour():
    """permet de lancer toutes le definition a chaque tour """
    print(predateurs)
    mouvement_Preda()
    mouvement_proies() 
    mort_animaux()
    reproduction_proies()
    energie()
    passage_tours()



#creer proies et des predateur
def creer_animaux():
    """ creer les proies et predateurs initiaux """
    for p in range(Nproie): #creation des proies inital
        coord = choice(list(grille))
        canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "blue")
        proies.append(coord)
        proies[p] = [proies[p], life]
        grille.remove(coord)

    
    for p in range(Npreda) : #creations des predateurs inital
        coord = choice(list(grille))
        canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "red")
        predateurs.append(coord)
        predateurs[p] = [predateurs[p], life, ENERGIE]
        grille.remove(coord)


def reproduction_proies() :
    """ permet la reproduction de N proies """
    for p in range(Rproie): #reproduction des proies a chaque tours
        coord = [choice(list(grille)), life]
        canvas.create_rectangle(coord[0][0]*CARRE,coord[0][1]*CARRE,coord[0][0]*CARRE+CARRE,coord[0][1]*CARRE+ CARRE, fill = "blue") 
        proies.append(coord) 
        grille.remove(coord[0]) 


def mort_animaux() :
    """ si la vie atteint 0 l'animal meurt """
    a_delete_proies = []
    a_delete_preda = []
    for p in proies:
        p[1] -= 1
        if p[1] == 0:
            suppr = canvas.find_overlapping(p[0][0]*CARRE-10,p[0][1]*CARRE-10,p[0][0]*CARRE+CARRE-10,p[0][1]*CARRE+CARRE-10)
            for obj in suppr : 
                canvas.delete(obj)

            a_delete_proies.append(p)
            grille.append(p[0])
    
    for k in a_delete_proies:
        proies.remove(k)
    

    for p in predateurs:
        p[1] -= 1
        if (p[1] == 0) :
            suppr = canvas.find_overlapping(p[0][0]*CARRE-10,p[0][1]*CARRE-10,p[0][0]*CARRE+CARRE-10,p[0][1]*CARRE+CARRE-10)
            for obj in suppr : 
                canvas.delete(obj)

            a_delete_preda.append(p)
            grille.append(p[0])
    
    for k in a_delete_preda :
        predateurs.remove(k)


def energie() :
    a_delete = []
    for p in predateurs:

        p[2] -= 1
        if (p[2] == 0) :
            suppr = canvas.find_overlapping(p[0][0]*CARRE-10,p[0][1]*CARRE-10,p[0][0]*CARRE+CARRE-10,p[0][1]*CARRE+CARRE-10)
            for obj in suppr : 
                canvas.delete(obj)

            a_delete.append(p)
            grille.append(p[0])
    
    for k in a_delete :
        predateurs.remove(k)

    for p in predateurs :
        for k in proies :
            if p[0] == k[0] :
                p[2] += MIAM
                proies.remove(k)

    for i in predateurs :
        if i[2] >= Rpreda :
            return
            for p in range(1) :
                coord = choice(list(grille))
                canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "red")
                coord = [coord, life, ENERGIE]

                predateurs.append(coord)
                grille.remove(coord[0])





    


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
