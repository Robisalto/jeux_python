import pygame

#definir la classe projectile

class Projectile(pygame.sprite.Sprite):

    #definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y +80
        self.origin_image = self.image
        self.angle = 0

    #faire tourner le projectile
    def rotate(self):
        self.angle +=8
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1)

        #permet de prendre l'origine de l'image au centre de l'image
        self.rect = self.image.get_rect(center = self.rect.center)

    #supprimer le projectile
    def remove(self):
        self.player.all_projectiles.remove(self)

    #faire bouger le projectile
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #vérifier si notre projectile n'est pas present sur l'ecran
        if self.rect.x > 1080:
            self.remove()
