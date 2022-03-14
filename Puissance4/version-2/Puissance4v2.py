
# Auteur : Arthur Romary
# Tentative de creation d'un puissance 4
# Pas d'affichage visuel, que sur terminal.
# but du jeu : deux joueur doivent poser des jetons tours à tours
# le premier qui fait un alignement (horizontal, vertical, diagonal) de quatre de ses jetons gagne
# taille du quadrillage / grille : 7*6 (L*H)
# version 2 : retravaillage du code pour être plus adapté à la POO

class Grid:
    """
    Classe representant la grille de jeu, et les jetons qui s'y situent

    Parameters
    ----------
    grid: 2d int array
        tableau de case du jeu, composé de valeures entieres
    _CASE_VIDE : int const
        constante de case vide, permettant d'y attribuer une valeur

    Attributes
    ----------

    A faire, pas sur de quoi mettre.

    """
    def __init__(self) -> None:
        #constante d'état pour case vide, pour faciliter la vie en cas de changement de nbr pour vide et joueur
        self._CASE_VIDE = 0

        self.grid = [[self._CASE_VIDE for i in range(6)] for j in range(7)]
        pass

    def __str__(self) -> str:
        etat = ""
        for i in range(len(self.grid[0])):
            etat += "\n"
            for j in range(len(self.grid)): #pas parfait ; à ameliorer ?
                etat += str( self.grid[j][i] )
        return etat


    def getGrid(self) -> 'Grid': #nécéssaire ?
        return self.grid

    '''
    boolean qui retourne vrai si le jeton donné amene la victoire 
    param : positionPion -> la colonne ou le pion à été posé (au dessus)
    '''
    def estPionGagnant(self, positionPion) -> bool:
        #idee un peu degueu:
        #verif de ligne de chaque coté, avec conteur du nombre de case correct,
        #puis de colonnes, meme process,
        #et same pour diagonales (2)


        #code actuel : un peu une horreur, à refaire ?

        case = 0
        while case < len(self.grid[positionPion]) and self.grid[positionPion][case] == self._CASE_VIDE :
            case +=1
            
        if self.grid[positionPion][case] == self._CASE_VIDE:
            print("DEBUG estPionGagnant: pas de pion du joueur en cours trouvé")
            return False
        else:
            player = self.grid[positionPion][case]
        
        #Debug
        print(f"DEBUG estPionGagnant: pion vérifié en case ({positionPion}, {case}) appartenant au joueur {player}")


        #verif colonne (visuellement; en calcul, verif ligne)
        val_longueur = 1
        eloignement = 1
        while (case - eloignement >= 0 ) and self.grid[positionPion][case - eloignement] == player:

            #Debug
            print(f"DEBUG estPionGagnant: pion vérifié (colone-ligne, partie 1) en case ({positionPion}, {case - eloignement}) appartenant au joueur {player}")

            eloignement += 1
            val_longueur += 1

        eloignement = 1
        while ( eloignement < len(self.grid[positionPion])-case ) and self.grid[positionPion][case + eloignement] == player:

            #Debug
            print(f"DEBUG estPionGagnant: pion vérifié (colone-ligne, partie 2) en case ({positionPion}, {case + eloignement}) appartenant au joueur {player}")

            eloignement += 1
            val_longueur += 1

        if val_longueur >= 4:
            print("DEBUG estPionGagnant : colonne (en code ligne) gagnante")
            return True

        #verif ligne (visuellement; en calcul, verif colonne)
        val_longueur = 1
        eloignement = 1
        while ( positionPion - eloignement >= 0  ) and self.grid[positionPion - eloignement ][case] == player:
            
            #Debug
            print(f"DEBUG estPionGagnant: pion vérifié (colone-ligne, partie 3) en case ({positionPion - eloignement}, {case}) appartenant au joueur {player}")
            
            eloignement += 1
            val_longueur += 1

        eloignement = 1
        while ( eloignement < len(self.grid) - positionPion ) and self.grid[positionPion + eloignement][case] == player:

            #Debug
            print(f"DEBUG estPionGagnant: pion vérifié (colone-ligne, partie 4) en case ({positionPion + eloignement}, {case}) appartenant au joueur {player}")


            eloignement += 1
            val_longueur += 1

        if val_longueur >= 4:
            print("DEBUG estPionGagnant : ligne (en code colonne) gagnante")
            return True


        #verif diagonales
        #diag 1
        val_longueur = 1
        eloignement = 1
        while ( case - eloignement >= 0 and positionPion - eloignement >= 0 ) and self.grid[positionPion - eloignement ][case - eloignement] == player:
            eloignement += 1
            val_longueur += 1

        eloignement = 1
        while ( eloignement < len(self.grid[positionPion]) - case and  eloignement < len(self.grid) - positionPion) and self.grid[positionPion + eloignement][case + eloignement] == player:
            eloignement += 1
            val_longueur += 1

        if val_longueur >= 4:
            print("DEBUG estPionGagnant : Diagonale 1 gagnante")
            return True

        #diag 2
        val_longueur = 1
        eloignement = 1
        while ( eloignement < len(self.grid[positionPion]) - case and positionPion - eloignement >= 0 ) and self.grid[positionPion - eloignement ][case + eloignement] == player:
            eloignement += 1
            val_longueur += 1

        eloignement = 1
        while ( case - eloignement >= 0 and eloignement < len(self.grid) - positionPion) and self.grid[positionPion + eloignement][case - eloignement] == player:
            eloignement += 1
            val_longueur += 1

        if val_longueur >= 4:
            print("DEBUG estPionGagnant : Diagonale 2 gagnante")
            return True

        return False

    def estGridGagnant(self) -> bool:
        est_gagne = False
        for i in range(len(self.grid)):
            if self.estPionGagnant(i): # verifie tous les derniers pions de colonnes
                est_gagne = True

        return est_gagne

    def comparerGrid(self, other: 'Grid') -> bool: # grid ne passe pas ?
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
    def placerPion(self, positionPion: int, player: 'Player') -> 'Grid':
        newGrid = self.copyGrid()
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
    def estRemplis(self) -> bool:
        remplis = True
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == self._CASE_VIDE:
                    remplis = False
        return remplis
    
    '''
    Indique si une position donnée est correcte ou non, aka si un pion est placable
    param : positionPion -> la position donnée de placement de pion
    return : boolean -> si la position est correcte ou non
    '''
    def estPlacable(self, positionPion) -> bool:
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


    def copyGrid(self) -> 'Grid':
        newGrid = Grid()

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                newGrid.grid[i][j] = self.grid[i][j]
        
        return newGrid


