from pygame.locals import *
import pygame
 
class Bubble(pygame.sprite.Sprite):

    def __init__(self, a, b):
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image = pygame.image.load("images/donut.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(40,40))
        self.rect.x = a
        self.rect.y = b

