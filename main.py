import pygame,sys
from tree import Tree

pygame.init()

WINDOW_SIZE = (1280, 960)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Fractal Tree')

pos_init = (WINDOW_SIZE[0]/2, WINDOW_SIZE[1])

angle_increment = 45
length_scale = 0.65
level = 10

while True:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                length_scale += 0.01
            if event.key == pygame.K_DOWN:
                length_scale -= 0.01
            if event.key == pygame.K_RIGHT:
                angle_increment += 2
            if event.key == pygame.K_LEFT:
                angle_increment -= 2
        

    tree = Tree(angle_increment= angle_increment, length_scale= length_scale)
    tree.tree_init(window,pos_init, 90, level= level)
    pygame.display.update()
    pygame.display.flip()