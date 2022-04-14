import tkinter as tk 
import random as rd

COTE = 600



#creation des proies 
def proie() :
    matrice = []



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

racine.mainloop()