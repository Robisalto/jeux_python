import pygame
from comet import Comet

#creer une classe pour gerer cet evenement

class CometFallEvent:

    #lors du chargement on va creer un compteur
    def __init__(self):
        self.percent = 0
        self.percent_speed = 50

        #definir un groupe de Sprite pour stocker les cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full_loaded(self):
        return self.percent >=100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #apparaitre comet
        self.all_comets.add(Comet())

    def attempt_fall(self):
        #la jauge evenement totalement chargee
        if self.is_full_loaded():
            print("pluie de cometes")
            self.meteor_fall()
            self.reset_percent()

    def update_bar(self, surface):

        #ajouter du pourcentage à la barre
        self.add_percent()

        #appel de la methode pour declencher la pluie de cometes
        self.attempt_fall()

        #barre noire en arriere plan
        pygame.draw.rect(surface, (0,0,0),
            [0, #axe des x
            surface.get_height()-20, #l'axe des y
            surface.get_width(),# ]ongueur de la fenetre
            10 #epaisseur de la barre
            ] )
        #jauge rouge
        pygame.draw.rect(surface, (187, 11, 11),
            [0,  # axe des x
            surface.get_height()-20,  # l'axe des y
            (surface.get_width()/100)*self.percent,  # ]ongueur de la fenetre
            10  # epaisseur de la barre
            ])