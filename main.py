import pygame

from game import Game

pygame.init()


#generer la fenetre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080,720))

#importer l'arrière plan de la fenetre
backgroung = pygame.image.load("assets/bg.jpg")

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
