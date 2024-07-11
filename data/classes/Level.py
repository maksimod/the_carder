from data.classes.Enemy import Enemy
from data.classes.Hero import Hero

from data.global_vars import enemies
from data.global_vars import levels

from data.classes.constructor.Elements import TextButton, ImgButton, CText, Img
from data import MusicPlayer

from data.classes.Deck import Deck

from data.global_vars import hero, deck

import pygame
from random import *

class Level:
    def __init__(self,current_level, screen_info):
        screen = screen_info[0]
        screen_scale = screen_info[1]
        screen_size = screen_info[2]

        w,h = screen_size
        self.w,self.h = w,h

        # self.background = self.enemy_type = self.ways = None
        self.current_level = current_level
        # Chose current background and enemy with random module
        current_level_parameters = levels.LEVELS[current_level]
        background_path = current_level_parameters[0][randint(0, len(current_level_parameters[0])-1)]
        self.music = current_level_parameters[1][randint(0, len(current_level_parameters[1])-1)]

        get_enemies_by_level = enemies.level_enemy_types[current_level]
        self.enemy_name = get_enemies_by_level[randint(0, len(get_enemies_by_level)-1)]
        self.current_enemy = Enemy(self.enemy_name, screen_info)

        self.player = Hero(hero.hero_class, screen_info)


        #Creating serfaces to make opportunity to put them on the screen
        self.background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(self.background, (
            self.background.get_size()[0] * screen_scale, self.background.get_size()[1] * screen_scale))


        next_turn_src = 'data/images/elements/buttons/next_turn.png','data/images/elements/buttons/next_turn_light.png'
        self.next_turn = ImgButton(screen_info,next_turn_src,(w-200,h-250), k=0.2)

        input_src = 'data/images/elements/deck/input.png','data/images/elements/deck/input_light.png'
        self.inp_pos = (100,h-100)
        self.input = ImgButton(screen_info,input_src,self.inp_pos, k=0.2)
        # self.input_text = CText(str(deck.cards_input),k=0.4)

        output_src = 'data/images/elements/deck/output.png', 'data/images/elements/deck/output_light.png'
        self.out_pos = (w-200, h - 100)
        self.output = ImgButton(screen_info, output_src, self.out_pos, k=0.2)
        # self.output_text = CText(str(deck.cards_output), k=0.4)

        #Start music
        MusicPlayer.play(self.music)

        #create a deck
        self.playerDeck = Deck(screen_info, self.current_enemy, self.player)

    def check_win(self):
        # self.h = screen_size[1]
        # self.w = screen_size[0]
        mp = pygame.mouse.get_pos()
        if mp[0]<50 and mp[1]<50:
            return 1
        elif mp[0]>self.w-50 and mp[1]>self.h-50:
            return 0
        else:
            return -1


    #This function draw player, cards, background and enemy every frame
    def draw(self, screen_info):
        screen = screen_info[0]
        screen.blit(self.background, (0, 0))

        if (self.current_enemy.draw_enemy()): return 'WIN'
        if self.player.update_hero()=='DEAD': return 'DEFEAT'

        self.playerDeck.draw()

        if self.next_turn.draw_check_click():
            self.current_enemy.make_turn()
            self.player.make_turn()
            self.playerDeck.take_cards()
            pass
        if self.input.draw_check_click():
            pass
        if self.output.draw_check_click():
            pass
            # print("OK!")
        self.input_text = CText(str(deck.cards_input), k=0.4)
        self.output_text = CText(str(deck.cards_output), k=0.4)
        self.input_text.draw(screen, (self.inp_pos[0]+self.input.get_w()//4,self.inp_pos[1]+10))
        self.output_text.draw(screen, (self.out_pos[0] + self.input.get_w() // 4, self.out_pos[1] + 10))