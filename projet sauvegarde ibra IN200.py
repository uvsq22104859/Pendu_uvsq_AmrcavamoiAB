# ---------------------------------- PROJET PYTHON : IBRAHIM / GUILLAUME / ARNAUD --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

# On configure le scroller de difficulté de 0 à 8 ainsi que les differents boutons 

scroller=tk.Scale(fenetre_menu ,from_=0, to=8, orient="horizontal")


bouton_aide= tk.Button(fenetre_menu, text="Aide", command=aide, bg="green")
bouton_aide['font'] = font_bouton
bouton_aide.grid(sticky="nw")
bouton_jouer = tk.Button(fenetre_menu, text="Jouer", command=lambda : je())
bouton_quitter = tk.Button(fenetre_menu, text="Quitter", command=lambda : je(1))
bouton_charger = tk.Button(fenetre_menu, text="Charger une partie ", command= charger)
bouton_jouer['font'] = font_bouton
bouton_quitter['font'] = font_bouton
bouton_charger['font'] = font_bouton

Label_1.grid(row = 1, column = 1)
bouton_jouer.grid(row = 4, column = 1)
bouton_quitter.grid(row = 5, column = 3)
bouton_charger.grid(row = 0, column = 3)
Label_2.grid(row=5, column=0)
scroller.grid(row=5, column=1)

           
fenetre_menu.mainloop()


