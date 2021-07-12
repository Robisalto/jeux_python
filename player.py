import pygame
from projectile import Projectile
import animation
#creer une classe joueur

class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect =self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health >0:
            self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        #dessine la bar de vie
        pygame.draw.rect(surface, (60,63,60),[self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (11, 210, 46), [self.rect.x +50, self.rect.y +20, self.health, 7])


    def launch_projectile(self):
        #creer une instance de projectile

        self.all_projectiles.add(Projectile(self))

        #demarrer l'animation du lanbcer
        self.start_animation()

    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.collision_check(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity