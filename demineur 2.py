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
    
   

from tkinter import *


c = 50                         
longueur = 10                   
largeur = 10
cases = []                      



    
fen = Tk()
fen.title('Démineur')



bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 1, column = 1, sticky=W+E, padx=3, pady=3)
bouton = tkinter.Button (text = "Quitter") 
    

dessin = Canvas(fen, width = largeur*c+2, height = longueur*c+2, bg = 'white')
dessin.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)


for ligne in range(longueur):          
    transit=[]
    for colonne in range(largeur):   
        transit.append(dessin.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
        
        

    cases.append(transit)      


for ligne in range(longueur):
    for colonne in range(largeur):
        if carte[ligne][colonne] == 'X':      
            dessin.itemconfigure(cases[ligne][colonne], outline='white', fill='red')
        else:
            dessin.itemconfigure(cases[ligne][colonne], outline='white', fill='black')


 


fen.mainloop()                  
    
    

