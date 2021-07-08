import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        #definir l'image de la comete
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(20,800)
        self.rect.y = -random.randint(0,800)

    def fall(self):
        self.rect.y += self.velocity