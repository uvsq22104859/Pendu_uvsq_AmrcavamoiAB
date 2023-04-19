import tkinter as tk
import random
from tkinter import messagebox
import tkinter.font

bank_mots = ["bonjour", "sensible", "montagne", "russe", "livre"]
score = 0
nbr_indice_util = 0
fenetre = 0
rep = ""

def jeu(new):
    """
    fenetre permetent de jouer 
    oú sont definie les autres fonction pour jeu
    """
    global bank_mots, score, nbr_indice_util, fenetre, rep
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
        in_word = False
        for i in range(len(mots[1])):
            if lettre == mots[1][i]:
                mots[0][i] = mots[1][i]
                in_word = True
            if mots[0] == mots[1]:
                if tk.messagebox.askyesno(title="Fin de partie", message="Voulez vous refaire un partie?"):
                    fenetre.destroy()
                    jeu(True)
                else:
                    fenetre.destroy()
                return
            saisie.delete(0,len(saisie.get()))
        affiche_mot(mots)
        return in_word

    def ver():
        """
        Verifie si l'utilisateur a bien mis un nombre de lettres egal aux nombre de lettres du mots secret
        sinon affiche un message informatife rapelent qu'il faut mettre le meme nombre de lettre 
        """
        global score, fenetre, rep
        mots = saisie.get()
        nbr_lettre = len(mots)
        print(rep[1])
        if nbr_lettre != len(rep[0]) :
            tk.messagebox.showinfo(title="Invalid entry", message="Votre reponse doit avoir le meme nombre de lettre que le mot a deviner.")
            saisie.delete(0, nbr_lettre)
            return
        score += 1
        for i in range(nbr_lettre):
            if mots[i] != rep[1][i]:
                saisie.delete(0,len(mots))
                return
        if tk.messagebox.askyesno(title="Fin de partie", message="Voulez vous refaire un partie?"):
            fenetre.destroy()
            jeu(True)
        else:
            fenetre.destroy()
        return
    
    def ver_lettre(event):
        global score
        if event.widget["bg"] == "green" or event.widget["bg"] == "red":
            return
        if verify(event.widget["text"], rep):
            event.widget.config(bg="green")
        else:
            event.widget.config(bg="red")
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


    if(new):
        score = nbr_indice_util = 0
        fenetre =  tk.Tk()
        fenetre.geometry("900x600")
            #Mots aléatoire
        index = random.randint(0, len(bank_mots)-1)
        rep = def_mot(bank_mots[index])
    else:
        fenetre =  tk.Tk()
        fenetre.geometry("900x600")
    
     #Widgets
    label = tk.Label(fenetre, font=("Helvetica",30))
    bouton_Ok  = tk.Button(fenetre, text="OK", command = ver)
    b_indice = tk.Button(fenetre, text = "indice", command = indice)
    b_Score = tk.Button(fenetre, text="Score", command=Tableau_score)

    rec = tk.StringVar
    saisie = tk.Entry(fenetre, textvariable = rec, take = 'focus')

      #Bouton lettres
    bouton_a = tk.Button(fenetre,text="a")
    bouton_a.bind('<Button-1>', ver_lettre)

    bouton_b =tk.Button(fenetre, text="b")
    bouton_b.bind('<Button-1>', ver_lettre)

    bouton_c =tk.Button(fenetre, text="c")
    bouton_c.bind('<Button-1>', ver_lettre)

    bouton_d =tk.Button(fenetre, text="d")
    bouton_d.bind('<Button-1>', ver_lettre)

    bouton_e =tk.Button(fenetre, text="e")
    bouton_e.bind('<Button-1>', ver_lettre)

    bouton_f =tk.Button(fenetre, text="f")
    bouton_f.bind('<Button-1>', ver_lettre)

    bouton_g =tk.Button(fenetre, text="g")
    bouton_g.bind('<Button-1>', ver_lettre)

    bouton_h =tk.Button(fenetre, text="h")
    bouton_h.bind('<Button-1>', ver_lettre)

    bouton_i =tk.Button(fenetre, text="i")
    bouton_i.bind('<Button-1>', ver_lettre)

    bouton_j =tk.Button(fenetre, text="j")
    bouton_j.bind('<Button-1>', ver_lettre)

    bouton_k =tk.Button(fenetre, text="k")
    bouton_k.bind('<Button-1>', ver_lettre)

    bouton_l =tk.Button(fenetre, text="l")
    bouton_l.bind('<Button-1>', ver_lettre)

    bouton_m =tk.Button(fenetre, text="m")
    bouton_m.bind('<Button-1>', ver_lettre)

    bouton_n =tk.Button(fenetre, text="n")
    bouton_n.bind('<Button-1>', ver_lettre)

    bouton_o =tk.Button(fenetre, text="o")
    bouton_o.bind('<Button-1>', ver_lettre)

    bouton_p =tk.Button(fenetre, text="p")
    bouton_p.bind('<Button-1>', ver_lettre)

    bouton_q =tk.Button(fenetre, text="q")
    bouton_q.bind('<Button-1>', ver_lettre)

    bouton_r =tk.Button(fenetre, text="r")
    bouton_r.bind('<Button-1>', ver_lettre)

    bouton_s =tk.Button(fenetre, text="s")
    bouton_s.bind('<Button-1>', ver_lettre)

    bouton_t =tk.Button(fenetre, text="t")
    bouton_t.bind('<Button-1>', ver_lettre)

    bouton_u =tk.Button(fenetre, text="u")
    bouton_u.bind('<Button-1>', ver_lettre)

    bouton_v =tk.Button(fenetre, text="v")
    bouton_v.bind('<Button-1>', ver_lettre)

    bouton_w =tk.Button(fenetre, text="w")
    bouton_w.bind('<Button-1>', ver_lettre)

    bouton_x =tk.Button(fenetre, text="x")
    bouton_x.bind('<Button-1>', ver_lettre)

    bouton_y =tk.Button(fenetre, text="y")
    bouton_y.bind('<Button-1>', ver_lettre)

    bouton_z =tk.Button(fenetre, text="z")
    bouton_z.bind('<Button-1>', ver_lettre)

    #   Positionnement
    label.grid(row = 0, column = 4, columnspan=5)
    saisie.grid(row = 1, column = 0, columnspan=5)
    bouton_Ok.grid(row = 1, column = 10)
    b_indice.grid(row=10, column=7)
    b_Score.grid(row=10, column=10)

    #Positionnement lettres
    #Ligne 1
    bouton_a.grid(row = 3, column=1)    
    bouton_b.grid(row = 3, column=2)    
    bouton_c.grid(row = 3, column=3)    
    bouton_d.grid(row = 3, column=4)    
    bouton_e.grid(row = 3, column=5)    
    bouton_f.grid(row = 3, column=6)
    #Ligne 2
    bouton_g.grid(row = 4, column=1)    
    bouton_h.grid(row = 4, column=2)    
    bouton_i.grid(row = 4, column=3)    
    bouton_j.grid(row = 4, column=4)    
    bouton_k.grid(row = 4, column=5)    
    bouton_l.grid(row = 4, column=6)
    #Ligne 3
    bouton_m.grid(row = 5, column=1)    
    bouton_n.grid(row = 5, column=2)    
    bouton_o.grid(row = 5, column=3)    
    bouton_p.grid(row = 5, column=4)    
    bouton_q.grid(row = 5, column=5)    
    bouton_r.grid(row = 5, column=6)
    #Ligne 4  
    bouton_s.grid(row = 6, column=1)    
    bouton_t.grid(row = 6, column=2)
    bouton_u.grid(row = 6, column=3)
    bouton_v.grid(row = 6, column=4)
    bouton_w.grid(row = 6, column=5)
    bouton_x.grid(row = 6, column=6)
    #ligne 5
    bouton_y.grid(row = 7, column=3)
    bouton_z.grid(row = 7, column=4)
    
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
    
    affiche_mot(rep)

   

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
        jeu(True)
    fenetre = tk.Tk()
    fenetre.geometry("900x600")
    test = tk.Button(text="OK", command=Ok)
    test.pack()
    fenetre.mainloop()
    pass

def Tableau_score():
    """
    Ouvre une fentre avec les score d'afficher
    """
    global fenetre
    fenetre.destroy()
    def retour():
        fenetre.destroy()
        jeu(False)
    fenetre = tk.Tk()
    fenetre.protocol("WM_DELETE_WINDOW", retour)
    fenetre.mainloop()

start()