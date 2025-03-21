# -*- coding: utf-8 -*-


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


#### Representation graphique

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
        if j< len(grille[i])-1:
            print("|",end="")
    print()

#Fonction auxiliaire qui permet d'afficher les séparateurs
def afficher_separateur(grille):
    print("  ", end="")
    for j in range(len(grille[0])):
        print("------", end="")
    print()  


#Fonction qui permet d'afficher la grille complète
def afficher_grille(grille):

    afficher_indice_colonne(grille) #Affichage de l'indice des colonnes

    for i in range(len(grille)):
        afficher_ligne(grille,i) #Affichage des lignes
        if i < len(grille) -1:
            afficher_separateur(grille) #Affichage des séparations entre les lignes


#Fonction qui permet de savoir si un pion est dans la grille
def est_dans_grille(ligne, colonne, grille):
    return 0 <= ligne < len(grille) and 0 <= colonne < len(grille)


#Fonction qui permet de savoir si la valeur de case entrée est au bon format
def est_au_bon_format(message):
    if len(message) != 2:
        return False
    
    if not ('A' <= message[0] <= 'Z'):
        return False

    if not ('1' <= message[1] <= '9'):
        return False

    return True

def saisir_coordonnees(grille):

    while True:

        entree = input("Entrez une coordonée : ").upper() #On utilise .upper pour mettre la lettre en majuscule 

        if not est_au_bon_format(entree):
            print("Le format que vous avez rentré est invalide veuillez réesayer")
            continue
    
        ligne = ord(entree[0])-65 #Pour avoir la valeur de la ligne en lettre
        colonne = entree[1]

        if est_dans_grille(ligne, colonne, grille) and grille[ligne][colonne] == " ":
            return ligne, colonne
    

### Jeu de test
def test_est_dans_grille(grille):
    assert est_dans_grille(0,0,grille) == True
    assert est_dans_grille(0,1,grille) == False

def test_est_au_bon_format():
    assert est_au_bon_format("A2") == True
    assert est_au_bon_format("A22") == False
    assert est_au_bon_format("a2") == True
    assert est_au_bon_format("a55") == False
    assert est_au_bon_format("AA") == False
    assert est_au_bon_format("11") == False
    assert est_au_bon_format("1a") == False
    assert est_au_bon_format("a1") == True





def main():
    print("Configuration de début :")
    afficher_grille(initialiser_configuration_debut())


if __name__ == "__main__":
    main()


