import tkinter as tk
import random
from tkinter import messagebox
import tkinter.font
import os


bank_mots = 0
score = 0
nbr_indice_util = 0
max_erreur = 7
taille_mots = 6
nbr_erreur = 0
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
        label.config(text = texte )

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
                if tk.messagebox.showinfo(title="Fin de partie", message="Voulez avez gagner"):
                    fenetre.destroy()
                    FinDePartie()
                return
        affiche_mot(mots)
        if not in_word:
            perdu
        return in_word

    def ver():
        """
        Verifie si l'utilisateur a bien mis un nombre de lettres egal aux nombre de lettres du mots secret
        sinon affiche un message informatife rapelent qu'il faut mettre le meme nombre de lettre 
        """
        global score, fenetre, rep
        mots = saisie.get()
        nbr_lettre = len(mots)
        if nbr_lettre != len(rep[0]) :
            tk.messagebox.showinfo(title="Invalid entry", message="Votre reponse doit avoir le meme nombre de lettre que le mot a deviner.")
            saisie.delete(0, nbr_lettre)
            return
        score += 1
        msg = "Sore : " + str(score)
        l_score.config(text = msg)
        for i in range(nbr_lettre):
            if mots[i] != rep[1][i]:
                saisie.delete(0,len(mots))
                perdu()
                return
        if tk.messagebox.showinfo(title="Fin de partie", message="Voulez avez gagner"):
            fenetre.destroy()
            FinDePartie()
        return
    
    def ver_lettre(event):
        global score
        if event.widget["bg"] == "green" or event.widget["bg"] == "red":
            return
        if verify(event.widget["text"], rep):
            event.widget.config(bg="green")
        else:
            event.widget.config(bg="red")
            perdu()
        score += 1
        msg = "Sore : " + str(score)
        l_score.config(text = msg)

    def perdu():
        global max_erreur, nbr_erreur
        nbr_erreur += 1
        if max_erreur == nbr_erreur:
            if tk.messagebox.askyesno(title="You lose", message="Dommage vous avez perdu \nVouler vous faire une nouvelle partie?"):
                fenetre.destroy()
                jeu(True)
            else:
                fenetre.destroy()

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
        msg = "Sore : " + str(score)
        l_score.config(text = msg)
        nbr_indice_util += 1
        verify(rep[1][lettre_indice[random.randint(0,len(lettre_indice)-1)]],rep)


    if(new):
        score = nbr_indice_util = 0
        fenetre =  tk.Tk()
        fenetre.geometry("900x600")
            #Mots aléatoire
        with open("src/dictionnaire.txt", "r") as file:
            bank_mots = file.read().split("\n")
        for i in range(len(bank_mots)):
            bank_mots[i] = bank_mots[i].split(";")
        print(taille_mots)
        print(bank_mots[taille_mots-1])
        index = random.randint(0, len(bank_mots[taille_mots-1])-2)
        rep = def_mot(bank_mots[taille_mots-1][index])
    else:
        fenetre =  tk.Tk()
        fenetre.geometry("900x600")
    
     #Widgets
    label = tk.Label(fenetre, font=("Helvetica",30))
    bouton_Ok  = tk.Button(fenetre, text="OK", command = ver)
    b_indice = tk.Button(fenetre, text = "indice", command = indice)
    l_score = tk.Label(fenetre, text = "Score : 0")

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
    label.grid(row = 0, column = 1, columnspan=6)
    saisie.grid(row = 1, column = 1, columnspan=6)
    bouton_Ok.grid(row = 1, column = 10)
    b_indice.grid(row=10, column=7)
    l_score.grid(row = 12, column=20)

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
            if messagebox.askyesno(message="Voulez vous vraiment nous quitter ?"):
                fenetre.destroy()    
    
    affiche_mot(rep)

   

    fenetre.protocol("WM_DELETE_WINDOW", closed)

    fenetre.mainloop()

