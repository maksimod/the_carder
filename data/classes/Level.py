from data.classes.Enemy import Enemies
from data.classes.Hero import Hero

from data.global_vars import levels

from data.classes.constructor.Elements import ImgButton, CText
from data import MusicPlayer

from data.classes.Deck import Deck

from data.global_vars import hero, deck, enemies

import pygame
from random import *

from data.classes.Deck import Card

from data.global_vars.screen_info import *

class Level:
    def __init__(self,current_level):
        self.input_was_pressed = False
        self.output_was_pressed = False
        self.input_cards = []
        self.output_cards = []

        w,h = screen_size
        self.w,self.h = w,h

        self.current_level = current_level
        # Chose current background and enemy with random module
        current_level_parameters = levels.LEVELS[current_level]
        rand_level_back = randint(0, len(current_level_parameters[0])-1)
        if levels.level_pass_line is not None:
            rand_level_back = levels.level_pass_line
        else:
            levels.level_pass_line = rand_level_back
        background_path = current_level_parameters[0][rand_level_back]
        self.music = current_level_parameters[1][randint(0, len(current_level_parameters[1])-1)]

        get_enemies_by_level = enemies.level_enemy_types[current_level]
        self.enemy_name = get_enemies_by_level[randint(0, len(get_enemies_by_level)-1)]
        self.current_enemy = Enemies(self.enemy_name)

        self.player = Hero(hero.hero_class)

        #Creating serfaces to make opportunity to put them on the screen
        self.background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(self.background, (
            self.background.get_size()[0] * screen_scale, self.background.get_size()[1] * screen_scale))

        next_turn_src = 'data/images/elements/buttons/next_turn.png','data/images/elements/buttons/next_turn_light.png'
        self.next_turn = ImgButton(next_turn_src,(w-150*screen_scale,h-150*screen_scale), k=0.2)

        input_src = 'data/images/elements/deck/input.png','data/images/elements/deck/input_light.png'
        self.inp_pos = (75*screen_scale,h-50*screen_scale)
        self.input = ImgButton(input_src,self.inp_pos, k=0.2)

        output_src = 'data/images/elements/deck/output.png', 'data/images/elements/deck/output_light.png'
        self.out_pos = (w-150*screen_scale, h - 50*screen_scale)
        self.output = ImgButton(output_src, self.out_pos, k=0.2)

        #Start music
        # MusicPlayer.play(self.music)

        #create a deck
        self.playerDeck = Deck(self.current_enemy, self.player)

    def check_win(self):
        mp = pygame.mouse.get_pos()
        if mp[0]<50 and mp[1]<50:
            return 1
        elif mp[0]>self.w-50 and mp[1]>self.h-50:
            return 0
        else:
            return -1

    def draw(self):
        screen = screen_info[0]
        screen.blit(self.background, (0, 0))

        if self.next_turn.draw_check_click():
            # print(deck.hand_cards_col)
            deck.hand_cards_col = deck.hand_max_cards_col
            deck.focused_cards = [False for i in range(deck.hand_cards_col)]
            self.current_enemy.make_turn()
            self.player.make_turn()
            self.playerDeck.take_cards()
            pass
        if self.input.draw_check_click():
            self.input_was_pressed = True
        if self.output.draw_check_click():
            self.output_was_pressed = True

        if hero.hero[hero.hero_class][0][0]<=0:
            del self.playerDeck
            return 'DEFEAT'
        #If ALL enemies (not slaves) were dead:
        flag = True
        for el in self.current_enemy.get_names():
            if enemies.enemies[el][0][0]>0:
                flag = False
                break
        if flag:
            del self.playerDeck
            return 'WIN'

        self.current_enemy.draw_enemies()

        self.player.update_hero()


        self.playerDeck.draw()

        self.input_text = CText(str(deck.cards_input), k=0.2*screen_scale)
        self.output_text = CText(str(deck.cards_output), k=0.2*screen_scale)
        self.input_text.draw((self.inp_pos[0]+self.input.get_w()//4,self.inp_pos[1]+10))
        self.output_text.draw((self.out_pos[0] + self.input.get_w() // 4, self.out_pos[1] + 10))

        #if we want to see input our output cards
        if self.input_was_pressed:
            screen.fill((0, 100, 200))
            if pygame.mouse.get_pressed()[0]:
                self.input_was_pressed = False
            if self.input_cards:
                i = 0
                for el in self.input_cards:
                    max_str_cards = 8
                    if i < max_str_cards:
                        el.live((100*screen_scale + i * el.get_width() * 1.1, 50*screen_scale))
                    elif max_str_cards * 2 > i >= max_str_cards:
                        el.live((100*screen_scale + (i - max_str_cards) * el.get_width() * 1.1, 50*screen_scale + el.get_height() + 40*screen_scale))
                    else:
                        el.live((100*screen_scale + (i - max_str_cards * 2) * el.get_width() * 1.1, 50*screen_scale + 2 * (el.get_height() + 40*screen_scale)))
                    i += 1
            else:
                i = 0
                for el in deck.input:
                    self.input_cards.append(Card(el.collect_src_name(),0.4,i,just_show=True))
                    i+=1
                shuffle(self.input_cards)
        else: self.input_cards = []

        if self.output_was_pressed:
            screen.fill((0, 100, 200))
            if pygame.mouse.get_pressed()[0]:
                self.output_was_pressed = False
            if self.output_cards:
                i = 0
                for el in self.output_cards:
                    #max 5 cards in stroke
                    max_str_cards = 8
                    if i<max_str_cards:
                        el.live((100*screen_scale+i*el.get_width()*1.1,50*screen_scale))
                    elif max_str_cards*2>i>=max_str_cards:
                        el.live((100*screen_scale + (i - max_str_cards) * el.get_width() * 1.1, 50*screen_scale + el.get_height() + 40*screen_scale))
                    else:
                        el.live((100*screen_scale + (i-max_str_cards*2) * el.get_width() * 1.1, 50*screen_scale+ 2*(el.get_height()+40*screen_scale)))
                    i+=1
            else:
                i = 0
                for el in deck.output:
                    self.output_cards.append(Card(el.collect_src_name(),0.4,i,just_show=True))
                    i+=1
        else: self.output_cards = []