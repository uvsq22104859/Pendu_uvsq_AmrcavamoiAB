import json

def sauvegarder_score(nom_joueur, score):
    # Essayer d'ouvrir le fichier "scores.json" en mode lecture
    try:
        with open("scores.json", "r") as f:
            scores = json.load(f) # Charger les scores depuis le fichier dans un dictionnaire
    # Si le fichier n'existe pas, créer un dictionnaire vide pour stocker les scores
    except FileNotFoundError:
        scores = {}
        
    # Ajouter le score du joueur actuel au dictionnaire des scores
    scores[nom_joueur] = score
    
    # Écrire le dictionnaire mis à jour dans le fichier "scores.json"
    with open("scores.json", "w") as f:
        json.dump(scores, f)





def sauvegarder_score(nom_joueur, score):
    # Essayer d'ouvrir le fichier "scores.txt" en mode lecture
    try:
        with open("scores.txt", "r") as f:
            # Charger les scores depuis le fichier dans un dictionnaire
            scores = {}
            for line in f:
                key, value = line.strip().split(":")
                scores[key] = int(value)
    # Si le fichier n'existe pas, créer un dictionnaire vide pour stocker les scores
    except FileNotFoundError:
        scores = {}
        
    # Ajouter le score du joueur actuel au dictionnaire des scores
    scores[nom_joueur] = score
    
    # Écrire le dictionnaire mis à jour dans le fichier "scores.txt"
    with open("scores.txt", "w") as f:
        for key, value in scores.items():
            f.write(f"{key}:{value}\n")





def sauvegarder_score(nom_joueur, score):
    # Charger les scores depuis le fichier dans un dictionnaire s'ils existent
    scores = {}
    with open("scores.txt", "r") as f:
        for line in f:
            key, value = line.strip().split(":")
            scores[key] = int(value)

    # Ajouter le score du joueur actuel au dictionnaire des scores
    scores[nom_joueur] = score

    # Écrire le dictionnaire mis à jour dans le fichier
    with open("scores.txt", "w") as f:
        for key, value in scores.items():
            f.write(f"{key}:{value}\n")





def sauvegarder_score(nom_joueur, score):
    # Charger les scores depuis le fichier dans un dictionnaire s'ils existent
    scores = {}
    f = open("scores.txt", "r")
    for line in f:
        key, value = line.strip().split(":")
        scores[key] = int(value)
    f.close()

    # Ajouter le score du joueur actuel au dictionnaire des scores
    scores[nom_joueur] = score

    # Écrire le dictionnaire mis à jour dans le fichier
    f = open("scores.txt", "w")
    for key, value in scores.items():
        f.write(f"{key}:{value}\n")
    f.close()
