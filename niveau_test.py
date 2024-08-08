import pygame
from sys import exit

pygame.init()
width, height = 1280,720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test")
clock = pygame.time.Clock() 

rect_x = width // 2
rect_y = height // 2
rect_width = 25
rect_height = 25
rect_speed = 500

rect1_outer_cursor = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
rect1_inner_cursor = pygame.Rect(rect_x, rect_y, 2, 2)

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 10)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
    screen.fill((230,230,230))

    # texte pos des rect
    text_surface_rect = my_font.render("x:"+str(rect1_inner_cursor.x)+" y:"+str(rect1_inner_cursor.y), False, (0, 0, 0))
    screen.blit(text_surface_rect, (20,20))
    
    # texte pos du curseur
    text_surface_mouse = my_font.render("mouse position:"+str(pygame.mouse.get_pos()), False, (0, 0, 0))
    screen.blit(text_surface_mouse, (100,100))

    pygame.draw.rect(screen,"grey", rect1_outer_cursor)
    pygame.draw.rect(screen,"red", rect1_inner_cursor)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rect1_outer_cursor.y -= rect_speed * dt
        rect1_inner_cursor.y -= rect_speed * dt
    if keys[pygame.K_s]:
        rect1_outer_cursor.y += rect_speed * dt
        rect1_inner_cursor.y += rect_speed * dt
    if keys[pygame.K_a]:
        rect1_outer_cursor.x -= rect_speed * dt
        rect1_inner_cursor.x -= rect_speed * dt
    if keys[pygame.K_d]:
        rect1_outer_cursor.x += rect_speed * dt
        rect1_inner_cursor.x += rect_speed * dt

    # Ensure the rectangle stays within the window boundaries
    rect1_outer_cursor.x = max(0, min(rect1_outer_cursor.x, width))
    rect1_outer_cursor.y = max(0, min(rect1_outer_cursor.y, height))
    rect1_inner_cursor.x = max(0, min(rect1_inner_cursor.x, width))
    rect1_inner_cursor.y = max(0, min(rect1_inner_cursor.y, height))
    

    pygame.display.flip()
    dt = clock.tick(60) / 1000

# quit
pygame.quit()