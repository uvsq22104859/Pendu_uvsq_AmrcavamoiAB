
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
