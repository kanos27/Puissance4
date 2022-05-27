from jeu import Jeu


def main():
    jeu = Jeu()
    print(jeu)
    # print(jeu.estPlacable(3))
    # jeu.placerPion(3)
    # print(jeu)
    # jeu.grid[1][2] = 1
    # print(jeu)

    # jeu.placerPion(2)
    # print(jeu)
    # jeu.placerPion(1)
    # print(jeu)
    # jeu.placerPion(4)
    # print(jeu)
    # print(jeu.estGagne(4))

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


if __name__ == '__main__':
    main()
