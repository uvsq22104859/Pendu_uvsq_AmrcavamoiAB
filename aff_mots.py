import tkinter as tk
import random
from tkinter import messagebox
import tkinter.font

bank_mots = ["bonjour", "sensible", "montagne", "russe", "livre"]
score = 0
nbr_indice_util = 0
fenetre = 0

def jeu():
    """
    fenetre permetent de jouer 
    oú sont definie les autres fonction pour jeu
    """
    global bank_mots, score, nbr_indice_util, fenetre
    score = nbr_indice_util = 0
    def def_mot(mots):
        """
        enregistre le mot choisi dans un tableau a deux dimensions
        dans la premiere ligne est enregistrer des "*" c'est cette ligne qui est afficher
        et dans la seconde le mot a trouver
        """
        aff = [[],[]]
        for i in mots:
            aff[1].append(i)
            aff[0].append("*")
        return aff

    def affiche_mot(liste):
        """
        Permet de modifier le texte du label afiiche la premiere ligne de aff
        """
        texte = ""
        for i in liste[0]:
            texte += i
        label.config(text = texte, font = ("Helvetica",30))

    def verify(lettre, mots):
        """
        verifie si la lettre donner par l'utilisateur est dans le mot
        Et si le mot a ete trouver demande a l'utilisateur si il veut rejouer
        """
        global fenetre
        for i in range(len(mots[1])):
            if lettre == mots[1][i]:
                mots[0][i] = mots[1][i]
            if mots[0] == mots[1]:
                if tk.messagebox.askyesno(title="Fin de partie", message="Voulew vous refaire un partie?"):
                    fenetre.destroy()
                    jeu()
                else:
                    fenetre.destroy()
                return
            saisie.delete(0,len(saisie.get()))
        affiche_mot(mots)

    def ver():
        """
        Verifie si l'utilisateur a bien mis une seule lettre
        sinon affiche un message informatife rapelent qu'il faut mettre qu'une seule lettre 
        """
        global score
        nbr_lettre = len(saisie.get())
        if nbr_lettre > 1 :
            tk.messagebox.showinfo(title="Max elements 1", message="Vous ne pouvez entrer qu'une lettre a la fois.")
            saisie.delete(0, nbr_lettre)
            return
        verify(saisie.get(), rep)
        score += 1

    def SaveParti():
        """
        Permet d'enregistrer la partie dans un fichier
        """
        pass

    def indice():
        """
        Revele une lettre presente dans le mot pour aider l'utilisateur
        """
        global score, nbr_indice_util
        lettre_indice = []
        for i in range(len(rep[1])):
            if rep[0][i] != rep[1][i]:
                lettre_indice.append(i)
        score += 1
        nbr_indice_util += 1
        verify(rep[1][lettre_indice[random.randint(0,len(lettre_indice)-1)]],rep)



    def maxone():
        """
        empeche de mettre plus d'une lettre 
        """
        if len(saisie.get()) < 1:
            return True
        else:
            saisie.delete(0, len(saisie.get()))
            return True


    fenetre =  tk.Tk()
    fenetre.geometry("900x600")

    #Widgets
    label = tk.Label(fenetre, font=("Helvetica",30))
    bouton1  = tk.Button(fenetre, text="OK", command = ver)
    b_indice = tk.Button(fenetre, text = "indice", command = indice)

    rec = tk.StringVar

    saisie = tk.Entry(fenetre, textvariable = rec, take = 'focus', validate = "key", validatecommand = maxone)

    #Mots aléatoire
    index = random.randint(0, len(bank_mots)-1)
    rep = def_mot(bank_mots[index])
    affiche_mot(rep)
    #Positionnement
    label.grid(row = 0, column = 4)
    saisie.grid(row = 1, column = 3)
    bouton1.grid(row = 2, column = 5)
    b_indice.grid(row=3, column=6)

    #Petite blague
    def closed():
        """
        Affiche un message pour etre sur que l'utilsateur veut qutter l'application
        """
        if messagebox.askyesno("Essayez de trouver", "Voulez-vous vraiment nous quitter ?"):
            if messagebox.askyesno("Sauvegarde", "Voulez vous sauvegarder la partie ?"):
                SaveParti()
                print("partie saved")
            fenetre.destroy()

    fenetre.protocol("WM_DELETE_WINDOW", closed)

    fenetre.mainloop()

def start():
    """
    Fonction qui demare l'application et affiche les regle du jeu.
    Renvoi vers la fonction jeu
    """
    global fenetre
    def Ok():
        fenetre.destroy()
        jeu()
    fenetre = tk.Tk()
    fenetre.geometry("900x600")
    test = tk.Button(text="OK", command=Ok)
    test.pack()
    fenetre.mainloop()
    pass

start()
# fenetre.destroy()

# print("score: ",score, "nomnre d'indices utiliser: ", nbr_indice_util)

# fenetre = tk.Tk()
# 
# fenetre.mainloop()