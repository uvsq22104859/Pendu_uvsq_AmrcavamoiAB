import tkinter as tk


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
    affiche_mot(mots)


fenetre =  tk.Tk()

fenetre.geometry("900x600")

label = tk.Label(fenetre)

rec = tk.StringVar

saisie = tk.Entry(fenetre, textvariable = rec)

rep = def_mot("bonjour")
affiche_mot(rep)
label.grid(row = 0, column = 4)
print(rep)
i = 0
while(i < 7):
    lettre = input("entrer une lettre :\t")
    verify(lettre, rep)
    i += 1
    label.grid(row = 0, column = 4)
fenetre.destroy()
fenetre.mainloop()