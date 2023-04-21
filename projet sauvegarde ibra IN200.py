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
       
       