class Player():

    def __init__(self, value) -> None: # est-ce correct ?
        # boolean is_ia ?
        self.value = value

        pass

    def __str__(self) -> str:
        return str(self.value)
        
    '''
    Fait jouer le joueur : prend le terrain actuel du jeu et retourne la position de la colonne que le joueur à choisit (dépend du type de joueur)
    '''
    def playTurn(self, curr_grid) -> int:
        #prend un terrain en attribut, et ressort une valeur, le move qu'il souhaite jouer
        #pour cela, en fonction du tape de joueur demande a l'humain, ou a l'ia
        move = self.inputJoueur(curr_grid)

        return move

    '''
    se charge de l'input des joueur, retourne la colonne selectionnée
    return : positionChoix : int de la colonne choisie
    '''
    def inputJoueur(self, curr_grid) -> int:
        #on commence à -1 pour l'effectuer au moins une fois
        positionChoix = -1
        while (positionChoix < 0 or positionChoix > len(curr_grid.grid) -1):
            #a ameliorer : partie affichage dediée
            positionChoix = int(input(f"Joueur {self.value}, sur quelle colonne souhaitez-vous placer votre pion ? /n>"))
        return positionChoix
        ...


class Jeu:
    '''
    initie la classe jeu avec un tour de joueur et une grille format 7x6

    probleme actuel : grille en format ligne-colonne et non colonne-ligne
    '''
    def __init__(self) -> None:

        self.curr_grid = Grid()


        self.player1 = Player(1)
        self.player2 = Player(2)
        self.curr_player = self.player1 # à changer
        pass

    '''
    retourne un string montrant l'etat du jeu, avec une indication du joueur et de l'etat de la grille
    '''
    def __str__(self) -> str:
        etat = ""
        etat += "joueur : " + str(self.curr_player) + "\n" + "grille :"
        etat += str(self.curr_grid)
        return etat


    def boucleJeu(self) -> None:
        #input du joueur
        #verification de l'input et redemande jusqu'à bon
        #place pion
        #verifie si gagnant
        #si gagnant, jeu s'arrete, joueur en cours déclaré vainqueur
        #sinon, verification que terrain n'est pas remplis
        #puis changement de joueur, et on recommence

        est_gagne = False
        while not self.curr_grid.estRemplis() and not est_gagne:
            #a ameliorer : partie affichage dediée
            print(self)
            choixJoueur = self.curr_player.playTurn(self.curr_grid)
            print("DEBUG boucleJeu : inputJoueur() passé")
            while not self.curr_grid.estPlacable(choixJoueur):
                
                #a ameliorer : partie affichage dediée
                print("le pion n'est pas placable à cet endroit, veuillez réessayer.")
                choixJoueur = self.curr_player.playTurn(self.curr_grid)
            
            self.curr_grid = self.curr_grid.placerPion(choixJoueur, self.curr_player)
            est_gagne = self.curr_grid.estPionGagnant(choixJoueur)

            if not est_gagne and (not self.curr_grid.estRemplis()) :
                self.jSuivant()
        
        print("partie finie !")
        if self.curr_grid.estRemplis():
            print("Le terrain est entièrement remplis, il y a donc égalité.")
        else :
            print(f"le gagnant est joueur {self.curr_player}, félicitation !")

        ...



    '''
    change le joueur en cours
    '''
    def jSuivant(self) -> None:
        if self.curr_player == self.player1:
            self.curr_player = self.player2
        else: 
            self.curr_player = self.player1


    





if __name__ == "__main__":
    jeu = Jeu()
    print(jeu)
    #print(jeu.estPlacable(3))
    #jeu.placerPion(3)  
    #print(jeu)
    #jeu.grid[1][2] = 1
    #print(jeu)

    #jeu.placerPion(2)
    #print(jeu)
    #jeu.placerPion(1)
    #print(jeu)
    #jeu.placerPion(4)
    #print(jeu)
    #print(jeu.estGagne(4))

    # print("DEBUG MAIN : TEST : verification des cas de gagne :")
    # jeu2 = Jeu()
    # jeu2.grid[1][5] = 1
    # jeu2.grid[2][4] = 1
    # jeu2.grid[3][3] = 1
    # jeu2.grid[4][2] = 1
    # print(jeu2)
    # print(jeu2.estGagne(1))

    # print("DEBUG MAIN : FIN TESTS : verifications de cas gagne")
    print("DEBUG MAIN : DEBUT TEST : partie complete :")
    # jeu3 = Jeu()
    # #print(jeu3.estRemplis())
    # jeu3.boucleJeu()

    jeu.boucleJeu()

    print("DEBUG MAIN : FIN DES TESTS")
