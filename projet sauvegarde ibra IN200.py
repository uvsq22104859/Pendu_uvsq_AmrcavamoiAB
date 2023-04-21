from random import randint
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
#import PIL as pil
#from PIL import ImageTk

def aide(): # C'est une fenetre pour expliquer les regles du jeu 
       
        regles_jeu = tk.Toplevel() # On crée la fenetre pour les regles du jeu
        regles_jeu.geometry("800x300") # Taille de la fenetre
        regles_jeu.title("Regles du jeu") # Titre de la fenetre
        # On commence à partir d'ici a créer nos widjets
        zone_texte1 = tk.Label (regles_jeu, text = "Le jeu du pendu est un jeu de devinettes où un joueur doit deviner un mot en proposant des lettres. Voici les règles de base du jeu :")
        zone_texte2= tk.Label (regles_jeu, text = "1. Le joueur doit deviner le mot en proposant des lettres une à une.")
        zone_texte3 = tk.Label (regles_jeu, text = "2. Si une lettre proposée est dans le mot, elle est révélée dans le mot.")
        zone_texte4= tk.Label (regles_jeu, text = "3. Si une lettre proposée n'est pas dans le mot, un élément est ajouté au dessin du pendu.")
        zone_texte5 = tk.Label (regles_jeu, text = "4. Le joueur a un nombre limité de propositions avant que le dessin ne soit complété (10 erreurs sont autorisées).")
        zone_texte6 = tk.Label (regles_jeu, text = "5. Si le joueur devine le mot avant que le dessin ne soit complété, il gagne. Sinon, il perd.")
        # On utilise le parametre (sticky="nw") pour le positionnement de nos lignes de texte
        zone_texte1.grid(sticky="nw")
        zone_texte2.grid(sticky="nw")
        zone_texte3.grid(sticky="nw")
        zone_texte4.grid(sticky="nw")
        zone_texte5.grid(sticky="nw")
        zone_texte6.grid(sticky="nw")
        boutton_compris=tk.Button(regles_jeu, text="J'ai compris", command= regles_jeu.destroy) # On ferme la page d'aide en cliquant sur "jai compris" à l'aide de la fonction ".destroy"
        boutton_compris.grid(sticky="s") 

        regles_jeu.mainloop


mote="" # Variable qui servira plus à stocker les mots
chrge = False # Car aucun mot n'a été utilisé pour le moment

jeu = False # Car le jeu n'a tjrs pas commencé

fenetre_menu = tk.Tk() # Codage de la fentre du menu
fenetre_menu.geometry("800x500+400+200") 
fenetre_menu.grid_columnconfigure(0, weight=1)
fenetre_menu.grid_columnconfigure(1, weight=1)
fenetre_menu.grid_columnconfigure(2, weight=1)
fenetre_menu.grid_columnconfigure(3, weight=1)
fenetre_menu.grid_rowconfigure(1, weight=1)
fenetre_menu.grid_rowconfigure(2, weight=1)
fenetre_menu.grid_rowconfigure(3, weight=1)
fenetre_menu.grid_rowconfigure(4, weight=1)
fenetre_menu.grid_rowconfigure(5, weight=1)
font_label = font.Font(size=20) # Configuration de la police 
font_bouton = font.Font(size=15)
font_label2 = font.Font(size=16)

# On créé ici une fonction qui servira à coder la difficulté du jeu
difficulte = 0

def je(n = None):
    global difficulte
    if n != 1:
        global jeu
        jeu = True
        difficulte=scroller.get()
    fenetre_menu.destroy()

# La fonction charger est appelée lorsque l'utilisateur clique sur le bouton "Charger". Elle définit les variables mote, score et chrge comme des variables globales, et les initialise à None, 0 et False, respectivement. La fonction ouvre un fichier CSV contenant les sauvegardes précédentes du jeu, et stocke la première ligne du fichier dans la variable ligne. Ensuite, la fonction appelle la fonction je pour commencer le jeu
def charger():
    global mote
    global score
    global chrge
    chrge = True
    path = "C:/Users/Administrateur/Desktop/save.csv"
    mode = "r"
    csv_save = open(path, mode)
    ligne = csv_save.readline()
    csv_save.close()
    je()

# On créé la conction qui permet de charger les mots aléatoirement 
def mots(liste):
    element = randint(0,len(liste)-1)
    mot = liste[element]
    return mot


score = 0
Label_1 = tk.Label(fenetre_menu, text="Jeu du Pendu", fg = "black")
Label_1['font'] = font_label
Label_2 = tk.Label(fenetre_menu, text="Choisis ta difficulté :")
Label_2['font'] = font_label2
