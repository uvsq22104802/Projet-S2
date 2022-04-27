from calendar import c
import tkinter as tk 
import random as rd
from random import randint, choice

#definition du canvas
COTE = 600
GRILLE = 30
CARRE = COTE//GRILLE
grille  = {}
proies =  {}

#definition des regles de vie 
life = 5
n = 10
reproduction = 5

def move() :
    global proies,coord
    coord_proies = []
    coord = choice(list(grille))
    mv = [[0,-1],[0,1],[-1,0],[1,0],[1,1],[1,-1],[-1,1],[-1,-1]] 
    for coord in coord_proies :
        proies = rd.choice(mv))


def tour(event):
    mort()
    move()

    for p in range(reproduction):
        coord = choice(list(grille))
        grille.pop(coord)
        canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "blue")
        proies[coord] = life
        coord = coord_proies
        coord_proies.append


#creer proies
def creer_proies():
    for p in range(n):
        coord = choice(list(grille))
        grille.pop(coord)
        canvas.create_rectangle(coord[0]*CARRE,coord[1]*CARRE,coord[0]*CARRE+CARRE,coord[1]*CARRE+ CARRE, fill = "blue")
        proies[coord] = 5
        coord_proies.append
    


def mort() :
    print(proies)
    a_delete = []
    for p in proies:
        proies[p] -= 1
        if proies[p] == 0:
            suppr = canvas.find_overlapping(p[0]*CARRE,p[1]*CARRE,p[0]*CARRE+CARRE,p[1]*CARRE+CARRE)
            for obj in suppr : 
                canvas.delete(obj)
            a_delete.append(p)
            grille[p] = 0
            
    for position in a_delete:
        proies.pop(position)




        
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

move()

racine.mainloop()
