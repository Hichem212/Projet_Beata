# Beata - Jeu de Plateau Stratégique

Beata est un jeu de stratégie opposant deux joueurs sur un plateau de 9x9 cases. Ce projet est une implémentation en Python réalisée dans le cadre du module **Info/Projet-S2-2024/2025**.

## 📝 Présentation du jeu

Le but du jeu est de réduire le nombre de pions de l'adversaire à **moins de 6**. Chaque joueur commence la partie avec 27 pions, pour un total de 54 pions sur le plateau.

### Matériel & Configuration
* **Plateau** : Grille de 9x9 cases.
* **Pions** : 54 pions réversibles. Dans le code, ils sont représentés par `X` (Joueur 1) et `O` (Joueur 2).
* **Configuration initiale** : Les pions sont disposés sur les trois premières et trois dernières lignes du plateau.

## 🕹️ Règles de déplacement

Les déplacements s'effectuent dans les **8 directions** : horizontalement, verticalement et en diagonale. Trois types d'actions sont possibles :

1. **Prise par élimination** : Un pion se déplace sur une case occupée par un adversaire pour l'éliminer. Il doit y avoir au moins une case vide entre le départ et l'arrivée, et aucune autre pièce ne doit obstruer le chemin. Les pions voisins immédiats ne peuvent pas être éliminés de cette façon.
2. **Prise par retournement (Saut)** : Un pion saute par-dessus un pion adverse vers une case vide située immédiatement derrière. Le pion sauté change alors de camp et prend la couleur du joueur courant. Il est possible d'enchaîner plusieurs sauts en un seul tour.
3. **Déplacement libre** : Si aucune prise (élimination ou retournement) n'est possible pour les deux joueurs, un joueur peut effectuer un déplacement "libre" d'une seule case vers une arrivée vide.

## 🚀 Installation et Utilisation

### Prérequis
* Python 3.x

### Lancement du jeu
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre_pseudo/Projet_Beata.git
2.Accédez au fichier : 
   '''bash
      cd Projet_Beata

3.Lancez le script principal : 
   '''bash
      python atelier2.py
   
