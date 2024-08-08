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

    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    # game loop
    while JEUX_ON:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JEUX_ON = False

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # flip() met à jour l'image
        pygame.display.flip()

        # limits FPS to 60
        # clock.tick(60)
        dt = clock.tick(60) / 1000

    # quit
    pygame.quit()
