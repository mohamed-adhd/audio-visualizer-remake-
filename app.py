import pygame 
import sys
from source import Button,callback,last_s
import sounddevice as sd
import numpy as np
pygame.init()
font=pygame.font.Font(None,30)
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption("remake viz")
mode=0
impo=Button(450,350,150,75,"import a file",pygame.Color('green'),pygame.Color('dark green'),pygame.Color('black'))
live =Button(650,350,150,75,"live mode",pygame.Color('blue'),pygame.Color('dark blue'),pygame.Color('black'))
weltxt="welcome to audio visualizer remake ! choose your input :"
txt1=font.render(weltxt,True,pygame.Color('white'))
stream=sd.InputStream(callback=callback,channels=2,samplerate=44100,blocksize=2024)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if mode==0:
            if(impo.handle_event(event)):
                mode=1
                impo.is_hovered=False
            elif(live.handle_event(event)):
                mode=2
                live.is_hovered=False
    screen.fill(pygame.Color("black"))
    if mode==0:
        impo.draw(screen)
        live.draw(screen)
        screen.blit(txt1,(385,100))
    elif mode==1:
        #brother they get it so easy with the libraries and shi , like , everything is just a fonction u dont have to do anything 
        stream=np.array_split(last_s,120)
        bar_val=[np.mean(bar) for bar in stream]
        xb=40
        for b in bar_val:
            pygame.draw.rect(screen,pygame.Color('white'),(xb,720-b,b,10))
            xb+=10
            
            
    pygame.display.flip()
