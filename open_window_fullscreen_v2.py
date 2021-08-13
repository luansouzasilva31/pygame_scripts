import pygame, os

'''
    A classe abaixo abre uma imagem em fullscreen. Para fechá-la, basta chamar
    o método close(). Isso permite que o controle possa ser feito in-código,
    não necessitando de eventos usuais como delay ou key_pressed.
'''

class HDMI():
    def __init__(self, path):
        # set variables
        self.path = path
        
        # init pygame
        pygame.init()
        
        # set resolution and create surface
        self.resolution = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.surface = pygame.display.set_mode(self.resolution, pygame.SCALED|pygame.NOFRAME)

        # Importing image
        self.image = pygame.image.load(self.path)
        
        # Scaling image to the desired resolution
        self.image = pygame.transform.scale(self.image, self.resolution)
        self.rect = self.image.get_rect()
        
        self.surface.blit(self.image, self.rect)
        pygame.display.update()
        
    def close(self):
        pygame.quit()


path = '/home/luansouzasilva/Downloads/dead_37.png'

hdmi = HDMI(path)
pygame.time.delay(3000)
hdmi.close()