def start():
    """
    Fonction qui demare l'application et affiche le menu.
    Renvoi vers la fonction jeu
    """
    global fenetre, taille_mots, max_erreur
    word_size = [3,4,5,6,7,8,9,10,11,12,13,14,15]
    erreur = [1,2,3,4,5,6,7,8,9]
    def Ok():
        global taille_mots, max_erreur
        taille_mots = variable.get()
        max_erreur = v_erreur.get()
        fenetre.destroy()
        jeu(True)
    
    def addWord():
        word = s_word.get()
        s_word.delete(0,len(word))
        list = []
        with open("src/dictionnaire.txt", "r") as file:
            list = file.read().split("\n")
        for i in range(len(list)):
            list[i] = list[i].split(";")
        list[len(word)-1].append(word)
        with open("src/dictionnaire.txt", "w") as file:
            for i in range(len(list)):
                for j in range(len(list[i])):
                    if(list[i][j] != ""):
                        file.write(list[i][j]+";")
                file.write("\n")


    fenetre = tk.Tk()
    fenetre.geometry("900x600")
    variable = tk.IntVar()
    variable.set(word_size[3])
    deroul = tk.OptionMenu(fenetre, variable, *word_size)
    v_erreur = tk.IntVar()
    v_erreur.set(erreur[6])
    d_erreur = tk.OptionMenu(fenetre, v_erreur, *erreur)
    l_erreur = tk.Label(fenetre, text="nombre d'echec autorisé")
    test = tk.Button(text="Start", command=Ok)
    b_taille = tk.Label(text="taille mots")
    rec = tk.StringVar
    s_word = tk.Entry(fenetre, textvariable=rec)
    b_word = tk.Button(text="ajouter un mot", command=addWord)
    rules = tk.Canvas(fenetre, width=500, height=550, bg="#ffffff")
    rules.create_text(
        (250, 25),
        text = "LE PENDU:",
        fill = "red"
    )
    rules.create_text(
        (250, 100),
        text = "Le but du jeu: trouver le mots secret\n avant d'etre pendu, vous serez pendu si vous faites trop d'erreur \n\n\tPour ce faire vous devez appuyer sur les lettres\nCe qui decouvre petit a petit le mot si la lettre et de dans.\nSi la lettre esr dans le mots, la lettre devient verte sinon elle devient rouge",
        fill = "black"
    )

    rules.grid(row=1, column = 3, rowspan= 10, columnspan=5)
    test.grid(row=11, column=3, columnspan=5)
    deroul.grid(row=1, column=1)
    b_taille.grid(row=1, column=2)
    d_erreur.grid(row = 3, column=1)
    l_erreur.grid(row=3, column= 2)
    s_word.grid(row=1, column=10)
    b_word.grid(row=1, column=11)

    fenetre.mainloop()


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

def FinDePartie():
    global fenetre, score
    name = ""
    def setName():
        name = s_name.get()
        if len(name) == 0:
            tk.messagebox.showinfo(message="vous devez d'abord entrer votre nom")
        sauvegarder_score(name, score)


    def sauvegarder_score(nom_joueur, score):
        # Charger les scores depuis le fichier dans un dictionnaire s'ils existent
        scores = {}
        #if os.stat("src/scores.txt").st_size == 0:
        f = open("src/scores.txt", "r")
        for line in f:
            key, value = line.strip().split(":")
            scores[key] = int(value)
        f.close()

        # Ajouter le score du joueur actuel au dictionnaire des scores
        scores[nom_joueur] = score

        # Écrire le dictionnaire mis à jour dans le fichier
        f = open("src/scores.txt", "w")
        for key, value in scores.items():
            f.write(f"{key}:{value}\n")
        f.close()
        if tk.messagebox.askyesno(title="Fin de partie", message="Voulez vous refaire un partie?"):
            fenetre.destroy()
            start()
        else:
            fenetre.destroy()

    fenetre = tk.Tk()
    fenetre.geometry("900x600")
    l_name = tk.Button(fenetre, text="Nom")
    text = tk.StringVar
    s_name = tk.Entry(fenetre, textvariable= text, take= "focus")
    b_enter = tk.Button(fenetre, text = "OK", command=setName)

    s_name.grid(row = 0, column = 0)
    l_name.grid(row=0, column=1)
    b_enter.grid(row=1,column=1)

    pass

start()

