import tkinter as tk 
import random as rd

#definition du canvas
COTE = 600
GRILLE = 30
CARRE = COTE//GRILLE

#definition des regles de vie 
life = 5
n = 10
reproduction = 330


def tour(event):
    global position,vie 
    mort_deplacement()

    for i in range (reproduction) :
       randomx = rd.randint(0,GRILLE-1)
       randomy = rd.randint(0,GRILLE-1)

       while [randomx, randomy] in position : 
            randomx = rd.randint(0,GRILLE-1)
            randomy = rd.randint(0,GRILLE-1)

       canvas.create_rectangle(randomx*CARRE,randomy*CARRE,randomx*CARRE+CARRE,randomy*CARRE+CARRE,fill="blue")
       position.append([randomx, randomy])
       vie.append(life)
    


def crée_proie() :
    global position, vie
    position = []
    vie = []

    for i in range (n) :
       randomx = rd.randint(0,GRILLE-1)
       randomy = rd.randint(0,GRILLE-1)

       while [randomx, randomy] in position : 
            randomx = rd.randint(0,GRILLE-1)
            randomy = rd.randint(0,GRILLE-1)

       canvas.create_rectangle(randomx*CARRE,randomy*CARRE,randomx*CARRE+CARRE,randomy*CARRE+CARRE,fill="blue")
       position.append([randomx, randomy])
       vie.append(life)

    


def mort_deplacement() :
    for j in range (len(vie)) :
        vie[j] -= 1
        
        if vie[j] == 0 :
            mourir = canvas.find_overlapping(position[j][0]*CARRE,position[j][1]*CARRE,position[j][0]*CARRE+CARRE,position[j][1]*CARRE+CARRE)
            for obj in mourir :
                canvas.delete(obj)


        
        



#Creation du canvas#
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=COTE, height=COTE)
canvas.grid()

#bouton
bt = tk.Button(racine,text="nouveau tour")
bt.grid()
bt.bind('<Button-1>', tour)


test = crée_proie()


print(position)

racine.mainloop()
