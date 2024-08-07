from utile_import import * # chemin des fichiers de textures
import pygame
import pandas
import os
from Bouton import * # Classe bouton
from variables import *

# Code principal
if __name__ == '__main__':

    # init
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE) # taille de la fenetre
    screen.fill(COULEUR_FOND_FENETRE) # la couleur de fond d'écran

    pygame.display.set_caption(TITRE)   # titre de l'écrans

    clock = pygame.time.Clock()     # init horloge

    etat_jeu = liste_etat_jeu[0]

    bouton_menu = Bouton((200, 100), IMG_BLOCK_METAL, (400, 300), "titre_temporaire")
    bouton_menu.affichage_image(screen)

    # game loop
    while JEUX_ON:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JEUX_ON = False

        

        # flip() met à jour l'image
        pygame.display.flip()

        # limits FPS to 60
        clock.tick(60)

    # quit
    pygame.quit()
