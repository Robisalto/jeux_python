import pygame
from player import Player

# creer une classe qui va representer le jeu

class Game:
    def __init__(self):
        #generer notre joueur
        self.player = Player()
        self.pressed = {}

