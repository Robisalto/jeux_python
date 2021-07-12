import pygame


#classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    #definir les choses à faire à la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f"assets/{sprite_name}.png")
        self.current_image = 0 #commencer l'anim à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #definir une méthode pour demarrer l'animation
    def start_animation(self):
        self.animation = True

    #definir une méthode pour animer le sprite
    def animate(self, loop = False):


        #vérifier que l'animation est active

        if self.animation:

            #passer à l'image suivante
            self.current_image += 1

            #verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                #remettre l'anim au depart
                self.current_image = 0

                #verfier si l'animation est en mode boucle:
                if loop is False:

                    #desactivation de l'animation
                    self.animation = False
            #modifier l'image de l'animation précédente par la nouvelle
            self.image = self.images[self.current_image]

    #definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les images du sprite
    images=[]

    #recuperer le chemin
    path = f"assets/{sprite_name}/{sprite_name}"

    #bouler sur chaque image danzs le dossier
    for num in range(1,24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))
    #renvoyer le contenu

    return images

#definir un dictionnaire qui va contenir les images chargées de chaque sprite
#mummy -> [mummy1.png, ....,mummyn.png]
animations = {
    "mummy":load_animation_images("mummy"),
    "player":load_animation_images("player")
}