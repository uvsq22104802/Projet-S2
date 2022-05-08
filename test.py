from calendar import c
import tkinter as tk 
import random as rd
from random import randint, choice, random

#definition du canvas
COTE = 600
GRILLE = 30
CARRE = COTE//GRILLE
grille  = {}
proies =  {}

#definition des regles de vie 
life = 5
n = 300
reproduction = 0

def mouvement() : 
    global P2
    P2 = {}
    mv = [[0,-1],[0,1],[-1,0],[1,0],[1,1],[1,-1],[-1,1],[-1,-1]] 
    
    for p in proies :
        
        MV = rd.choice(mv)
        a,b = MV[0], MV[1]
        coord = (p[0]+a,p[1]+b)
        
        
        while coord not in grille : 
            MV = rd.choice(mv)
            a,b = MV[0], MV[1]
            coord = (p[0]+a,p[1]+b)

        move = canvas.find_overlapping(p[0]*CARRE-10,p[1]*CARRE-10,p[0]*CARRE+CARRE-10,p[1]*CARRE+CARRE-10)
        for obj in move : 
            canvas.moveto(obj, (p[0]+a)*CARRE, (p[1]+b)*CARRE)

        
        
        
       

def tour(event):
    mouvement() 
    mort()
    
    for p in range(reproduction):
        coord = choice(list(grille))
        grille.pop(coord)
        canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "blue")
        proies[coord] = life


#creer proies
def creer_proies():
    for p in range(n):
        coord = choice(list(grille))
        grille.pop(coord)
        canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "blue")
        proies[coord] = life
    


def mort() :
    a_delete = []
    for p in P2:
        P2[p] -= 1
        if P2[p] == 0:
            suppr = canvas.find_overlapping(p[0]*CARRE,p[1]*CARRE,p[0]*CARRE+CARRE,p[1]*CARRE+CARRE)
            for obj in suppr : 
                canvas.delete(obj)
            a_delete.append(p)
            grille[p] = 0
            
    for position in a_delete:
        P2.pop(position)




        
#definition de toute les positions
def creer_grille():
    for i in range(30):
        for j in range(30):
            grille[(i,j)] = 0



#Creation du canvas#
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=COTE, height=COTE)
canvas.grid()

#bouton
bt = tk.Button(racine,text="nouveau tour")
bt.grid()
bt.bind('<Button-1>', tour)

creer_grille()

creer_proies()

racine.mainloop()