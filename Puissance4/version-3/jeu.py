# Auteur : Arthur Romary
# Tentative de creation d'un puissance 4
# Pas d'affichage visuel, que sur terminal.
# but du jeu : deux joueur doivent poser des jetons tours à tours
# le premier qui fait un alignement (horizontal, vertical, diagonal) de quatre de ses jetons gagne
# taille du quadrillage / grille : 7*6 (L*H)
# version 2 : retravaillage du code pour être plus adapté à la POO
from player import Player
from grid import Grid


class Jeu:
    '''
    initie la classe jeu avec un tour de joueur et une grille format 7x6

    probleme actuel : grille en format ligne-colonne et non colonne-ligne
    '''
    def __init__(self) -> None:

        self.curr_grid = Grid()


        self.player1 = Player(0)
        self.player2 = Player(1)
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
