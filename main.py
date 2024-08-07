# image texture
from utile_import import *
# pygame
import pygame
# pandas
import pandas
# os
import os
# bouton
from bouton import *

# nonnnnnnnnnnnnnnnnnnnnnnnnnn

# Code principal
if __name__ == '__main__':

    # variable titre et taille de l'écran
    SCREEN_SIZE = (1000, 1000)
    TITRE = "3313"

    # couleur fond
    FOND = (0, 0, 0)

    # init
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # titre de l'écrans
    pygame.display.set_caption(TITRE)

    # init horloge
    clock = pygame.time.Clock()

    # condition qui continue le jeu
    JEUX_ON = True

    # etat_jeu
    liste_etat_jeu = ["MENU", "NIVEAU_TEST"]

    etat_jeu = liste_etat_jeu[0]

    # game loop
    while JEUX_ON:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JEUX_ON = False

        bouton_menu = Bouton((200, 100), IMG_BLOCK_METAL, (400, 300), "titre_temporaire")

        # la couleur de fond de l'écran
        screen.fill(FOND)

        bouton_menu.affichage_image(screen)

        # flip() met à jour l'image
        pygame.display.flip()

        # limits FPS to 60
        clock.tick(60)

    # quit
    pygame.quit()
