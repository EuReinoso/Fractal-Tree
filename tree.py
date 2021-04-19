import pygame, math

pygame.init()

class Tree:
    def __init__(self, width= 1, angle_increment= 30, length_scale = 0.65):
        self.width = width
        self.angle_increment = angle_increment
        self.length_scale = length_scale

    def tree_init(self, window, p, angle , length= 150, level= 10, color= [200,200,200]):
        degrade = 30

        if level > 0 and length > 1:
            rad_angle = math.radians(angle)

            p_new = (p[0] - math.cos(rad_angle) * length, 
                    p[1] - math.sin(rad_angle) * length)
            
            pygame.draw.line(window, color, p, p_new, self.width)
            
            self.tree_init(window, p_new, angle - self.angle_increment, length= length * self.length_scale, level= level-1)
            self.tree_init(window, p_new, angle + self.angle_increment, length= length * self.length_scale, level= level-1)
                
    





    
