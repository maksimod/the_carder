import time
import keyboard
# from random import shuffle

import pygame

from data.classes.constructor.Elements import CardImg, CText

from data.global_vars import deck, hero, enemies

from time import *
from random import shuffle

from data.classes.constructor.Elements import Surface


class Deck:

    def __init__(self, screen_info, enemy, player):
        self.enemy,self.player = enemy,player

        if deck.hand_cards_col<=6:
            k = 0.4
        else:
            k = 0.4 - (deck.hand_cards_col-6)*0.03

        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]
        self.screen_size = screen_info[2]

        #convert card names to real cards!
        for i in range(len(deck.input)):
            deck.input[i] = Card(screen_info, deck.input[i], k, i)

        self.cards = []
        for i in range(deck.hand_cards_col):
            self.cards.append(deck.input[0])
            deck.input.pop(0)
            deck.cards_input-=1

    def take_cards(self):
        for i in range(len(self.cards)):
            deck.output.append(self.cards[0])
            del self.cards[0]
            deck.cards_output+=1

        for i in range(deck.hand_max_cards_col):
            if deck.input:
                self.cards.append(deck.input[0])
                deck.input.pop(0)
                deck.cards_input-=1
            else:
                deck.input = deck.output
                deck.output = []
                deck.cards_output = 0
                deck.cards_input = len(deck.input)
                shuffle(deck.input)
                self.cards.append(deck.input[0])
                deck.input.pop(0)
                deck.cards_input-=1

        deck.hand_cards_col = deck.hand_max_cards_col

        for i in range(len(self.cards)):
            self.cards[i].set_index(i)

    def play_card(self, src, card):
        cost = deck.cards[src][0]

        #Check for elements and make actions
        for action in deck.cards[src][1:]:
            if action[0] == 'A':
                #ATTACK ENEMY
                if action[1] == 'A':
                    attack = int(action[2:])
                    if enemies.enemies[self.enemy.get_type()][0][1] <= 0:
                        enemies.enemies[self.enemy.get_type()][0][0] -= attack
                    else:
                        if enemies.enemies[self.enemy.get_type()][0][1] - attack >= 0:
                            enemies.enemies[self.enemy.get_type()][0][1] -= attack
                        else:
                            attack -= enemies.enemies[self.enemy.get_type()][0][1]
                            enemies.enemies[self.enemy.get_type()][0][1] = 0
                            enemies.enemies[self.enemy.get_type()][0][0] -= attack
                # elif
            elif action[0] == 'P':
                if action[1] == 'D':
                    defence = int(action[2:])
                    hero.hero[hero.hero_class][0][1] += defence
            else:
                raise NameError('You did not add E support already')

        hero.hero[hero.hero_class][0][3] -= cost

        deck.output.append(card)
        deck.cards_output+=1

        return True

    def draw(self):
        cards = self.cards
        for i in range(deck.hand_cards_col):
            card_pos_x = self.screen_size[0] // 2 - (cards[0].get_width() * deck.hand_cards_col) // 2 + i * cards[0].get_width()
            card_pos_y = self.screen_size[1] - cards[0].get_height()
            if cards[i].live(self.screen, (card_pos_x,card_pos_y)) == True:
                if self.play_card(cards[i].get_card(), cards[i]):
                    del cards[i]
                    deck.hand_cards_col -= 1
                    break
                # self.play_card(cards[i].get_card())


