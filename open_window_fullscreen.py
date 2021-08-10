import pygame
from pygame.locals import *

# This function closes window based on time clocking
def open_window1(path, resolution, time):
    pygame.init()
    surface = pygame.display.set_mode(resolution, FULLSCREEN)
    
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, resolution)
    
    rect = image.get_rect(); rect.center = resolution[0]//2, resolution[1]//2
    
    surface.blit(image, rect)
    pygame.display.update()
    
    pygame.time.delay(time)
    pygame.quit()

# this function closes window based on key pressing
def open_window2(path, resolution, key):
    # key dict
    key_dict={'a':K_a, 'b':K_b, 'c':K_c, 'd':K_d, 'e':K_e, 'f':K_f,
              'g':K_g, 'h':K_h, 'i':K_i, 'j':K_j, 'k':K_k, 'l':K_l,
              'm':K_m, 'n':K_n, 'o':K_o, 'p':K_p, 'q':K_q, 'r':K_r,
              's':K_s, 't':K_t, 'u':K_u, 'v':K_v, 'w':K_w, 'x':K_x,
              'y':K_y, 'z':K_z}
    
    pygame.init()
    surface = pygame.display.set_mode(resolution, FULLSCREEN)
    
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, resolution)
    
    rect = image.get_rect(); rect.center = resolution[0]//2, resolution[1]//2
    
    surface.blit(image, rect)
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: #press-key events
                if event.key == key_dict[key]: # if C key is pressed ...
                    running = False
    pygame.quit()
    
if __name__=='__main__':
    # set parameters
    time = 3000 # in miliseconds
    resolution = (1920,1080)
    path = r'./dead_417.png'
    open_window1(path,resolution,time)

    #key = 'c' # only lowercase letters!
    #open_window2(path, resolution, key)





