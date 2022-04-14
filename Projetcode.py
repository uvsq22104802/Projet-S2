import tkinter as tk 
import random as rd

COTE = 300 

randomx = rd.randint(0,290)
randomy = rd.randint(0,290)


def crée_proie() :
    proie = canvas.create_oval(randomx,randomy,randomx+10,randomy+10,fill="blue")

    return[proie]
    






#Creation du canvas#

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=COTE, height=COTE)
canvas.grid()

boloss = crée_proie()

racine.mainloop()



