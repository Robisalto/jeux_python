import pygame


#creer une classe pour gerer cet evenement

class CometFallEvent:

    #lors du chargement on va creer un compteur
    def __init__(self):
        self.percent = 0
        self.percent_speed =5

    def add_percent(self):
        self.percent += self.percent_speed/100
    def update_bar(self, surface):

        #ajouter du pourcentage à la barre
        self.add_percent()
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