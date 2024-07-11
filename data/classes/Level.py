from data.classes.Enemy import Enemy

from data.global_vars import enemies
from data.global_vars import levels

from data.classes.constructor.Elements import TextButton, ImgButton, Text, Img
from data import MusicPlayer

from data.classes.Deck import Deck

import pygame
from random import *

class Level:
    def __init__(self,current_level, screen_info):
        screen = screen_info[0]
        screen_scale = screen_info[1]
        screen_size = screen_info[2]

        w,h = screen_size

        # self.background = self.enemy_type = self.ways = None
        self.current_level = current_level
        # Chose current background and enemy with random module
        current_level_parameters = levels.LEVELS[current_level]
        background_path = current_level_parameters[0][randint(0, len(current_level_parameters[0])-1)]
        self.music = current_level_parameters[1][randint(0, len(current_level_parameters[1])-1)]

        get_enemies_by_level = enemies.level_enemy_types[current_level]
        self.enemy_name = get_enemies_by_level[randint(0, len(get_enemies_by_level)-1)]
        self.current_enemy = Enemy(self.enemy_name, screen_info)


        #Creating serfaces to make opportunity to put them on the screen
        self.background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(self.background, (
            self.background.get_size()[0] * screen_scale, self.background.get_size()[1] * screen_scale))


        src = 'data/images/elements/buttons/next_turn.png','data/images/elements/buttons/next_turn_light.png'
        self.next_turn = ImgButton(screen_info,src,(w-300,h-300), k=0.2)


        #Start music
        MusicPlayer.play(self.music)

        #create a deck
        self.playerDeck = Deck(screen_info)

    def check_win(self,screen_size):
        self.h = screen_size[1]
        self.w = screen_size[0]
        mp = pygame.mouse.get_pos()
        if mp[0]<50 and mp[1]<50:
            return 1
        elif mp[0]>self.w-50 and mp[1]>self.h-50:
            return 0
        else:
            return -1


    #This function draw player, cards, background and enemy every frame
    def draw(self, screen_info, player):
        screen = screen_info[0]
        # screen_scale = screen_info[1]
        # screen_size = screen_info[2]
        screen.blit(self.background, (0, 0))
        self.current_enemy.draw_enemy()
        player.draw_hero()

        self.playerDeck.draw()


        if self.next_turn.draw_check_click():
            pass
            # print("OK!")
