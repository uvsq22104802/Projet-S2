import tkinter as tk 
import random as rd
import time

#definition du canvas
COTE = 600
GRILLE = 30
CARRE = COTE//GRILLE

#definition des regles de vie 
life = 5
n = 10
reproduction = 3


def tour(event):
    global position,vie 
    mort()

    for i in range (reproduction) :
       randomx = rd.randint(0,GRILLE-1)
       randomy = rd.randint(0,GRILLE-1)

       while [randomx, randomy] in position : 
            randomx = rd.randint(0,GRILLE-1)
            randomy = rd.randint(0,GRILLE-1)

       canvas.create_rectangle(randomx*CARRE,randomy*CARRE,randomx*CARRE+CARRE,randomy*CARRE+CARRE,fill="blue")
       position.append((randomx, randomy))
       vie.append(life)
       


def crée_proie() :
    global position, vie
    position = []
    vie = []

    for i in range (0,n) :
       randomx = rd.randint(0,GRILLE-1)
       randomy = rd.randint(0,GRILLE-1)

       while [randomx, randomy] in position : 
            randomx = rd.randint(0,GRILLE-1)
            randomy = rd.randint(0,GRILLE-1)

       canvas.create_rectangle(randomx*CARRE,randomy*CARRE,randomx*CARRE+CARRE,randomy*CARRE+CARRE,fill="blue")
       position.append((randomx, randomy))
       vie.append(life)

    return position


def mort() :
    for j in range (len(vie)) :
        vie[j] -= 1



    
    print(vie)


#creation du quadrillage#

def quadrillage() :
    for i in range (0,COTE,CARRE) : 
     canvas.create_line(COTE,i,0,i, fill="white")
     canvas.create_line(i,COTE,i,0, fill= "white")



#Creation du canvas#
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=COTE, height=COTE)
canvas.grid()

#bouton
bt = tk.Button(racine,text="nouveau tour")
bt.grid()
bt.bind('<Button-1>', tour)

quadrillage()

test = crée_proie()
print(position)

racine.mainloop()
