import tkinter as tk 
import random as rd

#definition du canvas
COTE = 600
GRILLE = 30
CARRE = COTE//GRILLE

#definition des regles de vie 
life = 5
n = 900
reproduction = 0
boucle = 1


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
        deplacement = rd.randint(1,4)
        
        if vie[j] == 0 :
            mourir = canvas.find_closest(position[j][0]*CARRE-10,position[j][1]*CARRE-10,position[j][0]*CARRE+CARRE-10,position[j][1]*CARRE+CARRE-10)
            for obj in mourir :
                canvas.delete(obj)
                del position[j]

        
        



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
