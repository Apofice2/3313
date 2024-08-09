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

    dt = 0

    image_joueur = pygame.image.load(IMG_PLAYER_BASE)

    joueur = image_joueur.get_rect()

    joueur.x, joueur.y = (100, 100)  # Coordonnées arbitraire

    bouton_menu = Bouton((200, 100), IMG_BLOCK_METAL, (400, 300), "titre_temporaire")

    # game loop
    while JEUX_ON:

        screen.fill(COULEUR_FOND_FENETRE)

        for event in pygame.event.get():
            if bouton_menu.detection_bouton(event) == True:
                JEUX_ON = False

            if event.type == pygame.QUIT:
                JEUX_ON = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            joueur.y -= 5
        if keys[pygame.K_s]:
            joueur.y += 5
        if keys[pygame.K_q]:
            joueur.x -= 5
        if keys[pygame.K_d]:
            joueur.x += 5


        # Affichage du joueur.
        screen.blit(image_joueur, (joueur.x, joueur.y))
        pygame.draw.rect(screen, (0, 255, 0), joueur, 2)

        bouton_menu.affichage_image(screen)

        # limits FPS to 60
        # clock.tick(60)
        dt = clock.tick(60)/1000

        # flip() met à jour l'image
        pygame.display.flip()

    # quit
    pygame.quit()
