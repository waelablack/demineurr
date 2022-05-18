import random
import tkinter
from tkinter import *
from tkinter import ttk


longueur = 10
largeur = 10
bombe = 30

carte = [[0 for i in range(longueur)] for i in range(largeur)]

while bombe != 0:
    
    i = random.randint(0, longueur-1)
    j = random.randint(0, largeur-1)
    if carte[i][j] != 'X':
        carte[i][j] = 'X'
        bombe = bombe - 1
    

for i in range(largeur):
    for j in range(longueur):
        if carte[i][j] != 'X':
            s=0
            if i-1 >= 0 and j-1 >=0:
                if carte[i-1][j-1] == 'X':
                    s = s + 1
            if i-1 >= 0 :     
                if carte[i-1][j] == 'X':
                    s = s + 1
            if  j-1 >=0:
                if carte[i][j-1] == 'X':
                    s = s + 1
            if i+1 < largeur and j+1 <longueur:
                if carte[i+1][j+1] == 'X':
                    s = s + 1
            if i+1 < largeur :
                if carte[i+1][j] == 'X':
                    s = s + 1
            if j+1 < longueur:
                if carte[i][j+1] == 'X':
                    s = s + 1
            if i+1 < largeur and j-1 >= 0:
                if carte[i+1][j-1] == 'X':
                    s = s + 1
            if i-1 >= 0 and j+1 < longueur:
                if carte[i-1][j+1] == 'X':
                    s = s + 1
            carte[i][j] = s
            
            
            
for ligne in carte:
    print (ligne)
    
   
##----- Importation des Modules -----##
from tkinter import *

##----- Variables globales -----##
c = 50                          # Longueur d'un côté d'une case
longueur = 10                   # Nombre de cases par ligne et par colonne
largeur = 10
cases = []                      # Liste contenant les objets cases

##----- Création de la fenêtre -----##

    
fen = Tk()
fen.title('Démineur')


##----- Création des boutons -----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 1, column = 1, sticky=W+E, padx=3, pady=3)
bouton = tkinter.Button (text = "Quitter") 
    
##----- Création des canevas -----##
dessin = Canvas(fen, width = largeur*c+2, height = longueur*c+2, bg = 'white')
dessin.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)

##----- Création des figures -----##
for ligne in range(longueur):          # Les cases de chaque ligne seront stockées dans "transit"
    transit=[]
    for colonne in range(largeur):    # Conception des cases d'une ligne
        transit.append(dessin.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
        
        

    cases.append(transit)       # Ajout de la ligne à la liste principale

##----- Modification des figures créées -----##
for ligne in range(longueur):
    for colonne in range(largeur):
        if carte[ligne][colonne] == 'X':      
            dessin.itemconfigure(cases[ligne][colonne], outline='white', fill='red')
        else:
            dessin.itemconfigure(cases[ligne][colonne], outline='white', fill='black')


 

##----- Programme principal -----##
fen.mainloop()                  # Boucle d'attente des événements
    
    

