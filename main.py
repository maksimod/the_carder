#modules
import random
import keyboard
import pygame
from sys import exit

#draw display, start preferences
screen_scale = 1.5
w,h = int(1200*screen_scale), int(600*screen_scale)
pygame.init()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Carder')
#To control fps 
clock = pygame.time.Clock()


from data.classes.Menu import Menu
menu = Menu(screen,screen_scale,[w,h])

from data.classes.Level import Level
level_passing = None

running = True
in_menu = True
in_level_passing = False
while running:
    #Меню
    if in_menu:
        menu.draw(screen)
        if menu.player_action_check():
            in_menu = False
            in_level_passing = True
            level_passing = Level()
    elif in_level_passing:
        level_passing.draw()

    #Updating display, control fps
    pygame.display.update()
    clock.tick(60)
    #interrupt quit error
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if keyboard.is_pressed('q'):
        running = False