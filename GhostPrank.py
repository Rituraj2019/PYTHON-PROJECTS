import pygame
from time import sleep
pygame.init() #inistializing module
pygame.mixer.init() # II
window=pygame.display.set_mode((0,0), pygame.FULLSCREEN)  #creating window for our application, using display.setmode
pygame.mixer.music.load("Hai Junoon.mp3") #loading nice music for starting time using music.load method
pygame.mixer.music.play() #playing nice music for starting time using music.play method

sleep(5)  #pause the execution of current thread for 5 sec. I.e before executing next code, it will wait for 5sec

pygame.mixer.music.load("Birthday Bash.mp3")  #loading scary music for game time
pygame.mixer.music.play()  #playing scaring music for game time

sleep(5) #pausing exeution of next code for 5 sec

image=pygame.image.load("Nilaroom.jpg")  #loading image by using image.load method
window.blit(image, (0,0))   #take the loaded image and blit/shhow it on the screen at (0,0)
pygame.display.update() #updating the portion of screen/display with that image

sleep(10) #pausing execution of next line of code (Which is by default stop in this case) for 10 sec.