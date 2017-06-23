from pygame.locals import *
import pygame
 
class Player(pygame.sprite.Sprite):
    # Starting position and speed
    x = 10
    y = 10
    speed = 10

    def __init__(self):
        super().__init__()
 
        # Create the Surface
        self.image = pygame.Surface([250, 250])
 
        # Load the image
        self.image = pygame.image.load("images/spatula.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 30))
 
        # Create a Rectangle to handle location, collision
        self.rect = self.image.get_rect(center=(10,350))
 
        #Set the horizontal starting position. This never needs to change
        self.rect.y = 380
