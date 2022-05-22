# Auteur : Arthur Romary
# Tentative de creation d'un puissance 4
# Pas d'affichage visuel, que sur terminal.
# but du jeu : deux joueur doivent poser des jetons tours à tours
# le premier qui fait un alignement (horizontal, vertical, diagonal) de quatre de ses jetons gagne
# taille du quadrillage / grille : 7*6 (L*H)
# version 2 : retravaillage du code pour être plus adapté à la POO



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
