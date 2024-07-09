# from data.classes.levels.level1 import Level1
from data.classes.Enemy import Enemy
from data.classes.Hero import Hero

from data.global_vars import enemies
from data.global_vars import levels

import pygame
from random import *

class Level:
    def __init__(self,current_level, screen_scale):
        # self.background = self.enemy_type = self.ways = None
        self.current_level = current_level
        # Chose current background and enemy with random module
        current_level_parameters = levels.LEVELS[current_level]
        background_path = current_level_parameters[0][randint(0, len(current_level_parameters[0])-1)]
        self.music = current_level_parameters[1][randint(0, len(current_level_parameters[1])-1)]


        #Creating serfaces to make opportunity to put them on the screen
        self.background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(self.background, (
            self.background.get_size()[0] * screen_scale, self.background.get_size()[1] * screen_scale))

        #Start music
        pygame.mixer_music.load(self.music)
        pygame.mixer_music.play(-1)

    def check_win(self,screen_size):
        self.h = screen_size[1]
        self.w = screen_size[0]
        mp = pygame.mouse.get_pos()
        # print(mp[0],mp[1])
        if mp[0]<50 and mp[1]<50:
            # print('OK!')
            return 1
        elif mp[0]>self.w-50 and mp[1]>self.h-50:
            return 0
        else:
            return -1


    #This function draw player, cards, background and enemy every frame
    def draw(self, screen_info):
        screen = screen_info[0]
        screen_scale = screen_info[1]
        screen_size = screen_info[2]
        screen.blit(self.background, (0, 0))