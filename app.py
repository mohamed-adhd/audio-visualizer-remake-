import pygame 
import sys
from source import Button
pygame.init()
font=pygame.font.Font(None,25)
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption("remake viz")
mode=0
impo=Button(450,350,150,75,"import a file",pygame.Color('green'),pygame.Color('dark green'),pygame.Color('black'))
live =Button(650,350,150,75,"live mode",pygame.Color('blue'),pygame.Color('dark blue'),pygame.Color('black'))
weltxt="welcome to audio visualizer remake ! choose your input :"
txt1=font.render(weltxt,True,pygame.Color('white'))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        impo.handle_event(event)
        live.handle_event(event)
    if impo.clicked:
        mode=1
    if mode==0:
        impo.draw(screen)
        live.draw(screen)
        screen.blit(txt1,(385,100))
    if mode==1:
        impo.draw(screen)
    pygame.display.flip()
