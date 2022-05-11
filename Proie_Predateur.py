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
life = 10
Nproie = 50
Npreda = 3
ENERGIE = 5
MIAM = 5
Rproie = 50
Rpreda = 12

            
def mouvement_mort_proies() : 
    """permet a la proies de bouger autour d'elle"""
    mv = [[0,-1],[0,1],[-1,0],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]] #listes des differentes position pouvant etre prise
    a_delete = []
    a_ajouter = []
    for p in proies : # pour chaque proies, on ajoute aux coordonnée + ou - 1 pour les deplacer 

        move = canvas.find_overlapping(p[0][0]*CARRE,p[0][1]*CARRE,p[0][0]*CARRE+CARRE,p[0][1]*CARRE+CARRE)
        canvas.delete(move[0])
        a_delete.append(p)
        
        if p[1] != 0 :
            p[1] -= 1
            MV = rd.choice(mv)
            a,b = MV[0], MV[1]
            coord = [[p[0][0]+a,p[0][1]+b],p[1]] 

            while coord[0] not in grille :
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

   


def mouvement_mort_Preda() :
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

        if coord[0] not in (grille or proies[0][0]):
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
    passage_tours()
    reproduction_proies()
    mouvement_mort_proies() 
    mouvement_mort_Preda()
    energie()






 
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



def energie() :
    for p in predateurs :
        for k in proies :
            if p[0] == k[0] :
                p[2] += MIAM

    a_delete = []
    for p in predateurs :
            p[1] -= 1
            p[2] -= 1
            if p[2] > Rpreda :
                print(p[1],p[2])
                coord = choice(list(grille))
                canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "red")
                predateurs.append([coord,life,ENERGIE])
                grille.remove(coord)
                p[2] = ENERGIE
            if p[1] == 0 :
                a_delete.append(p)
                suppr = canvas.find_overlapping(p[0][0]*CARRE,p[0][1]*CARRE,p[0][0]*CARRE+CARRE,p[0][1]*CARRE+ CARRE)
                canvas.delete(suppr[0])
                grille.append(a_delete[0])  

            if p[2] == 0 :
                a_delete.append(p)
                suppr = canvas.find_overlapping(p[0][0]*CARRE,p[0][1]*CARRE,p[0][0]*CARRE+CARRE,p[0][1]*CARRE+ CARRE)
                canvas.delete(suppr[0])
                grille.append(a_delete[0][0])   

            for i in a_delete :
                print(a_delete)
                print(predateurs)
                predateurs.remove(a_delete[0])
                a_delete.remove(a_delete[0])
                             



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
