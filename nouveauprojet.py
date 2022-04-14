import tkinter as tk 
import random as rd

COTE = 600

n = 10

def crée_proie() :
    for i in range (0,n) :
       randomx = rd.randint(0,COTE-20)
       randomy = rd.randint(0,COTE-20)
       proie = canvas.create_rectangle(randomx,randomy,randomx+20,randomy+20,fill="blue")


    return[proie]

#creation du quadrillage#

def quadrillage() :
    for i in range (0,COTE,20) : 
     canvas.create_line(COTE,i,0,i, fill="white")
     canvas.create_line(i,COTE,i,0, fill= "white")

#Creation du canvas#

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=COTE, height=COTE)
canvas.grid()

quadrillage()

test = crée_proie()

racine.mainloop()