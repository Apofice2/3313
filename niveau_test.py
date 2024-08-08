import pygame
from sys import exit

pygame.init()
width, height = 1280,720
screen = pygame.display.set_mode((width, height))
screen.fill((230,230,230))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

pygame.Rect(width/2, height/2, 1, 1)
pygame.draw.rect(screen,"red", rect,)


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit()

        pygame.display.flip()
        clock.tick(60)

# quit
pygame.quit()