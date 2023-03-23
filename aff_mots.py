import tkinter as tk
import random

bank_mots = ["bonjour", "sensible", "montagne", "russe", "livre"]

def def_mot(mots):
    aff = [[],[]]
    for i in mots:
        aff[1].append(i)
        aff[0].append("*")
    return aff

def affiche_mot(liste):
    text = ""
    for i in liste[0]:
        text += i
    label.config(text = text)

def verify(lettre, mots):
    for i in range(len(mots[1])):
        if lettre == mots[1][i]:
            mots[0][i] = mots[1][i]
        if mots[0] == mots[1]:
            fenetre.destroy()
    affiche_mot(mots)

def ver():
    q = saisie.get()
    verify(q, rep)
    saisie.delete(0,len(q))

def maxone():
    pass
    if len(saisie.get()) < 1:
        return True
    else:
        saisie.delete(0, len(saisie.get()))
        return True

fenetre =  tk.Tk()
fenetre.geometry("900x600")

#Widgets
label = tk.Label(fenetre)
bouton1  = tk.Button(fenetre, command = ver)

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

fenetre.mainloop()