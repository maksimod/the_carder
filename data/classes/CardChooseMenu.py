import pygame
import random

from data.classes.constructor.Elements import Img, ImgButton

from data import MusicPlayer

from data.global_vars import deck, hero

from time import sleep


import cv2
import numpy as np
# img1 = cv2.imread('data/images/cards/bercerk/attack.png')
# img2 = np.uint8(np.double(img1) + 15)
# cv2.imshow("frame",img1)
# cv2.imshow("frame2",img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# sleep(3)

class CardChooseMenu:
    def __init__(self, screen_info):
        pass

        hero_class = hero.hero_class

        self.screen_info = screen_info
        screen, screen_scale, screen_size = screen_info

        self.next_level = False
        self.text_size_scale = 1 * screen_scale

        self.screen_size = screen_size
        self.h = self.screen_size[1]
        self.w = self.screen_size[0]

        # Surfaces
        self.background = Img(self.screen_info, 'data/images/elements/class_choose.png')

        button_scale = 0.5715 * screen_scale
        # bp = (60, 300)
        # tc = [random.randrange(256 - 50), random.randrange(256 - 50), random.randrange(256 - 50)]

        #chose 3 (card_choose number) random cards:
        card1_choice = random.choice(deck.get_cards_depend_hero_class[hero_class])
        card2_choice = random.choice(deck.get_cards_depend_hero_class[hero_class])
        card3_choice = random.choice(deck.get_cards_depend_hero_class[hero_class])

        card_img1 = deck.cards_view[card1_choice][-1]
        card_img2 = deck.cards_view[card2_choice][-1]
        card_img3 = deck.cards_view[card3_choice][-1]


        card1_src = card_img1, np.uint8(np.double(cv2.imread(card_img1)) + 15)
        card2_src = card_img2, np.uint8(np.double(cv2.imread(card_img2)) + 15)
        card3_src = card_img3, np.uint8(np.double(cv2.imread(card_img3)) + 15)

        y_k = 1.47
        self.card1 = ImgButton(screen_info,card1_src, (0, self.h//y_k), button_scale)
        self.card2 = ImgButton(screen_info, card2_src, (self.card1.get_w(), self.h // y_k), button_scale)
        self.card3 = ImgButton(screen_info, card3_src, (self.card1.get_w()*2, self.h // y_k), button_scale)
        # self.princess = ImgButton(screen_info, princess_src, (self.bercerk.get_w()*3, self.h // y_k), button_scale)

        # Actions
        # self.create_clouds()
        MusicPlayer.play('data/music/CardChoose.mp3')

    def mouse_check(self):
        if self.bercerk.draw_check_click():
            hero.hero_class = 'bercerk'
            self.next_level = True
            MusicPlayer.stop()
            return True
        if self.isolda.draw_check_click():
            hero.hero_class = 'isolda'
            self.next_level = True
            MusicPlayer.stop()
            return True
        if self.joker.draw_check_click():
            hero.hero_class = 'joker'
            self.next_level = True
            MusicPlayer.stop()
            return True
        if self.princess.draw_check_click():
            hero.hero_class = 'princess'
            self.next_level = True
            MusicPlayer.stop()
            return True

    def player_action_check(self):
        if self.next_level: return True

    def draw(self, screen):
        self.background.draw(screen,(0, 0))
        # self.draw_clouds(screen)
        self.mouse_check()
        # The carder text