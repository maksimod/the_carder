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
from data.classes.Deck import Card
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

        # card_img1 = deck.cards_view[card1_choice][-1]
        # card_img2 = deck.cards_view[card2_choice][-1]
        # card_img3 = deck.cards_view[card3_choice][-1]

        self.card_img1 = deck.cards_view[card1_choice][-1][(deck.cards_view[card1_choice][-1].rfind('/')+1):(deck.cards_view[card1_choice][-1].rfind('.'))]
        self.card_img2 = deck.cards_view[card2_choice][-1][(deck.cards_view[card2_choice][-1].rfind('/')+1):(deck.cards_view[card2_choice][-1].rfind('.'))]
        self.card_img3 = deck.cards_view[card3_choice][-1][(deck.cards_view[card3_choice][-1].rfind('/')+1):(deck.cards_view[card3_choice][-1].rfind('.'))]

        self.card1 = Card(screen_info, self.card_img1, 0.8, 1, card_chose=True)
        self.card2 = Card(screen_info, self.card_img2, 0.8, 1, card_chose=True)
        self.card3 = Card(screen_info, self.card_img3, 0.8, 1, card_chose=True)

        # Actions
        # self.create_clouds()
        # MusicPlayer.play('data/music/CardChoose.mp3')

        self.card_x_offset = 200
    def mouse_check(self):
        if self.card1.live(self.screen_info[0], (200,290)):
            if self.card_img1 in deck.current_deck.keys(): deck.current_deck[self.card_img1]+=1
            else: deck.current_deck[self.card_img1]=1
            return True
        if self.card2.live(self.screen_info[0], (200+self.card1.get_width()+self.card_x_offset, 290)):
            if self.card_img2 in deck.current_deck.keys(): deck.current_deck[self.card_img2]+=1
            else: deck.current_deck[self.card_img2]=1
            return True
        if self.card3.live(self.screen_info[0], (200+2*(self.card1.get_width()+self.card_x_offset), 290)):
            if self.card_img3 in deck.current_deck.keys(): deck.current_deck[self.card_img3]+=1
            else: deck.current_deck[self.card_img3]=1
            return True

    def draw(self, screen):
        self.background.draw(screen,(0, 0))
        # self.draw_clouds(screen)
        if self.mouse_check():
            print("RET")
            return True
        # The carder text