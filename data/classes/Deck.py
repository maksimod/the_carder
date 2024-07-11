import time
import keyboard

import pygame

from data.classes.constructor.Elements import Img

from data.global_vars import deck

from time import *
from random import shuffle


from data.classes.constructor.Elements import Surface

class Deck:

    def collect_deck(self):
        result = []
        for el in deck.current_deck.keys():
            for i in range(deck.current_deck[el]):
                #     cards_src.append(deck.cards_view[el][1])
                result.append(el)
        # print(result)

        # print(deck.current_deck.keys(), deck.current_deck.values())
        # sleep(999)
        return result


    def collect_src(self,deck_cards):
        src = []
        for el in deck_cards:
            src.append(deck.cards_view[el][1])
        # print(src)
        # sleep(99)
        print(src)
        # sleep(99)
        return src

    def __init__(self, screen_info):
        self.cards_col = deck.cards_col

        deck_cards = self.collect_deck()
        shuffle(deck_cards)
        print(deck_cards)
        # sleep(99)
        self.card_src = self.collect_src(deck_cards)

        k = 0.4
        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]
        self.screen_size = screen_info[2]

        self.cards = []
        for i in range(self.cards_col):
            self.cards.append(Card(screen_info, self.card_src[i], k, i))

            # card_surfaces.append('')
            # card_surfaces[-1] = Img(screen_info, card_src[i])
            # card_surfaces[-1].scale(card_surfaces[-1],k)

        # self.card_surfaces = card_surfaces

    def draw(self):
        cards = self.cards
        for  i in range(self.cards_col):
            cards[i].show(self.screen, (
            self.screen_size[0] // 2 - (cards[0].get_width() * self.cards_col) // 2 + i * cards[0].get_width(),
            self.screen_size[1] - cards[0].get_height()), self.card_src[i])



class Card(Surface):
    def __init__(self, screen_info, card_src, k, index):
        self.focus = False

        self.index = index

        # self.pos = pos
        self.was_pressed = False
        self.was_pressed_enter = False
        self.was_pressed_down = False
        self.was_pressed_up = False

        self.k = k
        self.surface = Img(screen_info, card_src)
        self.surface.scale(self.surface,k)

        self.big = Img(screen_info, card_src)
        self.big.scale(self.big, k*1.5)
    def show(self, screen, pos, card_src):
        self.screen = screen
        self.pos = pos
        self.screen = screen
        self.draw_check_click(card_src)

    @staticmethod
    def make_size(mode, surface, ex, src=None, txt=None, k=1.2, font='data/text_fonts/menu_font.otf', color=None):
        if type(surface) == Img:
            if mode == 'B':
                surface.scale(ex, k)
            elif mode == 'N':
                surface.loadImg(src)
                surface.scale(ex, 1)
        return surface

    def draw_check_click(self, card_src, hotkey=None):
        bws, bhs = self.surface.get_width(), self.surface.get_height() // 2
        bwb, bhb = self.big.get_width(), self.big.get_height() // 2
        mpx, mpy = pygame.mouse.get_pos()


        self.real_pos = [self.pos[0],self.pos[1]]

        #Check that at least one card is active
        flag = False
        for el in deck.focused_cards:
            if el:
                flag = True
                break
        if flag:
            if self.index<deck.current_active_card:
                self.real_pos[0] -= (bwb-bws)//2
            if self.index>deck.current_active_card:
                self.real_pos[0] += (bwb - bws) // 2

        pxs, pys = self.real_pos
        pxb, pyb = pxs-(bwb-bws)//2,self.screen.get_height() - bhb * 2

        if not self.focus:
            if (pxs <= mpx <= pxs + bws) and (pys <= mpy <= pys + bhs*2):
                self.focus = True
                deck.current_active_card = self.index
            else: self.focus = False
        else:
            if pygame.mouse.get_pressed()[0]:
                pxb, pyb = mpx-bwb//2, mpy-bhb
                self.was_pressed = True
            else:
                if self.was_pressed:
                    pxb, pyb = -1000,-1000
                    pxs, pys = -1000, -1000
            if (pxb <= mpx <= pxb + bwb) and (pyb <= mpy <= pyb + bhb * 2):
                deck.current_active_card = self.index
                self.focus = True
            else: self.focus = False

        deck.focused_cards[self.index] = self.focus

        if self.focus: self.big.draw(self.screen, (pxb, pyb))
        else: self.surface.draw(self.screen, (pxs, pys))
