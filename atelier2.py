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

#Fonction qui permet de choisir la destination ou l'on veut placer le pion(On ne tient pas encore en compte les règles du jeu comme indiqué sur le sujet)
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


### Jeu de test

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

        if tour == 1:
            print("C'est au joueur 1 de jouer")
            pion = "X"
           
        else:
            print("C'est au joueur 2 de jouer")
            pion = "O"
        
        l,c = saisir_coordonees_depart(grille) # l et c représente la ligne et la colonne
        
        #On vérifie que l'on choisit le bon pion
        if grille[l][c] != pion:
            print("Vous ne pouvez pas déplacer les pions de l'adversaire")
            continue
        
        ligne,colonne = saisir_coordonnees_arrivee(grille)
        
        #Déplacement du pion
        grille[l][c] = " "
        grille[ligne][colonne] = pion

        
        tour = 3-tour

        



if __name__ == "__main__":
    main()


