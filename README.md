# Projet-S2
wow
ragondin
lol
import tkinter as tk
import random as rd

racine = tk.Tk() 
racine.title("Mon dessin")


def cercle():
    x=rd.randint(0,400)
    y=rd.randint(0,400)
    canvas.create_oval((x, y),(x+100,y+100),fill=couleur_fond)

def carré():
    x=rd.randint(0,400)
    y=rd.randint(0,400)
    canvas.create_rectangle((x,y),(x+100, y+100),fill=couleur_fond)


def croix():
    x=rd.randint(0,400)
    y=rd.randint(0,400)
    canvas.create_line((x,y), (x+100, y+100),fill=couleur_fond)
    canvas.create_line((x+100, y), (x, y+100),fill=couleur_fond)


def couleur():
    global couleur_fond 
    couleur_fond=input("couleur")

def undo():
    if len(objets)!=0:
        if canvas.delete(objets[-1])== "Line" :
          canvas.delete(objets[-1])
          del(objets[-1])
          canvas.delete(objets[-1])
          del(objets[-1])
        else:
          canvas.delete(objets[-1])
          del(objets[-1])
    
    
couleur_fond="red3"

bouton_couleur = tk.Button(racine, text="Choisir une couleur", command=couleur)
bouton_cercle = tk.Button(racine, text="Cercle", bg="cyan", command=cercle)
bouton_carré = tk.Button(racine, text="Carré",bg="purple", command=carré)
bouton_croix = tk.Button(racine, text="Croix", bg="red",command=croix)
bouton_undo = tk.Button(racine, text="Undo", bg="grey100", fg="blue",padx=20, font=("Times","20"), command=undo)


canvas = tk.Canvas(racine, width=500, height=500, bg="black", borderwidth =5 )

bouton_cercle.grid(column=0, row=3)
bouton_carré.grid(column=0, row=1)
bouton_croix.grid(column=0, row=2)
bouton_couleur.grid(column=1, row=0)
bouton_undo_grid(row=0,column=2)
canvas.grid(row=1, rowspan=3, column=1)

racine.mainloop()
