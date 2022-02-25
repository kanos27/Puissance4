
# Auteur : Arthur Romary
# Tentative de creation d'un puissance 4
# Pas d'affichage visuel, que sur terminal.
# but du jeu : deux joueur doivent poser des jetons tours à tours
# le premier qui fait un alignement (horizontal, vertical, diagonal) de quatre de ses jetons gagne
# taille du quadrillage / grille : 7*6 (L*H)
# version 2 : retravaillage du code pour être plus adapté à la POO

class Grid:

    def __init__(self):
        #constante d'état pour case vide, pour faciliter la vie en cas de changement de nbr pour vide et joueur
        self._CASE_VIDE = 0

        self.grid = [[self._CASE_VIDE for i in range(6)] for j in range(7)]
        pass

    def __str__(self):
        etat = ""
        for i in range(len(self.grid[0])):
            etat += "\n"
            for j in range(len(self.grid)): #pas parfait ; à ameliorer ?
                etat += str( self.grid[j][i] )
        return etat


    def getGrid(self): #nécéssaire ?
        return self.grid

    '''
    boolean qui retourne vrai si le jeton donné amene la victoire 
    param : positionPion -> la colonne ou le pion à été posé (au dessus)
    '''
    def estGagne(self, positionPion):
        #idee un peu degueu:
        #verif de ligne de chaque coté, avec conteur du nombre de case correct,
        #puis de colonnes, meme process,
        #et same pour diagonales (2)


        #code actuel : un peu une horreur, à refaire ?

        case = len(self.grid[positionPion]) -1
        while case >= 0 and self.grid[positionPion][case] != self.player :
            case -=1
            
        if self.grid[positionPion][case] != self.player:
            print("DEBUG  estGagne: pas de pion du joueur en cours trouvé")
            return False
        
        #verif colonne (visuellement; en calcul, verif ligne)
        val_longueur = 1
        eloignement = 1
        while (case - eloignement >= 0 ) and self.grid[positionPion][case - eloignement] == self.player:
            eloignement += 1
            val_longueur += 1

        eloignement = 1
        while ( eloignement < len(self.grid[positionPion])-case ) and self.grid[positionPion][case + eloignement] == self.player:
            eloignement += 1
            val_longueur += 1

        if val_longueur >= 4:
            print("DEBUG estGagne : colonne (en code ligne) gagnante")
            return True

        #verif ligne (visuellement; en calcul, verif colonne)
        val_longueur = 1
        eloignement = 1
        while ( positionPion - eloignement >= 0  ) and self.grid[positionPion - eloignement ][case] == self.player:
            eloignement += 1
            val_longueur += 1

        eloignement = 1
        while ( eloignement < len(self.grid) - positionPion ) and self.grid[positionPion + eloignement][case] == self.player:
            eloignement += 1
            val_longueur += 1

        if val_longueur >= 4:
            print("DEBUG estGagne : ligne (en code colonne) gagnante")
            return True


        #verif diagonales
        #diag 1
        val_longueur = 1
        eloignement = 1
        while ( case - eloignement >= 0 and positionPion - eloignement >= 0 ) and self.grid[positionPion - eloignement ][case - eloignement] == self.player:
            eloignement += 1
            val_longueur += 1

        eloignement = 1
        while ( eloignement < len(self.grid[positionPion]) - case and  eloignement < len(self.grid) - positionPion) and self.grid[positionPion + eloignement][case + eloignement] == self.player:
            eloignement += 1
            val_longueur += 1

        if val_longueur >= 4:
            print("DEBUG estGagne : Diagonale 1 gagnante")
            return True

        #diag 2
        val_longueur = 1
        eloignement = 1
        while ( eloignement < len(self.grid[positionPion]) - case and positionPion - eloignement >= 0 ) and self.grid[positionPion - eloignement ][case + eloignement] == self.player:
            eloignement += 1
            val_longueur += 1

        eloignement = 1
        while ( case - eloignement >= 0 and eloignement < len(self.grid) - positionPion) and self.grid[positionPion + eloignement][case - eloignement] == self.player:
            eloignement += 1
            val_longueur += 1

        if val_longueur >= 4:
            print("DEBUG estGagne : Diagonale 2 gagnante")
            return True

        return False

    def comparerGrid(self, other: Grid): # grid ne passe pas ?
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != other.grid[i][j]: # pas la meilleure méthode, car return dans for. Serait mieux avec while je crois.
                    return False
        
        return True

    '''
    Crée et retourne un nouveau terrain avec le pion placé à la position adapatée dans la grille, pour une colonne donnee. Ne vérifie pas que le pion est placable
    param positionPion = la colonne ou le pion doit être placé
    return 
    '''
    def JouerPion(self, positionPion, player):
        newGrid = self
        is_placed = False
        colonne = newGrid.grid[positionPion]
        case = len(colonne) - 1
        while not is_placed:
            if colonne[case] == newGrid._CASE_VIDE:
                newGrid.grid[positionPion][case] = player
                is_placed = True
            else :
                case-=1

        return newGrid


    '''
    boolean qui retourne vrai si le terrain est entierement remplis
    '''
    def estRemplis(self):
        remplis = True
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == self._CASE_VIDE:
                    remplis = False
        return remplis
    