# On créé des listes de motes tant que le jeu est lancé
while jeu == True:
    MOTS_3_LETTRES = [
    "art", "dos", "eau", "air", "bas", "sec", "thé", "pou", "fée", "gel",
    "sel", "axe", "but", "peu", "mur", "nez","riz", "roi", "sel", "uni", "vie", "zoo", "ski", "tas" 
    ]


    MOTS_4_LETTRES = [
    "agne", "amie", "anne", "banc", "beau", "bleu", "brun", "chat", "cher",
    "coq", "croc", "doux", "fête", "flou", "froid","gare", "gite", "gris", "ivre", "jean", "lion", "lune", "mais", "ment", "nuit", "page", "pont"
    ]


    MOTS_5_LETTRES = [
    "abris", "aider", "aimer", "allée", "amour", "arbre", "argent", "assis", "aube", "avant",
    "blanc", "boule", "bruit", "champ", "chien", "chute", "corps", "douce", "école", "écran",
    "faire", "fille", "fleur", "goutte", "grain", "habit", "jouer", "laisse", "lettre", "livre"
    ]


    MOTS_6_LETTRES = [
    "absent", "amical", "ananas", "anonyme", "artichaut", "ascenseur", "attaché", "automne", "ballon",
    "bataille", "bonheur", "courage", "décorer", "écouter", "épouser", "favori", "glisser", "horizon", "inventer",
    "jardins", "joueurs", "libre", "lumière", "magasin", "numéro", "object", "parcour", "querell", "rougeur"
    ]


    MOTS_7_LETTRES = [
    "abandon", "accueil", "affiche", "agréger", "aliments", "biberon", "branche", "capable", "chauffe", "commande",
    "compter", "conseil", "coupure", "détester", "dormir", "enfants", "ensemble", "expression", "flèches", "gardien",
    "géograph", "jogging", "lumineux", "marchand", "meubles", "nourritu", "organise", "parcours", "rencontr", "téléphon"
    ]

    MOTS_8_LETTRES = ["actuelle", "certaine", "chaudron", "défenseur", "épouvant", "français", "galaxie", "historie", "inconnue", "jongleur", "kamikaze", "loups-garous", "merveille", "nutrition", "opposant"]

    MOTS_9_LETTRES = ["alphabet", "banquiers", "carburant", "difficile", "éloquence", "fantasmes", "gymnastique", "habituels", "imaginaire", "jardinage", "kilomètre", "littéraire", "ministère", "nutrition", "observation", "panoramique", "quadriller", "radiateur", "soutenues", "téléphone"]
    
    MOTS_10_LETTRES = ["abdominaux", "bienveillance", "chocolatier", "débrouillard", "équilibriste", "fleurissement", "généreusement", "hémisphère", "imperméable", "jonglerie", "kilométrage", "librairies", "méthodiques", "nécessaires", "opportuniste", "photovoltaïque", "quantitatives", "récupérables", "somnambules", "turbulences"]
    
    MOTS_11_LETTREETPLUS = ["aménagements", "bouleversant", "contemplatif", "développante", "économiquement", "fascinatrice", "gratuitement", "hétérogène", "inattendues", "justification", "kangourousses", "luminescente", "méticuleuse", "nouvellement", "ostentatoire", "philanthrope", "quintessence", "radiodiffuse", "surveillante", "typographique"]

   
   
    liste_liste= [MOTS_3_LETTRES,MOTS_4_LETTRES,MOTS_5_LETTRES,MOTS_6_LETTRES,MOTS_7_LETTRES,MOTS_8_LETTRES,MOTS_9_LETTRES,MOTS_10_LETTRES,MOTS_11_LETTREETPLUS]
    # On crée une fonction qui charge les mots aléatoirement
    def choisirliste(liste,entier):
       return liste[entier]
   
   
    liste = choisirliste(liste_liste, difficulte)

    # Ici si le mot saisi est vrai le "mot" prendra le "mot" choisi dans la variable "mote" sinon il reprendra un mot de la liste
    if chrge:
        mot = mote
    else:
        mot = mots(liste)

   
    print(mot)
       
    # On créé la fonction qui remplacera chaque lettre du mot en "*"
    def tiret():
        global mot
        affichage=[]
        for i in range(len(mot)):
            affichage.append('*')
        return affichage

    # On crée la variables des scores 
    erreur = 0


    def ecrit_les_coords(evt):
        global erreur
        pos_x, pos_y = evt.x, evt.y
        erreur+=1
        print(pos_x,pos_y)
    

    # Ici si l'utilisateur devine le mot la fenetre se fermera avec la fonction ".destroy()" sinon le score augmentera de 1 et affichera un trait dans le canvas 

       def deviner_le_mt(mot1):
        global erreur
        mot1 = mot1.upper()
        if mot == mot1:
            messagebox.showinfo(fenetre,message="Vous avez gagné !")
            fenetre.destroy()
        else:
            erreur+=1
            creer_lignes(liste_ligne, erreur, canvas_personnage)
              
    # On crée l'interface graphique du pendu
    fenetre = tk.Tk()
    fenetre.title("pendu") # titre
    fenetre.geometry("820x555+400+200") # taille

    mot_pointille = tiret() # On retrouve ici notre fonctions pour les "*"

    canvas_personnage = tk.Canvas(fenetre, width=500, height=400, bg="green") # Ici c'est pour le perso

    lettre_deja_donne = [] # nmbr d'erreur
    lettre_deja_donne2 = [] # lettres deja donné par le jeu 
    label_erreur = tk.Label(fenetre, text="Vous avez fait "+str(erreur)+" erreur(s)") # le score (score ici veut dire erreur)
    label_lettre_deja_utilise = tk.Label(fenetre, text="Vous n'avez utilisé aucune lettre : ") # les lettres deja utilisés par l'utilisateur

    entre = tk.Entry(fenetre,width=10,font = ("helvetica", "10"))

    button_pour_mot = tk.Button(fenetre, text="Deviner le mot ?", command= lambda:deviner_le_mt(entre.get())) # espace de saisie pour deviner le mot

    reussite = 0
    label_score = tk.Label(fenetre, text = "Score : "+str(score)) # le score de l'utilisateur



    def change_label_deja(lett): # cette fonction met a jour la fonction "lebel_lettre_deja_utilise" qui met a jour les lettres donner par le jour 
        global lettre_deja_donne2
        cdc = ''
        for lettre in lettre_deja_donne2:
            cdc = cdc + lettre + ", "
        label_lettre_deja_utilise.config(text="Vous avez déjà utilisé les lettres : "+cdc)

    def change_label_erreur(): # celle si met a jour le fonction des lebels de score et d'erreur
        global erreur
        global score
        label_erreur.config(text="Vous avez fait "+str(erreur)+" erreur(s)")
        label_score.config(text="Score : "+str(score))
        fenetre.after(10, change_label_erreur)

    change_label_erreur()



    # fonction qui crée les lignes du pendu (sources prises d'internet)
    liste_ligne=[[100,400,400,400],[150,400,150,150],[150,150,300,150],[200,150,150,200],[300,150,300,200],[325,250,275,200],[ 300,250,300,300],[300,275,325,275],[275,275,325,275],   [300,300,325,320],[300,300,275,320]]

    def creer_lignes(liste_ligne, index, canevas):
        x1, y1, x2, y2 = liste_ligne[index-1]
        if index != 6:
            canevas.create_line(x1, y1, x2, y2, fill="black")
        else: canevas.create_oval(x1, y1, x2, y2, outline="black")


    # Ce code crée un label qui affiche le mot à deviner sous forme de tirets. La variable mot_pointille contient une chaîne de caractères avec un tiret pour chaque lettre du mot à deviner, par exemple "-----" si le mot a 5 lettres. La boucle for parcourt cette chaîne de caractères en sens inverse et construit une nouvelle chaîne mot_pointille_shw avec un espace entre chaque tiret et chaque lettre déjà trouvée. Cette chaîne est utilisée pour initialiser le texte du label label_pointille.
    mot_pointille_shw = ""
    for i in range(len(mot_pointille)):
        mot_pointille_shw = ' '+mot_pointille[i]+mot_pointille_shw

    label_pointille = tk.Label(fenetre, text=str(mot_pointille_shw))

    # La fonction change_label_pointille permet de mettre à jour le texte du label label_pointille lorsque le joueur trouve une nouvelle lettre du mot. Elle reçoit en argument une chaîne de caractères mot qui contient le mot à deviner avec les lettres déjà trouvées à leur place.
    def change_label_pointille(mot):
        mot_pointille_shw = ""
        for i in range(len(mot)):
            mot_pointille_shw = mot_pointille_shw+' '+mot[i]
        label_pointille.config(text=mot_pointille_shw)

    nb_lettre=0
    l_rien=[]
    for i in range(len(mot)):
        if not(mot[i] in l_rien):
            l_rien.append(mot[i])
            nb_lettre+=1

    # La fonction rejouer est appelée lorsque la partie est terminée et permet de demander au joueur s'il veut rejouer. Elle prend en argument un entier ent qui vaut 1 si le joueur veut rejouer et 0 sinon, ainsi que la fenêtre fen à fermer. Si ent est 1, la variable jeu est mise à True pour relancer le jeu, sinon elle est mise à False pour quitter le programme.
    def rejouer(ent,fen):
        global jeu
        if ent == 1:
            jeu = True
        else: jeu = False
        fen.destroy()

    fenetre.grid_rowconfigure(13, weight=1)

    # foction qui enregistre le mot actuel et le score actuel du jeu dans un fichier CSV.
    def sauvegarder():
        global mot
        global score
        path = "C:/Users/Administrateur/Desktop/save.csv"
        mode = "w"
        csv_save = open(path, mode)
        csv_save.write(mot+","+str(score)+"\n")
        csv_save.close()
   
    bouton_save = tk.Button(fenetre, text="Sauvegarder", command=sauvegarder)
   

    # la fonction utilise plusieurs variables globales telles que mot, mot_pointille, erreur, liste_ligne, canvas_personnage, reussite, lettre_deja_donne, nb_lettre et score pour suivre l'état actuel du jeu et mettre à jour les éléments visuels en conséquence. La fonction utilise également deux autres fonctions change_label_deja et creer_lignes pour mettre à jour le canevas et le libellé de la liste de lettres déjà sélectionnées.
    def lettre_dans_le_mot_ou_erreur(lettre):
        global mot
        global mot_pointille
        global erreur
        global liste_ligne
        global canvas_personnage
        global reussite
        global lettre_deja_donne
        global nb_lettre
        global score
        if lettre in mot:
            for i in range(len(mot)):
                if mot[i] == lettre:
                    mot_pointille[i] = lettre
            if not(lettre in lettre_deja_donne2):
                lettre_deja_donne2.append(lettre)
            change_label_deja(lettre)
            #print(mot_pointille)
            if not (lettre in lettre_deja_donne):
                change_label_pointille(mot_pointille)
                reussite += 1
                lettre_deja_donne.append(lettre)
                #print(reussite)
                #print(mot)
       
            if reussite == nb_lettre:
                messagebox.showinfo(fenetre,message="Vous avez gagné !")
                fenetre.destroy()
       
        else:
           
            if not(lettre in lettre_deja_donne2):
                lettre_deja_donne2.append(lettre)
                change_label_deja(lettre)
                erreur +=1
                creer_lignes(liste_ligne, erreur, canvas_personnage)
                score += 1
            if erreur >= 11:
                messagebox.showinfo(fenetre,message="Vous avez perdu !")
                fenetre.destroy()



    # les lettres (source internet)      
    boutonA=tk.Button(fenetre,text="A",command=lambda : lettre_dans_le_mot_ou_erreur("A"))
    boutonB=tk.Button(fenetre,text="B",command=lambda : lettre_dans_le_mot_ou_erreur("B"))
    boutonC=tk.Button(fenetre,text="C",command=lambda : lettre_dans_le_mot_ou_erreur("C"))
    boutonD=tk.Button(fenetre,text="D",command=lambda : lettre_dans_le_mot_ou_erreur("D"))
    boutonE=tk.Button(fenetre,text="E",command=lambda : lettre_dans_le_mot_ou_erreur("E"))
    boutonF=tk.Button(fenetre,text="F",command=lambda : lettre_dans_le_mot_ou_erreur("F"))
    boutonG=tk.Button(fenetre,text="G",command=lambda : lettre_dans_le_mot_ou_erreur("G"))
    boutonH=tk.Button(fenetre,text="H",command=lambda : lettre_dans_le_mot_ou_erreur("H"))
    boutonI=tk.Button(fenetre,text="I",command=lambda : lettre_dans_le_mot_ou_erreur("I"))
    boutonJ=tk.Button(fenetre,text="J",command=lambda : lettre_dans_le_mot_ou_erreur("J"))
    boutonK=tk.Button(fenetre,text="K",command=lambda : lettre_dans_le_mot_ou_erreur("K"))
    boutonL=tk.Button(fenetre,text="L",command=lambda : lettre_dans_le_mot_ou_erreur("L"))
    boutonM=tk.Button(fenetre,text="M",command=lambda : lettre_dans_le_mot_ou_erreur("M"))
    boutonN=tk.Button(fenetre,text="N",command=lambda : lettre_dans_le_mot_ou_erreur("N"))
    boutonO=tk.Button(fenetre,text="O",command=lambda : lettre_dans_le_mot_ou_erreur("O"))
    boutonP=tk.Button(fenetre,text="P",command=lambda : lettre_dans_le_mot_ou_erreur("P"))
    boutonQ=tk.Button(fenetre,text="Q",command=lambda : lettre_dans_le_mot_ou_erreur("Q"))
    boutonR=tk.Button(fenetre,text="R",command=lambda : lettre_dans_le_mot_ou_erreur("R"))
    boutonS=tk.Button(fenetre,text="S",command=lambda : lettre_dans_le_mot_ou_erreur("S"))
    boutonT=tk.Button(fenetre,text="T",command=lambda : lettre_dans_le_mot_ou_erreur("T"))
    boutonU=tk.Button(fenetre,text="U",command=lambda : lettre_dans_le_mot_ou_erreur("U"))
    boutonV=tk.Button(fenetre,text="V",command=lambda : lettre_dans_le_mot_ou_erreur("V"))
    boutonW=tk.Button(fenetre,text="W",command=lambda : lettre_dans_le_mot_ou_erreur("W"))
    boutonX=tk.Button(fenetre,text="X",command=lambda : lettre_dans_le_mot_ou_erreur("X"))
    boutonY=tk.Button(fenetre,text="Y",command=lambda : lettre_dans_le_mot_ou_erreur("Y"))
    boutonZ=tk.Button(fenetre,text="Z",command=lambda : lettre_dans_le_mot_ou_erreur("Z"))

    bouton_quit=tk.Button(fenetre,text='Quitter',command=lambda : fenetre.destroy())
   

 
    boutonA.grid(column=0,row=10)
    boutonB.grid(column=1,row=10)
    boutonC.grid(column=2,row=10)
    boutonD.grid(column=3,row=10)
    boutonE.grid(column=4,row=10)
    boutonF.grid(column=5,row=10)
    boutonG.grid(column=0,row=11)
    boutonH.grid(column=1,row=11)
    boutonI.grid(column=2,row=11)
    boutonJ.grid(column=3,row=11)
    boutonK.grid(column=4,row=11)
    boutonL.grid(column=5,row=11)
    boutonM.grid(column=0,row=12)
    boutonN.grid(column=1,row=12)
    boutonO.grid(column=2,row=12)
    boutonP.grid(column=3,row=12)
    boutonQ.grid(column=4,row=12)
    boutonR.grid(column=5,row=12)
    boutonS.grid(column=0,row=13)
    boutonT.grid(column=1,row=13)
    boutonU.grid(column=2,row=13)
    boutonV.grid(column=3,row=13)
    boutonW.grid(column=4,row=13)
    boutonX.grid(column=5,row=13)
    boutonY.grid(column=2,row=14)
    boutonZ.grid(column=3,row=14)

    canvas_personnage.grid(row=0, column=0, rowspan=10,columnspan=6)
    label_erreur.grid(row=0,column=7)
    label_pointille.grid(row = 1, column=7)
    label_lettre_deja_utilise.grid(row = 2, column=6, columnspan=3) 
    entre.grid(row= 7, column=6)
    button_pour_mot.grid(row= 7, column=7)
    label_score.grid(row=9,column=6)
    bouton_save.grid(row = 9, column=7)
    bouton_quit.grid(row=14,column=10)

    fenetre.resizable(width = False, height = False)

    fenetre.mainloop()
   
    fenetre_fin = tk.Tk()
    fenetre_fin.geometry("100x100+500+200")
    fenetre_fin.grid_rowconfigure(1, weight=1)
    fenetre_fin.grid_rowconfigure(2, weight=1)
    bouton_rejouer = tk.Button(fenetre_fin, text='Rejouer ?', command=lambda : rejouer(1,fenetre_fin))
    bouton_quitter = tk.Button(fenetre_fin, text='Quitter ?', command=lambda : rejouer(0,fenetre_fin))
    bouton_rejouer.grid(row=0, column=0)
    bouton_quitter.grid(row=1, column=0)

    fenetre_fin.mainloop()


    #----------------------------------------------------------------------------------------------------------- FIN       
  
       
       


