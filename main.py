import pygame
import math

from game import Game

pygame.init()


#generer la fenetre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080,720))

#importer l'arrière plan de la fenetre
backgroung = pygame.image.load("assets/bg.jpg")

#importer notre bannière
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() /4)

#importer le bouton pour lancer la partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() /3.33)
play_button_rect.y = math.ceil(screen.get_height() /2)

#charger notre jeu

game = Game()

running = True

#boucle tant que la condition est vraie

while (running):
    #applique l'arriere plan de notre jeu
    screen.blit(backgroung, (0,-200))


    #verifier si notre jeu a commncé ou non
    if game.is_playing:
        #declencher les instructions de la partie
        game.update(screen)
    else:
        # applique la bannière
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))
        screen.blit(banner,(banner_rect.x,0))


    # mettre à jour l'ecran
    pygame.display.flip()

        # si le joueur ferme cette fenetre
    for event in pygame.event.get():
  # l'evenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
                running = False
                pygame.quit()
# detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

                # detecter si la touche espace est utiliséé
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verif pour savoir si la souris est en collison avec jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.start()
