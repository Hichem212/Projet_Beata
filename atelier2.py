# -*- coding: utf-8 -*-
from random import *

#### REPRESENTATION DES DONNEES
### Initialisation des grilles et autres variables de jeu

def initialiser_configuration_debut():
    return [["X", "X", "X","X","X","X","X","X","X"],
            ["X", "X", "X","X","X","X","X","X","X"],
            ["X", "X", "X","X","X","X","X","X","X"],
            [" ", " ", " "," "," "," "," "," "," "],
            [" ", " ", " "," "," "," "," "," "," "],
            [" ", " ", " "," "," "," "," "," "," "],
            ["O", "O", "O","O","O","O","O","O","O"],
            ["O", "O", "O","O","O","O","O","O","O"],
            ["O", "O", "O","O","O","O","O","O","O"]]

def initialiser_configuration_milieu():
    return [["X", "X", "X","X","X","X","X","X","X"],
            ["X", " ", "X"," ","X","X","X"," ","X"],
            [" ", " ", "X","O","O","X","X"," "," "],
            [" ", " ", " "," "," "," "," "," "," "],
            [" ", " ", " "," "," "," "," "," "," "],
            [" ", " ", " "," "," "," "," "," "," "],
            ["O", " ", "X"," "," "," ","O","O","O"],
            ["O", "X", "O","O","O"," ","O","O","O"],
            ["O", "O", "O","O","O","O","O","O","O"]]

def initialiser_configuration_fin():
     return [["X", "X","X","X"," "," ","O"," "," "],
            [" ", " ", "O"," "," "," "," "," "," "],
            [" ", " ", "O","X"," "," "," ","O"," "],
            [" ", " ", " "," "," "," "," "," "," "],
            [" ", " ", " "," "," "," "," "," "," "],
            [" ", " ", " "," "," "," "," "," "," "],
            [" ", " ", " "," "," "," ","X"," "," "],
            [" ", " ", " "," "," "," "," "," "," "],
            [" ", "O", "O"," "," "," ","O","O","O"]]


#### Représentation graphique

#Fonction auxiliaire qui permet d'afficher l'indice de la colonne
def afficher_indice_colonne(grille):
    
    print("  ",end=" ") #Ce print permet de s'aligner avec les lettres dans la colonne
    for j in range(len(grille[0])):
        print(" ",j+1," ",end=" ")
    print()

#Fonction auxiliaire qui permet d'afficher les lignes
def afficher_ligne(grille,i):
    print(chr(65+i) + ' |',end="") #Affiche de l'indice de la ligne 
    for j in range(len(grille[i])):
        print(" ",grille[i][j] ," ",end="")
        if j < len(grille[i])-1:
            print("|",end="")
    print()

#Fonction auxiliaire qui permet d'afficher les séparateurs
def afficher_separateur(grille):
    print("  ", end="")
    for j in range(len(grille[0])):
        print("------", end="")
    print()  

#Fonction auxiliaire qui permet de connaitre le nombre de pion dans la grille de chaque joueur
def nombre_de_pion(grille):

    nbr_pion1,nbr_pion2 = 0,0

    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == "X":
                nbr_pion1+=1

            if grille[i][j] == "O":
                nbr_pion2+=1
    
    print("Joueur 1 : ",nbr_pion1,"pion" "\t\t\t" "joueur 2 : ",nbr_pion2,"pion")
    return nbr_pion1,nbr_pion2

#Fonction qui permet d'afficher la grille complète
def afficher_grille(grille):

    afficher_indice_colonne(grille) #Affichage de l'indice des colonnes

    for i in range(len(grille)):
        afficher_ligne(grille,i) #Affichage des lignes
        if i < len(grille) -1:
            afficher_separateur(grille) #Affichage des séparations entre les lignes
    nombre_de_pion(grille)

### Fonction de vérification
### SAISIE

#Fonction qui permet de savoir si un pion est dans la grille
def est_dans_grille(ligne, colonne, grille):
    return 0 <= ligne < len(grille) and 0 <= colonne < len(grille[0])


#Fonction qui permet de savoir si la valeur de case entrée est au bon format
def est_au_bon_format(message):
    if len(message) != 2:
        return False
    
    if not ('A' <= message[0] <= 'Z'):
        return False

    if not ('1' <= message[1] <= '9'):
        return False

    return True

