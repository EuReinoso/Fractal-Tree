import pygame

pygame.init()

class Stick:
    def __init__(self,size,pos):
        self.pos = pos
        self.size = size
        self.surface = pygame.Surface(size)
        self.sons = []
        self.sons_quant = 1

        self.init_sons()

    def init_sons(self):
        for i in range(self.sons_quant):
            size = (self.size[0], self.size[1]/2)
            pos = self.pos
            sons.append(Stick(size,pos))
