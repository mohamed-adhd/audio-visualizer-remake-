import pygame 
import sys
import source
from source import Button
import sounddevice as sd
import numpy as np
import tkinter as tk
from tkinter import filedialog


pygame.init()
font=pygame.font.Font(None,30)
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption("remake viz")
mode=0
impo=Button(450,350,150,75,"import a file",pygame.Color('green'),pygame.Color('dark green'),pygame.Color('black'))
live =Button(650,350,150,75,"live mode",pygame.Color('blue'),pygame.Color('dark blue'),pygame.Color('black'))
weltxt="welcome to audio visualizer remake ! choose your input :"
txt1=font.render(weltxt,True,pygame.Color('white'))
print(sd.query_devices())
print("default:", sd.default.device)
stream=sd.InputStream(device=2, callback=source.callback, channels=2, samplerate=44100, blocksize=2024)
stream.start()
smooth_vals=None
root=tk.Tk()
root.withdraw()
file=None
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if mode==0:
            if(impo.handle_event(event)):
                file = filedialog.askopenfilename(
                title="Select a file",
                filetypes=[("All Files", "*.*")]
                )
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
    elif mode==2:
        #brother they get it so easy with the libraries and shi , like , everything is just a fonction u dont have to do anything 
        if source.last_s is not None: 
            streamio=np.array_split(source.last_s,120)
            bar_val=np.array([np.mean(bar) for bar in streamio])

        if smooth_vals is None:
            smooth_vals = bar_val
        else:
            smooth_vals =smooth_vals*0.8+bar_val*0.2
        xb=40
        for b in smooth_vals:
            h=int(b*5)
            pygame.draw.rect(screen,pygame.Color('white'),(xb,720-h,8,h))
            xb+=10
    elif mode==1:
        
                    
                    
    pygame.display.flip()
