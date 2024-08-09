from utile_import import * # textures file pathings
import pygame
import pandas
import os

class Bouton:

    # attribues
    taille_bouton = 0.0

    image_bouton = IMG_BOUTON_DEFAUT

    coordonnée_bouton = (0,0)

    bouton = None

    text_afficher = None

    zone_text = None

    def __init__(self, taille_bouton ,image_bouton, coordonnée_bouton, text):

        self.taille_bouton = taille_bouton

        self.image_bouton = pygame.image.load(image_bouton)

        self.coordonnée_bouton = coordonnée_bouton

        self.text = text

        self.image_bouton = pygame.transform.scale(self.image_bouton, self.taille_bouton)

        self.bouton = self.image_bouton.get_rect()

        self.bouton.x, self.bouton.y = coordonnée_bouton

        # Création d'une police
        font = pygame.font.Font(None, 40)

        # Création du texte
        self.text_afficher = font.render(text, True, (255, 255, 0))

    # méthode qui colle l'image.
    def affichage_image(self, screen):

        # Affichage de l'image dans le rectangle
        screen.blit(self.image_bouton, self.bouton)
        screen.blit(self.text_afficher, self.bouton.center)

        # Rectangle vert, épaisseur 2 pixels
        pygame.draw.rect(screen, (255, 255, 0),self.bouton, 2)

    def detection_bouton(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.bouton.collidepoint(event.pos):
                print("gagner")
                return True
            else:
                return False