class Player():

    def __init__(self, value): # est-ce correct ?
        # boolean is_ia ?
        self.value = value

        pass

    def __str__(self):
        return self.value
        
    '''
    Fait jouer le joueur : prend le terrain actuel du jeu et retourne la position de la colonne que le joueur à choisit (dépend du type de joueur)
    '''
    def playTurn(self, Grid):
        #prend un terrain en attribut, et ressort une valeur, le move qu'il souhaite jouer
        #pour cela, en fonction du tape de joueur demande a l'humain, ou a l'ia
        move = 0

        return move


class Jeu:
    '''
    initie la classe jeu avec un tour de joueur et une grille format 7x6

    probleme actuel : grille en format ligne-colonne et non colonne-ligne
    '''
    def __init__(self):

        self.curr_grid = Grid()
        pass

    '''
    retourne un string montrant l'etat du jeu, avec une indication du joueur et de l'etat de la grille
    '''
    def __str__(self) :
        etat = ""
        etat += "joueur : " + str(self.player) + "\n" + "grille :"
        #etat += str(Grid)
        return etat


    def boucleJeu(self):
        #input du joueur
        #verification de l'input et redemande jusqu'à bon
        #place pion
        #verifie si gagnant
        #si gagnant, jeu s'arrete, joueur en cours déclaré vainqueur
        #sinon, verification que terrain n'est pas remplis
        #puis changement de joueur, et on recommence

        est_gagne = False
        while not self.estRemplis() and not est_gagne:
            #a ameliorer : partie affichage dediée
            print(self)
            choixJoueur = self.inputJoueur()
            print("DEBUG boucleJeu : inputJoueur() passé")
            while not self.estPlacable(choixJoueur):
                
                #a ameliorer : partie affichage dediée
                print("le pion n'est pas placable à cet endroit, veuillez réessayer.")
                choixJoueur = self.inputJoueur()
            
            self.placerPion(choixJoueur)
            est_gagne = self.estGagne(choixJoueur)

            if not est_gagne and not self.estRemplis():
                self.jSuivant()
        
        print("partie finie !")
        if self.estRemplis():
            print("Le terrain est entièrement remplis, il y a donc égalité.")
        else :
            print(f"le gagnant est joueur {self.player}, félicitation !")

        ...


    '''
    Indique si une position donnée est correcct ou non, aka si un pion est placable
    param : positionPion -> la position donnée de placement de pion
    return : boolean -> si la position est correcte ou non
    '''
    def estPlacable(self, positionPion):
        is_placable = False
        case = len(self.grid[positionPion]) -1
        while not is_placable and case >= 0:
            #print("DEBUG  estPlacable: val case : " + str(case))
            #print("DEBUG  estPlacable: self.grid[positionPion][case] : " + str(self.grid[positionPion][case]))
            if self.grid[positionPion][case] == self._CASE_VIDE:
                #print("DEBUG  estPlacable: est dans if" )
                is_placable = True
            case -= 1
        
        return is_placable


    '''
    change le joueur en cours
    '''
    def jSuivant(self):
        if self.player == 1:
            self.player = 2
        else: 
            self.player = 1


    '''
    boolean qui retourne vrai si le terrain est entierement remplis
    '''
    def estRemplis(self):
        remplis = True
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == self._CASE_VIDE:
                    remplis = False
        return remplis

    '''
    se charge de l'input des joueur, retourne la colonne selectionnée
    return : positionChoix : int de la colonne choisie
    '''
    def inputJoueur(self):
        #on commence à -1 pour l'effectuer au moins une fois
        positionChoix = -1
        while (positionChoix < 0 or positionChoix > len(self.grid) -1):
            #a ameliorer : partie affichage dediée
            positionChoix = int(input(f"Joueur {self.player}, sur quelle colonne souhaitez-vous placer votre pion ? /n>"))
        return positionChoix
        ...
    





if __name__ == "__main__":
    jeu = Jeu()
    print(jeu)
    print(jeu.estPlacable(3))
    jeu.placerPion(3)  
    print(jeu)
    #jeu.grid[1][2] = 1
    #print(jeu)

    jeu.placerPion(2)
    print(jeu)
    jeu.placerPion(1)
    print(jeu)
    jeu.placerPion(4)
    print(jeu)
    print(jeu.estGagne(4))

    print("DEBUG MAIN : TEST : verification des cas de gagne :")
    jeu2 = Jeu()
    jeu2.grid[1][5] = 1
    jeu2.grid[2][4] = 1
    jeu2.grid[3][3] = 1
    jeu2.grid[4][2] = 1
    print(jeu2)
    print(jeu2.estGagne(1))

    print("DEBUG MAIN : FIN TESTS : verifications de cas gagne")
    print("DEBUG MAIN : DEBUT TEST : partie complete :")
    jeu3 = Jeu()
    #print(jeu3.estRemplis())
    jeu3.boucleJeu()
