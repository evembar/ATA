import pygame
import random
import sys
import script
import time

FPS = 30
AnimCount = -1
CountRepeat = 0
color_metro = [(255,0,0), (255,255,255), (0,0,0)]
metro_font = ['fonts/segoeui.ttf', 'fonts/segoeuisl.ttf', 'fonts/segoeuib.ttf']

load_metro = [pygame.image.load('images/animation/load/01.png'),
pygame.image.load('images/animation/load/02.png'),
pygame.image.load('images/animation/load/03.png'),
pygame.image.load('images/animation/load/04.png'),
pygame.image.load('images/animation/load/05.png'),
pygame.image.load('images/animation/load/06.png'),
pygame.image.load('images/animation/load/07.png'),
pygame.image.load('images/animation/load/08.png'),
pygame.image.load('images/animation/load/09.png'),
pygame.image.load('images/animation/load/10.png')]

logo_metro = pygame.image.load('images/logo/logo.png')

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
#screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("ATA Framework")
clock = pygame.time.Clock()
def metro_load_fun():
    global AnimCount
    global CountRepeat
    
    x = 530
    y = 530
    
    screen.blit(load_metro[AnimCount//5], (x, y))
    AnimCount += 1 
    pygame.display.flip()
    
    if AnimCount >= 50:
        AnimCount = 0
        CountRepeat = CountRepeat + 1
        print(CountRepeat)
    if CountRepeat == 3:
        pygame.quit()
        script.script(color_metro = color_metro,
                      metro_font = metro_font)
    

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(color_metro[0])
    screen.blit(logo_metro, (500,0))
    metro_load_fun()   
    pygame.display.flip()


pygame.quit()
