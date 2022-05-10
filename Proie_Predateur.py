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
life = 1000
Nproie = 10
Npreda = 0
energie = 10
Rproie = 0
Rpreda = 0


#definition du mouvement
def mouvement() : 
    a_delete = []
    a_ajouter = []
    mv = [[0,-1],[0,1],[-1,0],[1,0]] 
    #mouvement des proies
    for p in proies :
        MV = rd.choice(mv)
        a,b = MV[0], MV[1]
        coord = [[p[0][0]+a,p[0][1]+b],p[1]]
        for k in grille :
            while coord[0] not in grille  :
                MV = rd.choice(mv)
                a,b = MV[0], MV[1]
                coord = [[p[0][0]+a,p[0][1]+b],p[1]]

   
        move = canvas.find_overlapping(p[0][0]*CARRE-10,p[0][1]*CARRE-10,p[0][0]*CARRE+CARRE-10,p[0][1]*CARRE+CARRE-10)
        for obj in move : 
            canvas.moveto(obj, coord[0][0]*CARRE, coord[0][1]*CARRE)
        grille.append(p)
        proies.remove(p)
        proies.append(coord)
            
        

    
    


    #mouvement predateur 
    return
    for p in predateurs :
        MV = rd.choice(mv)
        a,b = MV[0], MV[1]
        coord = [[p[0][0]+a,p[0][1]+b],p[1]]
        predateurs.remove(p)
        predateurs.append(coord)
    
        for k in grille : 
            while predateurs in k and ((p[0][0] or p[0][1])<0) and ((p[0][0] or p[0][1])>30):
                MV = rd.choice(mv)
                a,b = MV[0], MV[1]
                coord = [[p[0][0]+a,p[0][1]+b],p[1]]
                proies.remove(p)
                proies.append(coord)
                
        
        move = canvas.find_overlapping(p[0][0]*CARRE,p[0][1]*CARRE,p[0][0]*CARRE+CARRE,p[0][1]*CARRE+CARRE)
        for obj in move : 
            canvas.moveto(obj, coord[0][0]*CARRE, coord[0][1]*CARRE)
        


#definitiopn de la reproduction
def tour(event):
    mouvement() 
    mort_proies()
    mort_predateur()
    
    for p in range(Rproie):
        coord = [choice(list(grille)), life]
        canvas.create_rectangle(coord[0][0]*CARRE,coord[0][1]*CARRE,coord[0][0]*CARRE+CARRE,coord[0][1]*CARRE+ CARRE, fill = "blue") 
        proies.append(coord) 
        grille.remove(coord[0]) 

    for p in range(Rpreda) :
        coord = [choice(list(grille)), life, energie]
        canvas.create_rectangle(coord[0][0]*CARRE,coord[0][1]*CARRE,coord[0][0]*CARRE+CARRE,coord[0][1]*CARRE+ CARRE, fill = "red")
        predateurs.append(coord)
        grille.remove(coord[0])



#creer proies et des predateur
def creer_animaux():
    for p in range(Nproie):
        coord = choice(list(grille))
        canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "blue")
        proies.append(coord)
        proies[p] = [proies[p], life]
        grille.remove(coord)
    
    for p in range(Npreda) :
        coord = choice(list(grille))
        canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "red")
        predateurs.append(coord)
        predateurs[p] = [predateurs[p], life, energie]
        grille.remove(coord)


#mort des proies
def mort_proies() :
    a_delete = []
    for p in proies:
        p[1] -= 1
        if p[1] == 0:
            suppr = canvas.find_overlapping(p[0][0]*CARRE-10,p[0][1]*CARRE-10,p[0][0]*CARRE+CARRE-10,p[0][1]*CARRE+CARRE-10)
            for obj in suppr : 
                canvas.delete(obj)

            a_delete.append(p)
            grille.append(p[0])
    
    for k in a_delete:
        proies.remove(k)


def mort_predateur() :
    a_delete = []
    print(proies)
    for p in predateurs:
        p[1] -= 1
        p[2] -= 1
        if (p[1] == 0) or (p[2] == 0):
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