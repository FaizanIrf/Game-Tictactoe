# Créé par Faizan Muhammad, le 13/10/2025 en Python 3.7
# PROJET TICTACTOE TERMINALE NSI AIDE

""" Joueur """
class Joueur:
    def __init__(self, nom, symbole):
        self.nom = nom
        self.symbole = symbole

    def __str__(self):
        return f"{self.nom} ({self.symbole})"

""" Case """
class Case:

    def __init__(self, position):
        self.position = position
        self.valeur = None

    def __str__(self):
        return str(self.position) if self.valeur is None else self.valeur

""" Grille """
class Grille:
    def __init__(self):
        self.cases = [Case(i) for i in range(9)]

    def verif_case(self, position):
        return self.cases[position].valeur is None

    def joue(self, position, symbole):
        if self.verif_case(position):
            self.cases[position].valeur = symbole
            return True
        return False

    def verif_victoire(self):
        combinaisons = [
            # Lignes horizontales
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            # Lignes verticales
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            # Diagonales
            [0, 4, 8], [2, 4, 6]
        ]

        for comb in combinaisons:
            valeurs = [self.cases[i].valeur for i in comb]
            if valeurs[0] is not None and all(v == valeurs[0] for v in valeurs):
                return valeurs[0]
        return None

    def est_pleine(self):
        return all(not self.verif_case(i) for i in range(9))

    def __str__(self):
        lignes = []
        for i in range(0, 9, 3):
            ligne = " | ".join(str(self.cases[j]) for j in range(i, i+3))
            lignes.append(f"| {ligne} |")
        return "\n".join(lignes)

""" Jeu """
class Jeu:
    def __init__(self, joueur1, joueur2):
        # Le constructeur de Jeu.
        self.joueurs = [joueur1, joueur2]
        self.grille = Grille()
        self.joueur_actuel_index = 0
        self.coups_joues = 0

    def joueur_actuel(self):
        return self.joueurs[self.joueur_actuel_index]

    def joueur_suivant(self):
        self.joueur_actuel_index = 1 - self.joueur_actuel_index

    def tour(self):
        print("\nGrille actuelle :")
        print(self.grille)
        joueur = self.joueur_actuel()
        print(f"\nTour de {joueur.nom} ({joueur.symbole})")

        # Boucle tant que la case choisie n'est pas vide
        while True:
            try:
                choix = int(input("Choisissez une case (0-8) : "))
                if 0 <= choix <= 8:
                    if self.grille.verif_case(choix):
                        self.grille.joue(choix, joueur.symbole)
                        self.coups_joues += 1
                        break
                    else:
                        print("Case déjà occupée !")
                else:
                    print("Veuillez choisir un nombre entre 0 et 8.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def jeu_entier(self):
        # Permet de gérer le jeu en entier :
        print("=== DEBUT DE LA PARTIE ===")
        print(f"Joueur 1: {self.joueurs[0]}")
        print(f"Joueur 2: {self.joueurs[1]}")
        while True:
            self.tour()


            gagnant = self.grille.verif_victoire()
            if gagnant:
                print("\n" + "="*30)
                print(self.grille)
                print(f"🎉 FÉLICITATIONS ! {gagnant} a gagné la partie !")
                print("="*30)
                break
            elif self.grille.est_pleine():
                print("\n" + "="*30)
                print(self.grille)
                print("🤝 MATCH NUL ! La grille est pleine.")
                print("="*30)
                break

            # Si non, change de joueur
            self.joueur_suivant()

# Code pour tester le jeu
if __name__ == "__main__":
    # Création des joueurs
    joueur1 = Joueur("Alice", "X")
    joueur2 = Joueur("Bob", "O")

    # Création et démarrage du jeu
    jeu = Jeu(joueur1, joueur2)
    jeu.jeu_entier()