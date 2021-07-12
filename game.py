import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent

# creer une classe qui va representer le jeu

class Game:
    def __init__(self):
        #definir si le jeu a commencé ou non
        self.is_playing = True
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()
        #generer l'evenement comete
        self.comet_event = CometFallEvent(self)
    def start(self):
        self.is_playing =True
        monster = Monster(self)
        self.all_monsters.add(monster)

    def game_over(self):
        #remettre le jeu à neuf, retirer les monstres, remttre le joueur à 100 de vie, remettre le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.comet_event.reset_percent()


    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        #actualiser l'animation du jour

        self.player.update_animation()

        #actualiser la barre evenement du jeu
        self.comet_event.update_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # # recuperer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #recuperer les comets
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer mon groupe de projectiles

        self.player.all_projectiles.draw(screen)

        # appliquer les monstres

        self.all_monsters.draw(screen)

        #appliquer les comets
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur veut aller à gauche ou à droite

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def collision_check(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

