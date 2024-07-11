import keyboard
import pygame
from sys import exit
# Set screen
screen_scale = 1.5
w, h = int(1200 * screen_scale), int(600 * screen_scale)
screen_size = [w, h]
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Carder')

# To control fps
clock = pygame.time.Clock()

level_passing = None

running = True
in_menu = True
in_level_passing = False

current_level = 1
screen_info = [screen, screen_scale, screen_size]

pygame.init()
from data.classes.Menu import Menu
menu = Menu(screen_info)

from data.classes.Level import Level
from data.global_vars import deck,hero

from random import shuffle

#hero
hero_class = 'bercerk'

while running:
# Меню
    if in_menu:
        menu.draw(screen)
        if menu.player_action_check():
            in_menu = False
            in_level_passing = True
            # Go to 1st level, create a player
            level_passing = Level(current_level, screen_info)
            del menu
    elif in_level_passing:

        # If player goes on next level
        res = level_passing.draw(screen_info)
        if res == 'DEFEAT':
            # running = False
            # break
            hero.hero[hero.hero_class][0][0] = hero.hero[hero.hero_class][1][0]
            hero.hero[hero.hero_class][0][1] = 0
            hero.hero[hero.hero_class][0][2] = hero.hero[hero.hero_class][1][2]
            hero.hero[hero.hero_class][0][3] = hero.hero[hero.hero_class][1][3]
            hero.hero[hero.hero_class][0][4] = hero.hero[hero.hero_class][1][4]

            deck.input = [['attack','defense'][i%2] for i in range(12)]
            shuffle(deck.input)
            deck.output = []

            in_menu = True
            in_level_passing = False
            menu = Menu(screen_info)
        elif (res == 'WIN'):
            level_passing = Level(current_level, screen_info)
            current_level += 1


    # Updating display, control fps
    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if keyboard.is_pressed('q'):
        running = False

print('OK!')