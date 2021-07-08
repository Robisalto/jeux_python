import pygame
import random

#creation classe monster

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health =100
        self.max_health =100
        self.attack = 0.3
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540
        self.velocity = random.randint(1,2)

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #vérifier si il lui reste des points de vie
        if self.health <=0:
            # Reapparaitre comme un nouveau monstre (pour pas surcharger la mémoire)
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health



    def update_health_bar(self, surface):
        #dessine la bar de vie
        pygame.draw.rect(surface, (60,63,60),[self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (11, 210, 46), [self.rect.x +10, self.rect.y -20, self.health, 5])


    def forward(self):
        #le deplacement se fait si il n'y a pas de collisions
        if not self.game.collision_check(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en collision avec le joueur
        else:
            #infliger des degats
            self.game.player.damage(self.attack)

