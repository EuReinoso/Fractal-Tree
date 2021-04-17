import pygame,sys
from stick import Stick

pygame.init()

WINDOW_SIZE = (640, 480)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Fractal Tree')

pos_init = ((WINDOW_SIZE[0]/2, WINDOW_SIZE[1]),(WINDOW_SIZE[0]/2,WINDOW_SIZE[1] - 100))

stick = Stick(pos_init[0], pos_init[1])
tree = []
tree.append(stick)

def tree_init(i=0):
    global tree
    for son in tree[i].sons:
        tree.append(son)
        i += 1
        if len(tree[i].sons) > 0:
            tree_init(i= i)
            
def draw_tree():
    color = [200,200,200]
    degrade = 30
    for stk in tree:
        stk.draw(window, color)
        
        if color[2] >= degrade:
            color[1] -= degrade
            color[2] -= degrade

tree_init()
while True:
    window.fill((0, 0, 0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    draw_tree()
    pygame.display.update()
    pygame.display.flip()