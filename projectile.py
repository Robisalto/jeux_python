import pygame

#definir la classe projectile

class Projectile(pygame.sprite.Sprite):

    #definir le constructeur de cette classe
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("assets/projectile.png")
        self.rect = self.image.get_rect()
