

# Auteur : Arthur Romary
# Tentative de creation d'un puissance 4
# Pas d'affichage visuel, que sur terminal.
# but du jeu : deux joueur doivent poser des jetons tours à tours
# le premier qui fait un alignement (horizontal, vertical, diagonal) de quatre de ses jetons gagne
# taille du quadrillage / grille : 7*6 (L*H)
# version 2 : retravaillage du code pour être plus adapté à la POO

from player import Player
import math

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
        self._CASE_VIDE = "."

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
        while case < len(self.grid[positionPion])-1 and self.grid[positionPion][case] == self._CASE_VIDE :
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
        # il est surement meilleur d'utiliser inf, mais pour l'instant fait sans import math
        # donc pour l'instant : 0 = rien ; -10 = perdu ; 10 = gagne
        # par sécu, si les deux ont win, ce qui n'est pas censé arrivé, c'est considéré comme loose


        # on va utiliser un code d'etude totale du terrain,
        # en y étudiant chaque ligne possible, et chaque colonne
        # on peux y vérifier l'acces par rapport au reste de la ligne en question

        # on vérifie les enchainements de 1, 2 et 3, et on y regarde si ils sont accessibles, etc...
        # on y ajoutera ensuite la distance de colonne aux pions suivants,
        # et la distance maximum théorique au pion.
        # ensuite, on y additione les différents points calculés
        # multipliés par des facteurs en fonctions de s'ils sont positifs ou négatifs, en fonction du joueur en cours
        # et on retourne le score



        score = 0
        # constante pour quitter quand la partie est finie
        _perdu = -math.inf
        _gagne = math.inf

        # constante de coefficient pour que les coup bon de nous ou de l'adversaire soit plus ou moins valorisés
        _coeffBon = 1
        _coeffMauvais = -1
        
        enough = False

        # revue des colonnes :
        # colones = [], ligne = [][]
        for colonne in self.grid: # range(len(self.grid)):

            last_case = None
            suite_len = 1
            mur = 0

            for case in colonne[::-1] : # range(len(self.grid[colonne]))[::-1]: #pas sur pour le -1

                # ajout et finition de suite
                if case == last_case:
                    suite_len += 1

                else :
                    # finir la dernière suite, et ajouter les points si nécéssaire
                    if last_case == self._CASE_VIDE:
                        # cas dans lequel on est un pion après une case vide
                        # rien à faire à par ne pas le compter comme un mur

                        # reset :
                        mur = 0
                        suite_len = 1

                    elif last_case == None:
                        # cas dans lequel on est le pion après le mur
                        # rien à faire à par le compter comme un mur

                        # reset :
                        mur = 1
                        suite_len = 1

                    elif last_case == player :
                        # cas dans lequel on finit une suite à nous
                        # il faut prendre en compte la taille de la suite, les possibles murs autours
                        # et donner un score en conséquence

                        if case != self._CASE_VIDE:
                            mur += 1

                        if suite_len == 1 :
                            #le nombre de mur ne peux en théorie pas être en dessous de 1
                            if mur == 2 :
                                score += _coeffBon * 0
                            elif mur == 1 :
                                score += _coeffBon * 1

                        elif suite_len == 2 :
                            if mur == 2 :
                                score += _coeffBon * 1
                            elif mur == 1 :
                                score += _coeffBon * 3

                        elif suite_len == 3 :
                            if mur == 2 :
                                score += _coeffBon * 3
                            elif mur == 1 :
                                score += _coeffBon * 5

                        else :
                            score = _gagne
                            enough = True

                        # reset :
                        mur = 1
                        suite_len = 1

                    else :
                        # cas dans lequel on finit une suite adversaire
                        # il faut prendre en compte la taille de la suite, les possibles murs autours
                        # et donner un score en conséquence

                        if case != self._CASE_VIDE:
                            mur += 1

                        if suite_len == 1 :
                            #le nombre de mur ne peux en théorie pas être en dessous de 1
                            if mur == 2 :
                                score += _coeffMauvais * 0
                            elif mur == 1 :
                                score += _coeffMauvais * 1

                        elif suite_len == 2 :
                            if mur == 2 :
                                score += _coeffMauvais * 1
                            elif mur == 1 :
                                score += _coeffMauvais * 3

                        elif suite_len == 3 :
                            if mur == 2 :
                                score += _coeffMauvais * 3
                            elif mur == 1 :
                                score += _coeffMauvais * 5

                        else :
                            score = _perdu
                            enough = True
                            
                        #reset :
                        mur = 1
                        suite_len = 1



                last_case = case
        
        return score


    '''
    Will return a tuple containing the position and the player who last placed a token in a given column.
    '''
    def lastPlacedToken(self, positionPion: int) -> tuple:
        case = 0
        while case < len(self.grid[positionPion])-1 and self.grid[positionPion][case] == self._CASE_VIDE:
            case+=1

        if self.grid[positionPion][case] == self._CASE_VIDE:
            print("DEBUG lastPlacedToken : pas de pion placé dans cette colonne")
            return None
        else :
            return (case, self.grid[positionPion][case])


    def generateSons(self, player):
        t = []
        for c in self.genereateAllPlays():
            t.append(self.placerPion(c, player))
        return t
