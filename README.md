# Beata - Jeu de Plateau Stratégique

[cite_start]Beata est un jeu de stratégie opposant deux joueurs sur un plateau de 9x9 cases[cite: 5]. [cite_start]Ce projet est une implémentation en Python réalisée dans le cadre du module **Info/Projet-S2-2024/2025**[cite: 2].

## 📝 Présentation du jeu

[cite_start]Le but du jeu est de réduire le nombre de pions de l'adversaire à **moins de 6**[cite: 3, 118]. [cite_start]Chaque joueur commence la partie avec 27 pions, pour un total de 54 pions sur le plateau[cite: 6].

### Matériel & Configuration
* [cite_start]**Plateau** : Grille de 9x9 cases[cite: 5].
* [cite_start]**Pions** : 54 pions réversibles[cite: 6]. Dans le code, ils sont représentés par `X` (Joueur 1) et `O` (Joueur 2).
* [cite_start]**Configuration initiale** : Les pions sont disposés sur les trois premières et trois dernières lignes du plateau[cite: 7, 27].

## 🕹️ Règles de déplacement

[cite_start]Les déplacements s'effectuent dans les **8 directions** : horizontalement, verticalement et en diagonale[cite: 44]. Trois types d'actions sont possibles :

1. [cite_start]**Prise par élimination** : Un pion se déplace sur une case occupée par un adversaire pour l'éliminer[cite: 46]. [cite_start]Il doit y avoir au moins une case vide entre le départ et l'arrivée, et aucune autre pièce ne doit obstruer le chemin[cite: 48, 49]. [cite_start]Les pions voisins immédiats ne peuvent pas être éliminés de cette façon[cite: 53].
2. [cite_start]**Prise par retournement (Saut)** : Un pion saute par-dessus un pion adverse vers une case vide située immédiatement derrière[cite: 54, 58]. [cite_start]Le pion sauté change alors de camp[cite: 60]. [cite_start]Il est possible d'enchaîner plusieurs sauts en un seul tour[cite: 61].
3. [cite_start]**Déplacement libre** : Si aucune prise (élimination ou retournement) n'est possible, un joueur peut effectuer un déplacement "libre" d'une seule case vers une arrivée vide[cite: 113, 115].

## 🚀 Installation et Utilisation

### Prérequis
* Python 3.x

### Lancement du jeu
1. Clonez le dépôt :
   ```bash
   git clone [https://github.com/votre-pseudo/Projet_Beata.git](https://github.com/votre-pseudo/Projet_Beata.git)
