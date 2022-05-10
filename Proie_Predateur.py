from calendar import c
import tkinter as tk 
import random as rd
from random import randint, choice, random

#definition du canvas
COTE = 600
GRILLE = 30
CARRE = COTE//GRILLE
grille  = []
proies =  []
predateurs = []

#definition des regles de vie 
life = 10
Nproie = 0
Npreda = 10
ENERGIE = 5
Rproie = 0
Rpreda = 0


#definition du mouvement
def mouvement_proies() : 
    mv = [[0,-1],[0,1],[-1,0],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]] 
    #mouvement des proies
    for p in proies :
        MV = rd.choice(mv)
        a,b = MV[0], MV[1]
        coord = [[p[0][0]+a,p[0][1]+b],p[1]]
        for k in grille :
            while coord[0] not in grille or predateurs  :
                MV = rd.choice(mv)
                a,b = MV[0], MV[1]
                coord = [[p[0][0]+a,p[0][1]+b],p[1]]

   
        move = canvas.find_overlapping(p[0][0]*CARRE-10,p[0][1]*CARRE-10,p[0][0]*CARRE+CARRE-10,p[0][1]*CARRE+CARRE-10)
        for obj in move : 
            canvas.moveto(obj, coord[0][0]*CARRE, coord[0][1]*CARRE)
        grille.append(p)
        proies.remove(p)
        proies.append(coord)
            
        

def mouvement_Preda() :
    mv = [[0,-1],[0,1],[-1,0],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]] 
    #mouvement des predateur
    for p in predateurs :
        MV = rd.choice(mv)
        a,b = MV[0], MV[1]
        coord = [[p[0][0]+a,p[0][1]+b],p[1]]
        for k in grille :
            while coord[0] not in grille or proies :
                MV = rd.choice(mv)
                a,b = MV[0], MV[1]
                coord = [[p[0][0]+a,p[0][1]+b],p[1]]

   
        move = canvas.find_overlapping(p[0][0]*CARRE-10,p[0][1]*CARRE-10,p[0][0]*CARRE+CARRE-10,p[0][1]*CARRE+CARRE-10)
        for obj in move : 
            canvas.moveto(obj, coord[0][0]*CARRE, coord[0][1]*CARRE)
        grille.append(p)
        predateurs.remove(p)
        predateurs.append(coord)
        


#definitiopn de la reproduction
def tour(event):
    mouvement_proies() 
    mort_animaux()
    reproduction_proies()
    mouvement_Preda()
    energie()
    print(predateurs[])
    

    for p in range(Rpreda) :
        coord = [choice(list(grille)), life, ENERGIE]
        canvas.create_rectangle(coord[0][0]*CARRE,coord[0][1]*CARRE,coord[0][0]*CARRE+CARRE,coord[0][1]*CARRE+ CARRE, fill = "red")
        predateurs.append(coord)
        grille.remove(coord[0])



#creer proies et des predateur
def creer_animaux():
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
    for p in range(Rproie): #reproduction des proies a chaque tours
        coord = [choice(list(grille)), life]
        canvas.create_rectangle(coord[0][0]*CARRE,coord[0][1]*CARRE,coord[0][0]*CARRE+CARRE,coord[0][1]*CARRE+ CARRE, fill = "blue") 
        proies.append(coord) 
        grille.remove(coord[0]) 


def mort_animaux() : #definition de la mort des proies 
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
    return
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

    


#definition de toute les positions
def creer_grille():
    for i in range(30):
        for j in range(30):
            grille.append([i,j])



#Creation du canvas#
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=COTE, height=COTE)
canvas.grid()

#bouton
bt = tk.Button(racine,text="nouveau tour")
bt.grid()
bt.bind('<Button-1>', tour)

creer_grille()

creer_animaux()

racine.mainloop()
