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

pygame.init()
from data.classes.Menu import Menu
menu = Menu(screen, screen_scale, screen_size)

from data.classes.Level import Level

from data.classes.Hero import Hero

#hero
hero_class = 'bercerk'

screen_info = [screen, screen_scale, screen_size]

while running:
    # Меню
    if in_menu:
        menu.draw(screen)
        if menu.player_action_check():
            in_menu = False
            in_level_passing = True
            # Go to 1st level, create a player
            level_passing = Level(current_level, screen_info)
            player = Hero(hero_class, screen_info)
    elif in_level_passing:

        # If player goes on next level
        res = level_passing.draw(screen_info)
        if (res == 1):
            level_passing = Level(current_level, screen_scale)
            current_level += 1

        player.draw_hero()

    # Updating display, control fps
    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if keyboard.is_pressed('q'):
        running = False
