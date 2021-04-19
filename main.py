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

is_angle_increment_up = False
is_angle_increment_down = False
is_length_scale_up = False
is_length_scale_down = False
is_level_up = False
is_level_down = False

def move():
    global angle_increment, length_scale, level
    if is_angle_increment_up:
        angle_increment += 0.5
    if is_angle_increment_down:
        angle_increment -= 0.5

    if is_length_scale_up:
        length_scale += 0.001
    if is_length_scale_down:
        length_scale -= 0.001

    if is_level_up:
        level += 0.1
    if is_level_down:
        level -= 0.1

while True:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                is_length_scale_up = True
            if event.key == pygame.K_DOWN:
                is_length_scale_down = True
            if event.key == pygame.K_RIGHT:
                is_angle_increment_up = True
            if event.key == pygame.K_LEFT:
                is_angle_increment_down = True
            if event.key == pygame.K_w:
                is_level_up = True
            if event.key == pygame.K_s:
                is_level_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                is_length_scale_up = False
            if event.key == pygame.K_DOWN:
                is_length_scale_down = False
            if event.key == pygame.K_RIGHT:
                is_angle_increment_up = False
            if event.key == pygame.K_LEFT:
                is_angle_increment_down = False
            if event.key == pygame.K_w:
                is_level_up = False
            if event.key == pygame.K_s:
                is_level_down = False

    tree = Tree(angle_increment= angle_increment, length_scale= length_scale, width= 2)
    tree.tree_init(window,pos_init, 90, level= level)

    move()

    pygame.display.update()
    pygame.display.flip()