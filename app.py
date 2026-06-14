import pygame 
import sys


pygame.init()
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption("remake viz")


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()