#Fonction qui permet de choisir la destination ou l'on veut placer le pion
def saisir_coordonnees_arrivee(grille):

    while True:

        entree = input("Entrez une coordonée : ").upper() #On utilise .upper pour mettre la lettre en majuscule 

        if not est_au_bon_format(entree):
            print("Le format que vous avez rentré est invalide veuillez réesayer")
            continue
    
        ligne = ord(entree[0])-65 #Pour avoir la valeur de la ligne en lettre
        colonne = int(entree[1])-1 #Conversion en entier et ajuster pour l'index 0 
        
        #Cette condition permet de vérifier qu'on est bien dans la grille et que l'endroit ou l'on veut placer notre pion n'est pas un endroit deja prit
        if est_dans_grille(ligne, colonne, grille) and grille[ligne][colonne] == " ": 
            return ligne, colonne
        else:
            print("La case est en dehors de la grille ou elle est déja occupé")

#Fonction qui permet de choisir le pion que l'on souhaite déplacer
def saisir_coordonees_depart(grille):
    while True:

        depart = input("Entrez la coordonée du pion que vous voulez déplacé : ").upper()

        if not est_au_bon_format(depart):
            print("Le format que vous avez rentré est invalide veuillez réesayer")
            continue
        
        ligne = ord(depart[0])-65 #Pour avoir la valeur de la ligne en lettre
        colonne = int(depart[1])-1 #Conversion en entier et ajuster pour l'index 0 

        if grille[ligne][colonne] == 'X' or grille[ligne][colonne] == 'O': #Cette condition permet de savoir si l'on choisit bien un pion
            return ligne,colonne
        else:
            print("Cette case est vide")

#Fonction qui permet de verifier si une case est vide
def est_case_vide(grille, l, c):
    return est_dans_grille(l, c, grille) and grille[l][c] == " "


#Fonction qui permet de vérifié si c'est la case d'un adversaire
def est_case_adversaire(grille, l, c, pion):
    return est_dans_grille(l, c, grille) and grille[l][c] != pion and grille[l][c] != " "


def direction_verticale(l1, c1, l2, c2): #l1,l2,c1,c2 représente successivement ligne 1 , ligne 2,colonne 1 et colonne 2
    if c1 == c2 and l1 != l2:
        return (l2 - l1) // (l2 - l1), 0  # Résultat sera +1 ou -1
    return None

def direction_horizontale(l1, c1, l2, c2):
    if l1 == l2 and c1 != c2:
        return 0, (c2 - c1) // (c2 - c1)  # Résultat sera +1 ou -1
    return None

def direction_diagonale(l1,c1,l2,c2):
    dl = l2 - l1 # Représente la diagonale de la ligne
    dc = c2 - c1 # Représente la diagonale de la colonne

    # Vérifie que les deux mouvements (vertical et horizontal) sont non nuls et de même "longueur"
    if dl != 0 and dc != 0 and dl * dl == dc * dc:
        return dl // dl, dc // dc  # renvoie (+1, -1, etc.)
    return None

def obtenir_direction(l1, c1, l2, c2):
    #Retourne la direction (dl, dc) si elle est valide (verticale, horizontale ou diagonale), sinon None
    direction = direction_verticale(l1, c1, l2, c2)
    if direction is not None:
        return direction

    direction = direction_horizontale(l1, c1, l2, c2)
    if direction is not None:
        return direction

    return direction_diagonale(l1, c1, l2, c2)


def chemin_vide(grille, l1, c1, l2, c2):
    direction = obtenir_direction(l1, c1, l2, c2)

    dl, dc = direction
    l, c = l1 + dl, c1 + dc

    while (l, c) != (l2, c2):
        if not est_case_vide(grille, l, c):
            return False
        l += dl
        c += dc

    return True

def deplacement_retournement(grille, l1, c1, l2, c2, pion):
    # Déterminer la direction
    direction = obtenir_direction(l1, c1, l2, c2)

    dl, dc = direction
    l_saut = l2 - dl
    c_saut = c2 - dc

    # Vérifie que la case à sauter est bien un pion adverse
    if not est_case_adversaire(grille, l_saut, c_saut, pion):
        return False

    # Vérifie que toutes les cases entre départ et le pion sauté sont vides
    if not chemin_vide(grille, l1, c1, l_saut, c_saut):
        return False

    # Vérifie que la case d'arrivée est bien vide
    if not est_case_vide(grille, l2, c2):
        return False

    # Appliquer le retournement
    grille[l1][c1] = " "
    grille[l_saut][c_saut] = pion  # retourne le pion sauté
    grille[l2][c2] = pion
    return True

