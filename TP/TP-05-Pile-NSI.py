# une implémentation du type Pile en python avec la POO
class Pile:
    """Classe modélisant le Type Pile a l'aide de la POO """ 

    def __init__(self):
        """Fonction constructeur """
        self.__pile = [] # __ donc attibut privé 

    def creer_pile_vide():
        return []

    def est_vide(self):
        """Renvoie TRUE si la Pile est vide """
        return p == []

    def empiler(self,p,x):
        """Empile l'élément x au sommet de la Pile """
        p.append(x)

    def depiler(self,p):
        assert( not est_vide(p))
        return p.pop()

    def afficher_pile_0(self):
        print("^")
        for k in range(1):
            print("finir plus tard")