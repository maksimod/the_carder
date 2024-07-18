import keyboard
import pygame
from sys import exit

from data.classes.MainMenu import Menu
from data.classes.HeroChoseMenu import HeroChoseMenu
from data.classes.CardChooseMenu import CardChooseMenu
from data.classes.Level import Level

from data.global_vars.screen_info import *
from data.global_functions import restore

pygame.display.set_caption('Carder')

# To control fps
clock = pygame.time.Clock()

level_passing = None

running = True

in_menu = False
in_chose_hero = False
in_card_chose = True
in_level_passing = False

current_level = 1

pygame.init()

menu = Menu()
card_chose_hero = HeroChoseMenu()
card_chose_menu = CardChooseMenu()
level_passing = Level(current_level)


#hero
hero_class = 'bercerk'

while running:
    if in_menu:
        menu.draw()
        if (menu.player_action_check()):
            in_menu = False
            in_level_passing = True
            # Go to 1st level, create a player
            level_passing = Level(current_level)
            del menu
            print('OK')
    elif in_chose_hero:
        hero_chose_menu.draw()
        if hero_chose_menu.player_action_check():
            in_chose_hero = False
            in_level_passing = True
            # Go to 1st level, create a player
            level_passing = Level(current_level)
            del hero_chose_menu
    elif in_card_chose:
        if card_chose_menu.draw():
            print("OK")
            in_card_chose = False
            in_level_passing = True

            restore.next_level_parameters()

            level_passing = Level(current_level)
            del card_chose_menu
    elif in_level_passing:
        res = level_passing.draw()
        if res == 'DEFEAT':
            in_menu = True
            in_level_passing = False
            menu = Menu()
            restore.null_parameters()
        elif (res == 'WIN'):
            current_level += 1

            in_level_passing = False
            in_card_chose = True

            card_chose_menu = CardChooseMenu()

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