def deplacement_elimination(grille, l1, c1, l2, c2, pion):
    if not est_case_adversaire(grille, l2, c2, pion):
        return False
    if abs(l2 - l1) < 2 and abs(c2 - c1) < 2:
        return False  # pas de voisins immédiats
    if not chemin_vide(grille, l1, c1, l2, c2):
        return False

    # Exécution du déplacement
    grille[l2][c2] = pion
    grille[l1][c1] = " "
    return True


def tour_de_jeu(grille, pion):
    print("Tour du joueur 1(X) " if pion == 'X' else "Tour du joueur 2(O) ")

    while True:
        type_deplacement = input("Entrez le type de déplacement ('e' pour élimination, 'r' pour retournement) : ").lower()
        if type_deplacement in ['e', 'r']:
            break
        print(" Type invalide. Entrez 'e' ou 'r'.")

    # Première tentative de déplacement
    deplacement_reussi = False
    while not deplacement_reussi:
        l1, c1 = saisir_coordonees_depart(grille)
        l2, c2 = saisir_coordonnees_arrivee(grille)

        if grille[l1][c1] != pion:
            print(" Ce n'est pas votre pion.")
            continue

        if type_deplacement == 'e':
            deplacement_reussi = deplacement_elimination(grille, l1, c1, l2, c2, pion)
        else:
            deplacement_reussi = deplacement_retournement(grille, l1, c1, l2, c2, pion)

        if not deplacement_reussi:
            print(" Déplacement invalide selon les règles.")

    # Si c'est un retournement, proposer l'enchaînement
    if type_deplacement == 'r':
        encore = input("Voulez-vous continuer les sauts ? (o/n) : ").lower()
        while encore == 'o':
            afficher_grille(grille)
            deplacement_reussi = False
            while not deplacement_reussi:
                l1, c1 = saisir_coordonees_depart(grille)
                l2, c2 = saisir_coordonnees_arrivee(grille)
                if grille[l1][c1] != pion:
                    print("⛔ Ce n'est pas votre pion.")
                    continue
                deplacement_reussi = deplacement_retournement(grille, l1, c1, l2, c2, pion)
                if not deplacement_reussi:
                    print("⛔ Saut invalide.")
            encore = input("Continuer les sauts ? (o/n) : ").lower()


### Jeu de test

def test_est_case_vide():
    grille = initialiser_configuration_debut()

    assert est_case_vide(grille, 3, 3) == True
    assert est_case_vide(grille, 0, 0) == False
    assert est_case_vide(grille, 9, 9) == False  # hors grille

def test_est_case_adversaire():

    grille = initialiser_configuration_debut()
    assert est_case_adversaire(grille, 0, 0, "O") == True   # case X, adversaire de O
    assert est_case_adversaire(grille, 0, 0, "X") == False  # case X, même camp
    assert est_case_adversaire(grille, 3, 3, "O") == False  # case vide
    assert est_case_adversaire(grille, 9, 9, "X") == False  # hors grille

def test_direction_verticale():
    assert direction_verticale(2, 2, 5, 2) == (1, 0)
    assert direction_verticale(5, 4, 2, 4) == (-1, 0)
    assert direction_verticale(2, 3, 2, 5) == None

def test_direction_horizontale():
    assert direction_horizontale(4, 1, 4, 6) == (0, 1)
    assert direction_horizontale(7, 5, 7, 2) == (0, -1)
    assert direction_horizontale(3, 3, 6, 3) == None

def test_direction_diagonale():
    assert direction_diagonale(2, 2, 5, 5) == (1, 1)
    assert direction_diagonale(6, 6, 3, 3) == (-1, -1)
    assert direction_diagonale(1, 4, 4, 1) == (1, -1)
    assert direction_diagonale(0, 0, 0, 5) == None

def test_est_dans_grille(grille):
    assert est_dans_grille(0,0,grille) == True
    assert est_dans_grille(0,1,grille) == True
    assert est_dans_grille(9,99,grille) == False
    assert est_dans_grille(1,55,grille) == False
    assert est_dans_grille(2,2,grille) == True
    assert est_dans_grille(4,5,grille) == True
    assert est_dans_grille(0,0,grille) == True
    assert est_dans_grille(-2,-1,grille) == False