class Card(Surface):

    def set_index(self,index):
        self.index = index

    def get_card(self):
        return self.card_src

    @staticmethod
    def collect_src(src):
        return deck.cards_view[src][1]

    def __init__(self, screen_info, card_src, k, index):
        self.focus = False
        self.big_card_k = 1.5

        self.index = index

        # self.pos = pos
        self.are_pressed = False
        self.was_pressed = False
        self.was_pressed_enter = False
        self.was_pressed_down = False
        self.was_pressed_up = False

        self.card_src = card_src


        img = self.collect_src(card_src)
        default_src = 'data/images/cards/'+hero.hero_class+'/default.png'

        self.k = k
        self.surface = CardImg(screen_info, default_src,img)
        self.surface.scale(self.surface, k)

        self.big = CardImg(screen_info, default_src, img)
        self.big.scale(self.big, k * self.big_card_k)

    @staticmethod
    def transfer_description(description, number):
        res = []
        last_i = 0
        for i in range(1, len(description)):
            if i % number == 0:
                res.append(description[last_i:i])
                last_i = i
        res.append(description[last_i:])
        return res

    def draw_card_states(self):

        cost = str(deck.cards[self.card_src][0])
        self.cost = cost
        k, big_card_k = self.k, self.big_card_k
        description = deck.cards_view[self.card_src][0]

        descs = self.transfer_description(description, 13)

        cost_k = 0.6
        title_key = 0.5
        description_k = 0.5

        cost_text, f_cost_text = CText(cost, k=k * cost_k), CText(cost, k=k * cost_k * big_card_k)

        title = self.card_src
        title_text, f_title_text = CText(title, k=k * title_key), CText(title, k=k * title_key * big_card_k)

        descs_texts = []
        f_descs_texts = []
        for el in descs:
            descs_texts.append(CText(el, k=description_k * k))
            f_descs_texts.append(CText(el, k=description_k * k * big_card_k))

        # description, f_description = CText(description, k=description_k * k), CText(description, k=description_k * k * big_card_k)
        if not self.focus:
            cost_pos = (self.real_pos[0] + cost_text.get_width() // 2, self.real_pos[1] + cost_text.get_height() // 6)
            cost_text.draw(self.screen, cost_pos)

            title_pos = (self.real_pos[0]+self.surface.get_width()//2 - title_text.get_width() // 2, self.real_pos[1] + title_text.get_height() // 2)
            title_text.draw(self.screen, title_pos)

            description_pos = (self.real_pos[0] + self.bws // 8, self.real_pos[1] + self.bhs // 0.85)
            counter = 0
            for item in descs_texts:
                item.draw(self.screen, (description_pos[0], description_pos[1] + item.get_height() * counter))
                counter += 1
        else:
            f_cost_pos = (self.pxb + f_cost_text.get_width() // 2, self.pyb + f_cost_text.get_height() // 6)
            f_cost_text.draw(self.screen, f_cost_pos)

            f_title_pos = (self.pxb+self.big.get_width()//2-f_title_text.get_width()//2, self.pyb + f_title_text.get_height() // 2)
            f_title_text.draw(self.screen, f_title_pos)

            f_description_pos = (self.pxb + self.bwb//10, self.pyb + self.bhb // 0.85)
            counter = 0
            for item in f_descs_texts:
                item.draw(self.screen, (f_description_pos[0], f_description_pos[1] + item.get_height() * counter))
                counter += 1

    def live(self, screen, pos):
        self.screen = screen
        self.pos = pos
        self.screen = screen
        if self.draw_check_click() == 'Play':
            return True
        self.draw_card_states()

    @staticmethod
    def make_size(mode, surface, ex, src=None, txt=None, k=1.2, font='data/text_fonts/menu_font.otf', color=None):
        if type(surface) == Img:
            if mode == 'B':
                surface.scale(ex, k)
            elif mode == 'N':
                surface.loadImg(src)
                surface.scale(ex, 1)
        return surface

    def draw_check_click(self, hotkey=None):
        bws, bhs = self.surface.get_width(), self.surface.get_height() // 2
        bwb, bhb = self.big.get_width(), self.big.get_height() // 2
        mpx, mpy = pygame.mouse.get_pos()

        self.real_pos = [self.pos[0], self.pos[1]]

        # Check that at least one card is active
        flag = False
        for el in deck.focused_cards:
            if el:
                flag = True
                break
        if flag:
            if self.index < deck.current_active_card:
                self.real_pos[0] -= (bwb - bws) // 2
            if self.index > deck.current_active_card:
                self.real_pos[0] += (bwb - bws) // 2

        pxs, pys = self.real_pos
        pxb, pyb = pxs - (bwb - bws) // 2, self.screen.get_height() - bhb * 2

        if not (self.are_pressed) and self.was_pressed:
            if mpy > pyb:
                self.are_pressed = False
                self.was_pressed = False
                deck.focus_freeze = None
            else:
                deck.focus_freeze = None
                #check that if card apply to one of all enemies it focused at one of the enemy
                flag = True
                for el in deck.cards[self.card_src][1:]:
                    if 'E' in el:
                        flag = False
                        break
                if flag:
                    if int(self.cost)<=hero.hero[hero.hero_class][0][3]:
                        return 'Play'

        self.are_pressed = False
        if not self.focus:
            if (pxs <= mpx <= pxs + bws) and (pys <= mpy <= pys + bhs * 2):
                if (deck.focus_freeze == self.index) or deck.focus_freeze is None:
                    self.focus = True
                    deck.current_active_card = self.index
            else:
                self.focus = False
        else:
            if (deck.focus_freeze == self.index) or deck.focus_freeze is None:
                if pygame.mouse.get_pressed()[0]:
                    pxb, pyb = mpx - bwb // 2, mpy - bhb
                    self.are_pressed = True
                    self.was_pressed = True
                    deck.focus_freeze = self.index
            if (pxb <= mpx <= pxb + bwb) and (pyb <= mpy <= pyb + bhb * 2):
                deck.current_active_card = self.index
                if (deck.focus_freeze == self.index) or deck.focus_freeze is None:
                    self.focus = True
            else:
                self.focus = False

        deck.focused_cards[self.index] = self.focus

        if self.focus:
            pass
            self.big.draw(self.screen, (pxb, pyb))
        else:
            pass
            self.surface.draw(self.screen, (pxs, pys))

        self.pxb, self.pyb = pxb, pyb
        self.bws, self.bhs, self.bwb, self.bhb = bws, bhs, bwb, bhb
