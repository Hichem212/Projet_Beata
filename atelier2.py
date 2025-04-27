# -*- coding: utf-8 -*-
from random import randint

#### REPRESENTATION DES DONNEES
### Initialisation des grilles et autres variables de jeu

def initialiser_configuration_debut():
    """
    Initialise la configuration de départ du jeu.
    Retourne une grille 9x9 avec les pions des deux joueurs positionnés.
    """
    return [
        ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
    ]

def initialiser_configuration_milieu():
    """
    Initialise une configuration intermédiaire du jeu pour les tests.
    Retourne une grille 9x9 avec des pions déjà déplacés.
    """
    return [
        ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", " ", "X", " ", "X", "X", "X", " ", "X"],
        [" ", " ", "X", "O", "O", "X", "X", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["O", " ", "X", " ", " ", " ", "O", "O", "O"],
        ["O", "X", "O", "O", "O", " ", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
    ]

def initialiser_configuration_fin():
    """
    Initialise une configuration de fin du jeu pour les tests.
    Retourne une grille 9x9 avec peu de pions restants.
    """
    return [
        ["X", "X", "X", "X", " ", " ", "O", " ", " "],
        [" ", " ", "O", " ", " ", " ", " ", " ", " "],
        [" ", " ", "O", "X", " ", " ", " ", "O", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", "X", " "],
        [" ", " ", " ", " ", " ", " ", "X", " ", " "],
        [" ", " ", " ", " ", " ", " ", "O", " ", " "],
        [" ", "O", "O", " ", " ", " ", " ", "O", "O"]
    ]

#### Représentation graphique

def afficher_indice_colonne(grille):
    """
    Affiche les indices des colonnes pour faciliter la lecture de la grille.
    """
    print("  ", end=" ")  # Alignement avec les lettres des colonnes
    for j in range(len(grille[0])):
        print(" ", j + 1, " ", end=" ")
    print()

def afficher_ligne(grille, i):
    """
    Affiche une ligne de la grille avec son indice.
    """
    print(chr(65 + i) + ' |', end="")  # Affiche l'indice de la ligne (A, B, C, etc.)
    for j in range(len(grille[i])):
        print(" ", grille[i][j], " ", end="")
        if j < len(grille[i]) - 1:
            print("|", end="")
    print()

def afficher_separateur(grille):
    """
    Affiche une ligne de séparation entre les lignes de la grille.
    """
    print("  ", end="")
    for j in range(len(grille[0])):
        print("------", end="")
    print()

def nombre_de_pion(grille):
    """
    Compte le nombre de pions de chaque joueur dans la grille.
    Retourne un tuple avec le nombre de pions du joueur 1 (X) et du joueur 2 (O).
    """
    nbr_pion1, nbr_pion2 = 0, 0
    for i in range(len(grille)):
        for j in range(len(grille[i])): #Dans le cas ou la grille n'est pas carré 
            if grille[i][j] == "X":
                nbr_pion1 += 1
            if grille[i][j] == "O":
                nbr_pion2 += 1
    #print("Joueur 1 : ", nbr_pion1, "pion" "\t\t\t" "Joueur 2 : ", nbr_pion2, "pion")
    return nbr_pion1, nbr_pion2

def afficher_grille(grille):
    """
    Affiche la grille complète avec les indices des lignes et des colonnes.
    """
    afficher_indice_colonne(grille)  # Affichage des indices des colonnes
    for i in range(len(grille)):
        afficher_ligne(grille, i)  # Affichage des lignes
        if i < len(grille) - 1:
            afficher_separateur(grille)  # Affichage des séparations entre les lignes
    nbr_pion1,nbr_pion2 = nombre_de_pion(grille)  # Affichage du nombre de pions de chaque joueur
    print("Joueur 1 : ", nbr_pion1, "pion" "\t\t\t" "Joueur 2 : ", nbr_pion2, "pion")

#### Fonctions de vérification

def est_dans_grille(ligne, colonne, grille):
    """
    Vérifie si une coordonnée est dans les limites de la grille.
    Retourne True si la coordonnée est valide, False sinon.
    """
    return 0 <= ligne < len(grille) and 0 <= colonne < len(grille[0])

def est_au_bon_format(message):
    """
    Vérifie si une entrée utilisateur est au bon format (ex: "A2").
    Retourne True si le format est valide, False sinon.
    """
    if len(message) != 2:
        return False
    if not ('A' <= message[0] <= 'Z'):
        return False
    if not ('1' <= message[1] <= '9'):
        return False
    return True

def saisir_coordonnees_arrivee(grille):
    """
    Permet à l'utilisateur de saisir les coordonnées de d'arrivé  pour un déplacement.
    Retourne les coordonnées (ligne, colonne) si elles sont valides, sinon demande à l'utilisateur de réessayer.
    """
    while True:
        entree = input("Entrez une coordonnée d'arrivée : ").upper()
        if not est_au_bon_format(entree):
            print("Format invalide,veuillez réessayer ")
            continue
        ligne = ord(entree[0]) - 65
        colonne = int(entree[1]) - 1
        if est_dans_grille(ligne, colonne, grille):
            return ligne, colonne
        else:
            print("Coordonnée hors grille.")

def saisir_coordonees_depart(grille, pion):
    """
    Permet à l'utilisateur de saisir les coordonnées de départ pour un déplacement.
    Retourne les coordonnées (ligne, colonne) si elles sont valides, sinon demande à l'utilisateur de réessayer.
    """
    while True:
        depart = input("Entrez la coordonnée du pion que vous voulez déplacer : ").upper()
        if not est_au_bon_format(depart):
            print("Le format que vous avez rentré est invalide, veuillez réessayer.")
            continue
        
        ligne = ord(depart[0]) - 65  # Conversion de la lettre en indice de ligne
        colonne = int(depart[1]) - 1  # Conversion en entier et ajustement pour l'index 0
        
        # Vérifier d'abord si les coordonnées sont dans la grille
        if not est_dans_grille(ligne, colonne, grille):
            print("Coordonnées hors de la grille. La grille va de A-I et 1-9.")
            continue
            
        # Ensuite vérifier si c'est bien un pion du joueur
        if grille[ligne][colonne] == pion:
            return ligne, colonne
        else:
            print("Ce n'est pas un de vos pions")

def est_case_vide(grille, l, c):
    """
    Vérifie si une case est vide.
    Retourne True si la case est vide, False sinon.
    """
    return est_dans_grille(l, c, grille) and grille[l][c] == " "

def est_case_adversaire(grille, l, c, pion):
    """
    Vérifie si une case contient un pion adverse.
    Retourne True si la case contient un pion adverse, False sinon.
    """
    return est_dans_grille(l, c, grille) and grille[l][c] != pion and grille[l][c] != " "

def direction_verticale(l1, c1, l2, c2):
    """
    Calcule la direction verticale entre deux coordonnées.
    Retourne un tuple (dl, dc) si la direction est valide, None sinon.
    """
    if c1 == c2 and l1 != l2:
        return (l2 - l1) // abs(l2 - l1), 0  # Résultat sera +1 ou -1
    return None

def direction_horizontale(l1, c1, l2, c2):
    """
    Calcule la direction horizontale entre deux coordonnées.
    Retourne un tuple (dl, dc) si la direction est valide, None sinon.
    """
    if l1 == l2 and c1 != c2:
        return 0, (c2 - c1) // abs(c2 - c1)  # Résultat sera +1 ou -1
    return None

def direction_diagonale(l1, c1, l2, c2):
    """
    Calcule la direction diagonale entre deux coordonnées.
    Retourne un tuple (dl, dc) si la direction est valide, None sinon.
    """
    dl = l2 - l1  # Différence de lignes
    dc = c2 - c1  # Différence de colonnes
    if dl != 0 and dc != 0 and dl * dl == dc * dc:
        return dl // abs(dl), dc // abs(dc)  # Résultat sera +1 ou -1
    return None

def obtenir_direction(l1, c1, l2, c2):
    """
    Détermine la direction entre deux coordonnées.
    Retourne un tuple (dl, dc) si la direction est valide (verticale, horizontale ou diagonale), None sinon.
    """
    direction = direction_verticale(l1, c1, l2, c2)
    if direction is not None:
        return direction
    direction = direction_horizontale(l1, c1, l2, c2)
    if direction is not None:
        return direction
    return direction_diagonale(l1, c1, l2, c2)

def chemin_vide(grille, l1, c1, l2, c2):
    """
    Vérifie si le chemin entre deux coordonnées est vide.
    Retourne True si le chemin est vide, False sinon.
    """
    direction = obtenir_direction(l1, c1, l2, c2)
    if direction is None:
        print(f"Pas de direction reconnue entre {l1},{c1} -> {l2},{c2}")
        return False
    dl, dc = direction
    l, c = l1 + dl, c1 + dc
    while (l, c) != (l2, c2):
        if not est_case_vide(grille, l, c):
            print(" Chemin bloqué à (",chr(65+l),", ",c+1,")")
            return False
        l += dl
        c += dc
    return True

def deplacement_retournement(grille, ld, cd, la, ca, pion):
    """  
    Effectue un déplacement de retournement d'un pion adverse.
    Le retournement est possible seulement si :
    - La case d'arrivée est vide
    - Il y a exactement un pion adverse entre départ et arrivée
    - La distance est de 2 cases dans une direction (verticale, horizontale ou diagonale)
    """

    direction = obtenir_direction(ld, cd, la, ca)
    if direction is None:
        return False
    if not ((abs(la - ld) == 2 and ca == cd) or (la == ld and abs(ca - cd) == 2) or (abs(la - ld) == 2 and abs(ca - cd) == 2)):
        return False
    dl, dc = direction
    l, c = ld + dl, cd + dc
    if not est_case_adversaire(grille, l, c, pion) or not est_case_vide(grille, la, ca):
        return False
    grille[l][c] = pion
    grille[ld][cd] = " "
    grille[la][ca] = pion
    return True

def coups_possibles(grille, l1, c1, pion):
    """
    Vérifie si des coups d'élimination ou de retournement sont possibles depuis une position donnée.
    Retourne un tuple (elimination_possible, retournement_possible).
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    elimination_possible = False
    retournement_possible = False

    for dl, dc in directions:
        l, c = l1 + dl, c1 + dc
        while est_dans_grille(l, c, grille):
            if grille[l][c] == pion:
                break
            if est_case_adversaire(grille, l, c, pion):
                elimination_possible = True
            if not est_case_vide(grille, l, c):
                retournement_possible = True
            l += dl
            c += dc

    return elimination_possible, retournement_possible

def aucun_coup_possible(grille, pion):
    """
    Vérifie si aucun coup (élimination, retournement ou libre) n'est possible pour un joueur.
    Retourne True si aucun coup n'est possible, sinon False.
    """
    for l in range(9):
        for c in range(9):
            if grille[l][c] != pion:
                continue
            elim, ret = coups_possibles(grille, l, c, pion)
            if elim or ret:
                return False
            # Vérifie les déplacements libres (1 case autour)
            for dl in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dl == 0 and dc == 0:
                        continue
                    nl, nc = l + dl, c + dc
                    if est_case_vide(grille, nl, nc):
                        return False
    return True

def deplacement_elimination(grille, l1, c1, l2, c2, pion):
    """
    Effectue un déplacement par élimination d'un pion adverse.
    Retourne True si le déplacement est réussi, False sinon.
    """
    if not est_case_adversaire(grille, l2, c2, pion):
        return False
    if max(abs(l2 - l1), abs(c2 - c1)) <= 1:
        return False  # Refuse les déplacements vers des cases voisines immédiates
    if not chemin_vide(grille, l1, c1, l2, c2):
        return False
    grille[l2][c2] = pion
    grille[l1][c1] = " "
    return True

def deplacement_libre(grille, l1, c1, l2, c2, pion):
    """
    Effectue un déplacement libre d'un pion uniquement si les autres types de coups sont impossibles.
    """
    elim_possible, ret_possible = coups_possibles(grille, l1, c1, pion)
    if elim_possible or ret_possible:
        print("Déplacement libre interdit : un coup d'élimination ou de retournement est possible.")
        return False

    if not est_case_vide(grille, l2, c2):
        return False
    if max(abs(l2 - l1), abs(c2 - c1)) > 1:
        return False  # Déplacement libre limité à une case
    grille[l2][c2] = pion
    grille[l1][c1] = " "
    return True


def verifier_fin_de_jeu(grille):
    """
    Vérifie si le jeu est terminé (un joueur a moins de 6 pions).
    Retourne True si le jeu est terminé, False sinon.
    """
    nbr_pion1, nbr_pion2 = nombre_de_pion(grille)
    if nbr_pion1 < 6:
        return 2
    if nbr_pion2 < 6:
        return 1


def tour_de_jeu(grille, pion):
    """
    Applique la logique qui permet de jouer
    """
    afficher_grille(grille)
    print("Tour du joueur 1->(X)" if pion == 'X' else "Tour du joueur 2->(O)")

    ligne_depart, colonne_depart = saisir_coordonees_depart(grille,pion)

    while True:
        type_deplacement = demander_type_deplacement()

        ligne_arrivee, colonne_arrivee = saisir_coordonnees_arrivee(grille)

        deplacement_reussi = effectuer_deplacement(
            grille, type_deplacement, pion,
            ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee
        )

        if not deplacement_reussi:
            print("Déplacement invalide selon les règles. Réessayez avec un autre type si besoin.")
            continue


        # Gérer les enchaînements de sauts pour le retournement
        if type_deplacement == 'r':
            gerer_enchainement_sauts(grille, pion)

        break  # Sortir de la boucle si déplacement réussi


def demander_type_deplacement():
    """
    Demande à l'utilisateur de choisir le type de déplacement.
    Retourne 'e' pour élimination, 'r' pour retournement, ou 'l' pour déplacement libre.
    """
    while True:
        type_deplacement = input("Entrez le type de déplacement ('e' pour élimination, 'r' pour retournement, 'l' pour libre) : ").lower()
        if type_deplacement in ['e', 'r', 'l']:
            return type_deplacement
        print("Type invalide. Entrez 'e', 'r' ou 'l'.")



def effectuer_deplacement(grille, type_deplacement, pion, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee):
    """
    Effectue un déplacement en fonction du type de déplacement choisi.
    Retourne True si le déplacement est réussi, False sinon.
    """
    if type_deplacement == 'e':
        return deplacement_elimination(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, pion)
    elif type_deplacement == 'l':
        return deplacement_libre(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, pion)
    elif type_deplacement == 'r':
         return deplacement_retournement(grille,ligne_depart,colonne_depart,ligne_arrivee,colonne_arrivee,pion)
    return False

def gerer_enchainement_sauts(grille, pion):
    """
    Gère l'enchaînement des sauts pour un déplacement de retournement.
    """
    encore = input("Voulez-vous continuer les sauts ? (o/n) : ").lower()
    while encore == 'o':
        afficher_grille(grille)
        deplacement_reussi = False
        while not deplacement_reussi:
            ligne_depart, colonne_depart = saisir_coordonees_depart(grille,pion)
            ligne_arrivee, colonne_arrivee = saisir_coordonnees_arrivee(grille)
            deplacement_reussi = deplacement_retournement(grille, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, pion)
            if not deplacement_reussi:
                print("Saut invalide. Veuillez réessayer.")
        encore = input("Continuer les sauts ? (o/n) : ").lower()
        if verifier_fin_de_jeu(grille):
            return

#### Jeu de test

def test_est_case_vide():
    """
    Teste la fonction est_case_vide avec plusieurs cas.
    """
    grille = initialiser_configuration_debut()
    assert est_case_vide(grille, 3, 3) == True
    assert est_case_vide(grille, 0, 0) == False
    assert est_case_vide(grille, 9, 9) == False  # hors grille


def test_est_case_adversaire():
    """
    Teste la fonction est_case_adversaire avec plusieurs cas.
    """
    grille = initialiser_configuration_debut()
    assert est_case_adversaire(grille, 0, 0, "O") == True   # case X, adversaire de O
    assert est_case_adversaire(grille, 0, 0, "X") == False  # case X, même camp
    assert est_case_adversaire(grille, 3, 3, "O") == False  # case vide
    assert est_case_adversaire(grille, 9, 9, "X") == False  # hors grille

def test_direction_verticale():
    """
    Teste la fonction direction_verticale avec plusieurs cas.
    """
    assert direction_verticale(2, 2, 5, 2) == (1, 0)
    assert direction_verticale(5, 4, 2, 4) == (-1, 0)
    assert direction_verticale(2, 3, 2, 5) == None

def test_direction_horizontale():
    """
    Teste la fonction est_direction_horizontale avec plusieurs cas.
    """
    assert direction_horizontale(4, 1, 4, 6) == (0, 1)
    assert direction_horizontale(7, 5, 7, 2) == (0, -1)
    assert direction_horizontale(3, 3, 6, 3) == None

def test_direction_diagonale():
    """
    Teste la fonction direction_horizontale avec plusieurs cas.
    """
    assert direction_diagonale(2, 2, 5, 5) == (1, 1)
    assert direction_diagonale(6, 6, 3, 3) == (-1, -1)
    assert direction_diagonale(1, 4, 4, 1) == (1, -1)
    assert direction_diagonale(0, 0, 0, 5) == None

def test_est_dans_grille(grille):
    """
    Teste la fonction est_dans_grille avec plusieurs cas.
    """
    assert est_dans_grille(0,0,grille) == True
    assert est_dans_grille(0,1,grille) == True
    assert est_dans_grille(9,99,grille) == False
    assert est_dans_grille(1,55,grille) == False
    assert est_dans_grille(2,2,grille) == True
    assert est_dans_grille(4,5,grille) == True
    assert est_dans_grille(0,0,grille) == True
    assert est_dans_grille(-2,-1,grille) == False


def test_est_au_bon_format():
    """
    Teste la fonction est_au_bon_format avec plusieurs cas.
    """
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
    """
    Teste la fonction chemin_vide avec plusieurs cas.
    """
    grille = initialiser_configuration_milieu()

    # Cas de chemins vides
    assert chemin_vide(grille, 3, 0, 3, 4) == True     # Ligne vide
    assert chemin_vide(grille, 5, 3, 2, 3) == True   
    assert chemin_vide(grille, 2, 3, 5, 6) == True    # diagonale, mais bloqué
    assert chemin_vide(grille, 5, 0, 2, 3) == True   
    assert chemin_vide(grille, 3, 3, 3, 6) == True     # Ligne horizontale vide

    # Cas de chemins non valides (hors direction alignée)
    assert chemin_vide(grille, 1, 1, 2, 4) == False


def test_deplacement_elimination():
    """
    Teste la fonction deplacement_elimination avec plusieurs cas.
    """
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

def test_obtenir_direction():
    """
    Teste la fonction obtenir_direction avec plusieurs cas.
    """
    # Test des directions verticales
    assert obtenir_direction(2, 3, 5, 3) == (1, 0)   # Vers le bas
    assert obtenir_direction(5, 3, 2, 3) == (-1, 0)  # Vers le haut
    
    # Test des directions horizontales
    assert obtenir_direction(3, 2, 3, 5) == (0, 1)   # Vers la droite
    assert obtenir_direction(3, 5, 3, 2) == (0, -1)  # Vers la gauche
    
    # Test des directions diagonales
    assert obtenir_direction(2, 2, 5, 5) == (1, 1)    # Diagonale bas-droite
    assert obtenir_direction(5, 5, 2, 2) == (-1, -1)  # Diagonale haut-gauche
    assert obtenir_direction(2, 5, 5, 2) == (1, -1)   # Diagonale bas-gauche
    assert obtenir_direction(5, 2, 2, 5) == (-1, 1)  # Diagonale haut-droite
    
    # Test des cas non valides
    assert obtenir_direction(1, 1, 2, 3) == None     # Pas aligné
    assert obtenir_direction(0, 0, 0, 0) == None     # Même case

def test_deplacement_retournement():
    """
    Teste la fonction deplacement_retournement avec plusieurs cas.
    """
    grille = initialiser_configuration_milieu()
    
    # Cas valide : retournement horizontal
    grille[3][3] = "X"
    grille[3][4] = "O"
    grille[3][5] = " "
    assert deplacement_retournement(grille, 3, 3, 3, 5, "X") == True
    assert grille[3][4] == "X"  # Le pion adverse a été retourné
    assert grille[3][3] == " "  # Case départ vide
    assert grille[3][5] == "X"  # Case arrivée occupée
    
    # Cas valide : retournement vertical
    grille[3][3] = "X"
    grille[4][3] = "O"
    grille[5][3] = " "
    assert deplacement_retournement(grille, 3, 3, 5, 3, "X") == True
    
    # Cas invalide : distance incorrecte
    grille[0][0] = "X"
    grille[0][3] = "O"
    assert deplacement_retournement(grille, 0, 0, 0, 3, "X") == False
    
    # Cas invalide : pas de pion adverse entre départ et arrivée
    grille[1][1] = "X"
    grille[1][2] = " "
    grille[1][3] = " "
    assert deplacement_retournement(grille, 1, 1, 1, 3, "X") == False

def test_coups_possibles():
    """
    Teste la fonction coups_possibles avec plusieurs cas.
    """
    grille = initialiser_configuration_milieu()
    
    # Cas avec possibilité d'élimination
    grille[0][0] = "X"
    grille[0][2] = "O"
    elim, ret = coups_possibles(grille, 0, 0, "X")
    assert elim == False
    assert ret == False
    
    # Cas avec possibilité de retournement
    grille[2][2] = "X"
    grille[2][3] = "O"
    grille[2][4] = " "
    elim, ret = coups_possibles(grille, 2, 2, "X")
    assert elim == True
    assert ret == True
    
    # Cas sans possibilité
    grille[8][8] = "X"
    elim, ret = coups_possibles(grille, 8, 8, "X")
    assert elim == True
    assert ret == True

def test_aucun_coup_possible():
    """
    Teste la fonction aucun_coup_possible avec plusieurs cas.
    """
    grille = initialiser_configuration_milieu()
    
    # Cas où des coups sont possibles    
    # Cas où aucun coup n'est possible
    grille = [[" " for _ in range(9)] for _ in range(9)]
    grille[0][0] = "X"
    assert aucun_coup_possible(grille, "X") == False
    
    # Cas avec seulement des déplacements libres possibles
    grille = [[" " for _ in range(9)] for _ in range(9)]
    grille[4][4] = "X"
    assert aucun_coup_possible(grille, "X") == False

def test_deplacement_libre():
    """
    Teste la fonction deplacement_libre avec plusieurs cas.
    """
    grille = initialiser_configuration_milieu()
    
    # Cas valide quand aucun autre coup possible
    grille[8][8] = "X"
    grille[7][7] = " "
    assert deplacement_libre(grille, 8, 8, 7, 7, "X") == True
    
    # Cas invalide : autre coup possible
    grille[0][0] = "X"
    grille[0][1] = "O"
    assert deplacement_libre(grille, 0, 0, 1, 0, "X") == False
    
    # Cas invalide : distance trop grande
    grille[1][1] = "X"
    assert deplacement_libre(grille, 1, 1, 3, 3, "X") == False
    
    # Cas invalide : case non vide
    grille[2][2] = "X"
    grille[2][3] = "O"
    assert deplacement_libre(grille, 2, 2, 2, 3, "X") == False

### Code principal  

def main():

    #Execution affichage sur les 3 grilles ainsi que test 
    #print("Configuration de début :")
    #afficher_grille(initialiser_configuration_debut())
    test_est_dans_grille(initialiser_configuration_debut())
    test_est_au_bon_format()
    #print("\n")
    #print("Configuration de milieu :")
    #afficher_grille(initialiser_configuration_milieu())
    test_est_dans_grille(initialiser_configuration_milieu())
    test_est_au_bon_format()
    #print("\n")
    #print("Configuration de fin :")
    #afficher_grille(initialiser_configuration_fin())
    test_est_dans_grille(initialiser_configuration_fin())
    test_est_au_bon_format()
    test_deplacement_elimination()
    test_chemin_vide()
    test_est_au_bon_format()
    test_est_dans_grille(initialiser_configuration_debut())
    test_direction_diagonale()
    test_direction_horizontale()
    test_direction_verticale()
    test_est_case_adversaire()
    test_est_case_vide()
    test_aucun_coup_possible()
    test_obtenir_direction()
    test_coups_possibles()



    #Déplacement dans la grille(Les règles du jeu ne sont pas appliqué comme décrit dans l'atelier)
    print("\n");
    print("Bienvenue dans le jeu !")

    grille = initialiser_configuration_fin()  # Vous pouvez modifier cette partie pour choisir la grille que vous voulez tester
    tour = randint(1,2)  # 1 pour Joueur 1 (X), 2 pour Joueur 2 (O)
    print("Le joueur 1 joue avec les pions X et le joueur 2 joue avec les pions O")
    

    while True:
        pion = "X" if tour == 1 else "O"

        if aucun_coup_possible(grille, pion):
            print("Aucun coup possible pour le joueur",tour,"Il passe son tour.")
            tour = 3 - tour
            continue

        tour_de_jeu(grille, pion)
        
        # Vérifier fin de jeu
        resultat = verifier_fin_de_jeu(grille)
        if resultat == 1:
            afficher_grille(grille)
            print("Le joueur 1 (X) a gagné !")
            break
        elif resultat == 2:
            afficher_grille(grille)
            print("Le joueur 2 (O) a gagné !")
            break
            
        tour = 3 - tour  # alterner joueur
    

if __name__ == "__main__":
    main()