def test_est_au_bon_format():
    assert est_au_bon_format("A2") == True
    assert est_au_bon_format("A22") == False
    assert est_au_bon_format("a2") == False
    assert est_au_bon_format("a55") == False
    assert est_au_bon_format("AA") == False
    assert est_au_bon_format("11") == False 
    assert est_au_bon_format("1a") == False
    assert est_au_bon_format("a1") == False
    assert est_au_bon_format("B-1") == False
    assert est_au_bon_format("B5") == True
    assert est_au_bon_format("F6") == True

def test_chemin_vide():

    grille = initialiser_configuration_milieu()

    # Cas de chemins vides
    assert chemin_vide(grille, 3, 0, 3, 4) == True     # Ligne vide
    assert chemin_vide(grille, 5, 3, 2, 3) == False    # Bloqué par un pion en (3,3)
    assert chemin_vide(grille, 2, 3, 5, 6) == False    # diagonale, mais bloqué
    assert chemin_vide(grille, 5, 0, 2, 3) == False    # diagonale bloquée
    assert chemin_vide(grille, 3, 3, 3, 6) == True     # Ligne horizontale vide

    # Cas de chemins non valides (hors direction alignée)
    assert chemin_vide(grille, 1, 1, 2, 4) == False


def test_deplacement_elimination():

    # Copie pour test (on évite de modifier la config de base)
    grille = initialiser_configuration_milieu()

    # Cas valide : un pion X en (0,0) peut éliminer un pion O éloigné (on crée manuellement le cas ici)
    grille[0][0] = "X"
    grille[0][4] = "O"
    grille[0][1] = " "
    grille[0][2] = " "
    grille[0][3] = " "

    assert deplacement_elimination(grille, 0, 0, 0, 4, "X") == True
    assert grille[0][4] == "X"
    assert grille[0][0] == " "

    # Cas invalide : pas de case vide entre départ et adversaire (ils sont voisins)
    grille = initialiser_configuration_milieu()
    grille[2][3] = "X"
    grille[2][4] = "O"
    assert deplacement_elimination(grille, 2, 3, 2, 4, "X") == False

    # Cas invalide : il y a un obstacle dans le chemin
    grille = initialiser_configuration_milieu()
    grille[0][0] = "X"
    grille[0][1] = "O"
    grille[0][4] = "O"
    assert deplacement_elimination(grille, 0, 0, 0, 4, "X") == False

    # Cas invalide : la case d'arrivée n'est pas occupée par un pion adverse
    grille = initialiser_configuration_milieu()
    grille[1][1] = "X"
    grille[1][4] = " "
    assert deplacement_elimination(grille, 1, 1, 1, 4, "X") == False


### Code principal  

def main():

    #Execution affichage sur les 3 grilles ainsi que test 
    print("Configuration de début :")
    afficher_grille(initialiser_configuration_debut())
    test_est_dans_grille(initialiser_configuration_debut())
    test_est_au_bon_format()
    print("\n")
    print("Configuration de milieu :")
    afficher_grille(initialiser_configuration_milieu())
    test_est_dans_grille(initialiser_configuration_milieu())
    test_est_au_bon_format()
    print("\n")
    print("Configuration de fin :")
    afficher_grille(initialiser_configuration_fin())
    test_est_dans_grille(initialiser_configuration_fin())
    test_est_au_bon_format()
    
    #Déplacement dans la grille(Les règles du jeu ne sont pas appliqué comme décrit dans l'atelier)
    print("\n");
    print("Bienvenue dans le jeu !")

    grille = initialiser_configuration_debut()  # Vous pouvez modifier cette partie pour choisir la grille que vous voulez tester
    tour = randint(1,2)  # 1 pour Joueur 1 (X), 2 pour Joueur 2 (O)
    print("Le joueur 1 joue avec les pions X et le joueur 2 joue avec les pions O")
    for i in range(4): #On fait seulement 4 tours pour avoir un aperçu des mouvements
        afficher_grille(grille)
        tour_de_jeu(grille, "X" if tour == 1 else "O")
        tour = 3 - tour  # alterner joueur

        



if __name__ == "__main__":
    main()


