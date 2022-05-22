

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

    '''
    return an arrays with all possible moves a player can make (all players, since theres no difference in this game)
    '''
    def genereateAllPlays(self):
        if self.estRemplis(): # n'est pas supposé arriver je crois
            return []

        plays = []
        for i in range(len(self.grid)):
            if self.grid[i][-1] == self._CASE_VIDE:
                plays.append(i)
        
        return plays

    '''
    Return the game score to a given player, based on his current situation on the grid.
    currently, just changes based on win or loss.
    '''
    def evaluate(self, player):
        #il est surement meilleur d'utiliser inf, mais pour l'instant fait sans import math
        #donc pour l'instant : 0 = rien ; -10 = perdu ; 10 = gagne
        #par sécu, si les deux ont win, ce qui n'est pas censé arrivé, c'est considéré comme loose

        score = 0
        _perdu = -10
        _gagne = 10
        for i in range(len(self.grid)):
            if self.lastPlacedToken(i) == player:
                if self.estPionGagnant(i) and score != _perdu:
                    score = _gagne

            elif self.lastPlacedToken(i) != None:
                if self.estPionGagnant(i):
                    score = _perdu

        return score


    '''
    Will return the player who last placed a token in a given column.
    '''
    def lastPlacedToken(self, positionPion: int):
        case = 0
        while case < len(self.grid[positionPion]) and self.grid[positionPion][case] == self._CASE_VIDE:
            case+=1

        if self.grid[positionPion][case] == self._CASE_VIDE:
            print("DEBUG lastPlacedToken : pas de pion placé dans cette colonne")
            return None
        else :
            return self.grid[positionPion][case]
