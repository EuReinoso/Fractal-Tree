import pygame, math

pygame.init()

class Stick:
    def __init__(self, p_1, p_2,sons_quant= 1):
        self.p1 = p_1
        self.p2 = p_2
        self.sons_quant = sons_quant
        self.sons = []

        if self.get_length() > 1:
            self.init_sons()

    def draw(self,window, color):
        pygame.draw.line(window, color, self.p1, self.p2)

    def init_sons(self):
        for i in range(self.sons_quant):
            p1 = (self.p2[0], self.p2[1])
            p2 = (self.p2[0], self.p2[1] + self.get_length()/2)
            self.sons.append(Stick(p1, p2))

    def get_length(self):
        x = self.p1[0] - self.p2[0]
        y = self.p1[1] - self.p2[1]
        return math.pow(math.pow(x,2) + math.pow(y,2),1/2)
