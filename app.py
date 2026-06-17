import pygame 
import sys
import source
from source import Button
import sounddevice as sd
import numpy as np
import io
import tkinter as tk
from tkinter import filedialog
import soundfile as sf
from tinytag import TinyTag
pygame.init()
pygame.mixer.init()
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
stream=sd.InputStream(device=2, callback=source.callback, channels=2, samplerate=44100, blocksize=2048)
stream.start()
smooth_vals=None
root=tk.Tk()
root.withdraw()
file=None
pos=0
clock=pygame.time.Clock()
temp="now playing : "



cs=0

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
                temp+= file[file.rfind("/")+1:]
                txtr=font.render(temp,True,pygame.Color('white'))
                data,sr=sf.read(file)
                mode=1
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                tag= TinyTag.get(file, image=True)
                image_data= tag.get_image()
                ims=pygame.image.load(io.BytesIO(image_data))
                ims=pygame.transform.scale(ims,(300, 200))
                tag= TinyTag.get(file)
                dur=tag.duration
                
                impo.is_hovered=False
            elif(live.handle_event(event)):
                mode=2
                live.is_hovered=False
        elif mode==1:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    mode=0
        elif mode==2:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    mode=0
    screen.fill(pygame.Color("black"))
    if mode==0:
        impo.draw(screen)
        live.draw(screen)
        screen.blit(txt1,(385,100))
    elif mode==2:
        #brother they get it so easy with the libraries and shi , like , everything is just a fonction u dont have to do anything 
        if source.last_s is not None: 
            log_idx = np.geomspace(1, len(source.last_s)-1, 121).astype(int).clip(0, len(source.last_s)-1)
            bar_val = np.array([np.mean(source.last_s[log_idx[i]:log_idx[i+1]+1]) for i in range(120)])
            max_val = np.max(bar_val)
            if max_val > 1:
                bar_val = bar_val / max_val
            else:
                bar_val = np.zeros(120)# noise 
            
        if smooth_vals is None:
            smooth_vals = bar_val
        else:
            smooth_vals =smooth_vals*0.85+bar_val*0.15
        xb=40
        for i,b in enumerate(smooth_vals):
            h=int(b*600)
            t = i / 120
            if t < 0.33:
                color = (255, int(t * 3 * 255), 0)       
            elif t < 0.66:
                color = (int((1 - (t - 0.33) * 3) * 255), 255, 0) # the color palette is a reference to "in rainbows" by radiohead , the beat goes rounnnnnnnnnnnnnnd
            else:
                color = (0, int((1 - (t - 0.66) * 3) * 255), 255) 
            pygame.draw.rect(screen,color,(xb,720-h,8,h),border_radius=4)
            xb+=10
    elif mode==1:
        pm=pygame.mixer.music.get_pos()
        
        ps=pm/ 1000
                #s=pm//60
        #if s==0:
         #   tdt="00:"
        #else :
        #    tdt="0"+str(s)
        #tdt+=str((pm%60000))+"/"+str(dur//60000)+":"+str(dur%60000)
        e_m=str(int(ps//60))
        es=str(int(ps% 60))

        totm= str(int(dur//60))
        tot_s=str(int(dur%60))
        tdt=e_m+":"+es+"/"+totm+":"+tot_s



        chunk=data[pos:pos+2048]
        if chunk.ndim>1:
            chunk=chunk.mean(axis=1)
        fft = np.abs(np.fft.rfft(chunk))
        log_idx = np.geomspace(1, len(fft)-1, 121).astype(int).clip(0, len(fft)-1)
        bar_val = np.array([np.mean(fft[log_idx[i]:log_idx[i+1]+1]) for i in range(120)])
        max_val = np.max(bar_val)
        if max_val > 0:
            bar_val = bar_val / max_val
        if smooth_vals is None:
            smooth_vals = bar_val
        else:
            smooth_vals =smooth_vals*0.8+bar_val*0.2
        xb=40
        for i,b in enumerate(smooth_vals):
            h=int(b*600)
            t = i / 120
            if t < 0.33:
                color = (255, int(t * 3 * 255), 0)       
            elif t < 0.66:
                color = (int((1 - (t - 0.33) * 3) * 255), 255, 0) # the color palette is a reference to "in rainbows" by radiohead , the beat goes rounnnnnnnnnnnnnnd
            else:
                color = (0, int((1 - (t - 0.66) * 3) * 255), 255) 
            pygame.draw.rect(screen,color,(xb,720-h,8,h),border_radius=4)
            xb+=10
        pos+=2048
        screen.blit(txtr,(980,30))
        screen.blit(ims,(980,70))
        pygame.draw.rect(screen,pygame.Color('dark gray'),(150,30,800,20),border_radius=4)
        pygame.draw.rect(screen,pygame.Color('white'),(150,30,(750/dur)*ps,20),border_radius=4)
        tdt=font.render(tdt,True,pygame.Color('white'))
        screen.blit(tdt,(50,30))



                    
    clock.tick(44100//2048)
    pygame.display.flip()
