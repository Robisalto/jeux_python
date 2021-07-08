import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #definir l'image de la comete
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,5)
        self.rect.x = random.randint(20,800)
        self.rect.y = -random.randint(0,800)
        self.comet_event = comet_event

    def remove_comet(self):
        self.comet_event.all_comets.remove(self)

        #verfier si le nombre de cometes est zero
        if len(self.comet_event.all_comets) ==0:
            #remettre la barre à zero
            self.comet_event.reset_percent()
            #apparaitre les 2 premiers monstres
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            #on la retire
            self.remove_comet()
            # si il n'y a plus de comètes dans le jeu
            if len(self.comet_event.all_comets) == 0 :
                #remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False



        if self.comet_event.game.collision_check(self, self.comet_event.game.all_players):
            print("joueur touché")
            #retirer la boule de feu
            self.remove()
            #subir 20 points de dégats
            self.comet_event.game.player.damage(20)