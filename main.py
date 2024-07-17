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
in_chose_hero = False
in_card_chose = False

in_level_passing = False

current_level = 1
screen_info = [screen, screen_scale, screen_size]

pygame.init()
from data.classes.MainMenu import Menu
from data.classes.HeroChoseMenu import HeroChoseMenu
from data.classes.CardChooseMenu import CardChooseMenu

menu = Menu(screen_info)

from data.classes.Level import Level

from data.global_functions import restore

#hero
hero_class = 'bercerk'

while running:
    if in_menu:
        menu.draw(screen)
        if (menu.player_action_check()):
            in_menu = False
            in_level_passing = True
            # Go to 1st level, create a player
            level_passing = Level(current_level, screen_info)
            del menu
            print('OK')
    elif in_chose_hero:
        hero_chose_menu.draw(screen)
        if hero_chose_menu.player_action_check():
            in_chose_hero = False
            in_level_passing = True
            # Go to 1st level, create a player
            level_passing = Level(current_level, screen_info)
            del hero_chose_menu
    elif in_card_chose:
        if card_chose_menu.draw(screen):
            print("OK")
            in_card_chose = False
            in_level_passing = True

            restore.next_level_parameters()

            level_passing = Level(current_level, screen_info)
            del card_chose_menu
    elif in_level_passing:
        # If player goes on next level
        res = level_passing.draw(screen_info)
        if res == 'DEFEAT':
            in_menu = True
            in_level_passing = False
            menu = Menu(screen_info)
            restore.null_parameters()
        elif (res == 'WIN'):
            current_level += 1

            in_level_passing = False
            in_card_chose = True

            card_chose_menu = CardChooseMenu(screen_info)

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