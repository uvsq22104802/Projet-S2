from ast import Delete
import tkinter as tk 
import random as rd

COTE = 300

n = 100



def crée_proie() :
    global randomx, randomy
    for i in range (n) :
       randomx = rd.randint(0,290)
       randomy = rd.randint(0,290)
       proie = canvas.create_rectangle(randomx,randomy,randomx+10,randomy+10,fill="blue")

       coord = canvas.coords(proie)

       choc = canvas.find_overlapping(coord)
       for obj in choc : 
        canvas.itemconfigure(obj, fill = "red")

    


    return[proie]






#Creation du canvas#

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=COTE, height=COTE)
canvas.grid()

boloss = crée_proie()


racine.mainloop()
