import tkinter as tk
import random

bank_mots = ["bonjour", "sensible", "montagne", "russe", "livre"]
score = 0
nbr_indice_util = 0

def def_mot(mots):
    aff = [[],[]]
    for i in mots:
        aff[1].append(i)
        aff[0].append("*")
    return aff

def affiche_mot(liste):
    texte = ""
    for i in liste[0]:
        texte += i
    label.config(text = texte)

def verify(lettre, mots):
    for i in range(len(mots[1])):
        if lettre == mots[1][i]:
            mots[0][i] = mots[1][i]
        if mots[0] == mots[1]:
            fenetre.destroy()
            return
    affiche_mot(mots)

def ver():
    global score
    if len(saisie.get()) > 1 :
        saisie.delete(0,len(q))
        return
    verify(saisie.get(), rep)
    saisie.delete(0,len(saisie.get()))
    score += 1

def indice():
    global score, nbr_indice_util
    lettre_indice = []
    for i in range(len(rep[1])):
        if rep[0][i] != rep[1][i]:
            lettre_indice.append(i)
    score += 1
    nbr_indice_util += 1
    verify(rep[1][lettre_indice[random.randint(0,len(lettre_indice)-1)]],rep)



def maxone():
    print(saisie.get())
    if len(saisie.get()) < 1:
        return True
    else:
        saisie.delete(0, len(saisie.get()))
        return True

fenetre =  tk.Tk()
fenetre.geometry("900x600")

#Widgets
label = tk.Label(fenetre)
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

fenetre.mainloop()
print("score: ",score, "nomnre d'indices utiliser: ", nbr_indice_util)

# fenetre = tk.Tk()
# 
# fenetre.mainloop()