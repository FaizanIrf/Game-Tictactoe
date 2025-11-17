# Créé par Faizan Muhammad, le 17/11/2025 en Python 3.7
class NoeudBinaire:
    def __init__(self, valeur, fils_gauche, fils_droite):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droite = fils_droite

    def taille(self):
        compteur = 1

        if self.fils_gauche != None:
            compteur += self.fils_gauche.taille()

        if self.fils_droite != None:
            compteur += self.fils_droite.taille()

        return compteur


    def hauteur(self):
        hauteur_sag = 0
        hauteur_sad = 0

        if self.fils_gauche != None:
            hauteur_sag = self.fils_gauche.hauteur()

        if self.fils_droite != None:
            hauteur_sad = self.fils_droite.hauteur()

        return  1 + max(hauteur_sag, hauteur_sad)

    def est_feuille(self):
        return self.fils_gauche == None and self.fils_droite == None


    def nombre_feuilles(self):
        if self.est_feuille():
            return 1
        else:
            nombre_feuilles = 0
            if self.fils_gauche != None:
                nombre_feuilles += self.fils_gauche.nombre_feuilles()
            if self.fils_droite != None:
                nombre_feuilles += self.fils_droite.nombre_feuilles()
            return nombre_feuille

    def parcours_prefixe(self):
        print(self.valeur)
        if self.fils_gauche != None:
            self.fils_gauche.parcours_prefixe()
            if self.fils_droite != None:
                self.fils_droite.parcours_prefixe()

    def parcours_suffixe(self):
        if self.fils_gauche != None:
            self.fils_gauche.parcours_suffixe()
            if self.fils_droite != None:
                self.fils_droite.parcours_suffixe()
            print(self.valeur)

    def parcours_infixe(self):
        if self.fils_gauche != None:
            self.fils_gauche.parcours_infixe()
        print(self.valeur)
        if self.fils_droite != None:
            self.fils_droite.parcours_infixe()

    def parcours_largeur(self):
        f = File()
        f.ajouterFile(self)
        while not f.estvide():
            noeud = f.retirerFile()
            print(noeud.valeur)
            if noeud.fils_gauche != None:
                f.ajouterFile(noeud.fils_gauche)
            if noeud.fils_droite != None:
                f.ajouterFile(noeud.fils_droite)

class NBR(NoeudBinaire):

    def __init__(self,valeur):
        self.valeur = valeur
        self.fils_gauche = None
        self.fils_droite = None


    def inserer(self,x):
        if x < self.valeur:
            if self.fils_gauche!= None:
                self.fils_gauche.inserer(x)
            else:
                noeud = NBR(x)
                self.fils_gauche = noeud
        else:
            if self.fils_droite != None:
                self.fils_droite.inserer(x)
            else:
                noeud = NBR(x)
                self.fils_droite = noeud


    def contient(self,x):
        if self.valeur == x:
            return True
        elif x < self.valeur and self.fils_gauche != None:
            return self.fils_gauche.contient(x)
        elif x >= self.valeur and self.fils_droite != None:
            return self.fils_droite.contient(x)
        else:
            return False






    def trace_recherche(self,x):
        print(self.valeur)
        if self.valeur ==x:
            print("Trouve !")
        elif x < self.valeur and self.fils_gauche != None:
            print("Gauche")
            self.fils_gauche.contient(x)
        elif x >= self.valeur and self.fils_droite != None:
            print("Droite")
            self.fils_droite.contient(x)
        else:
            print("introuvable")


    def valeur_minimale(self):
        if self.fils_gauche != None:
            return self.fils_gauche.valeur_minimale()
        else:
            return self.valeur


    def valeur_maximale(self):
        if self.fils_droite != None:
            return self.fils_droite.valeur_maximale()
        else:
            return self.valeur












E = NoeudBinaire("E", None, None)
D = NoeudBinaire("D", None, None)
I = NoeudBinaire("I", None, None)
J = NoeudBinaire("J", None, None)
C = NoeudBinaire("C", None,E)
B = NoeudBinaire("B", C, D)
G = NoeudBinaire("G", I, None)
H = NoeudBinaire("H",  None,J)
F = NoeudBinaire("F", G, H)
A = NoeudBinaire("A", B, F)
arbre_binaire = A

print(A.taille())
print(arbre_binaire.nombre_feuilles())



