import pygame
import random

from data.classes.constructor.Elements import Img, ImgButton
from data.global_vars.screen_info import *
from data import MusicPlayer

from data.global_vars import deck, hero

from data.classes.Deck import Card
class CardChooseMenu:
    def __init__(self):
        pass

        hero_class = hero.hero_class

        self.screen_info = screen_info
        screen, screen_scale, screen_size = screen_info

        self.next_level = False
        self.text_size_scale = 1 * screen_scale

        self.screen_size = screen_size
        self.screen_scale = screen_scale
        self.h = self.screen_size[1]
        self.w = self.screen_size[0]

        # Surfaces
        self.background = Img('data/images/elements/class_choose.png')

        button_scale = 0.5715 * screen_scale

        #chose 3 (card_choose number) random cards:
        card1_choice = random.choice(deck.get_cards_depend_hero_class[hero_class])
        card2_choice = random.choice(deck.get_cards_depend_hero_class[hero_class])
        card3_choice = random.choice(deck.get_cards_depend_hero_class[hero_class])

        self.card_img1 = deck.cards_view[card1_choice][-1][(deck.cards_view[card1_choice][-1].rfind('/')+1):(deck.cards_view[card1_choice][-1].rfind('.'))]
        self.card_img2 = deck.cards_view[card2_choice][-1][(deck.cards_view[card2_choice][-1].rfind('/')+1):(deck.cards_view[card2_choice][-1].rfind('.'))]
        self.card_img3 = deck.cards_view[card3_choice][-1][(deck.cards_view[card3_choice][-1].rfind('/')+1):(deck.cards_view[card3_choice][-1].rfind('.'))]

        self.card1 = Card(self.card_img1, 0.6, 0, card_chose=True)
        self.card2 = Card(self.card_img2, 0.6, 1, card_chose=True)
        self.card3 = Card(self.card_img3, 0.6, 2, card_chose=True)

        # Actions
        # self.create_clouds()
        # MusicPlayer.play('data/music/CardChoose.mp3')

        self.card_x_offset = 100*self.screen_scale
    def mouse_check(self):
        kx = 200
        if deck.focused_cards[0]:
            if self.card2.live((kx*self.screen_scale+self.card1.get_width()+self.card_x_offset, 290*self.screen_scale)):
                if self.card_img2 in deck.current_deck.keys():
                    deck.current_deck[self.card_img2]+=1
                else:
                    deck.current_deck[self.card_img2]=1
                return True
            if self.card3.live((kx*self.screen_scale+2*(self.card1.get_width()+self.card_x_offset), 290*self.screen_scale)):
                if self.card_img3 in deck.current_deck.keys():
                    deck.current_deck[self.card_img3]+=1
                else:
                    deck.current_deck[self.card_img3]=1
                return True
            if self.card1.live((kx*self.screen_scale,290*self.screen_scale)):
                if self.card_img1 in deck.current_deck.keys(): deck.current_deck[self.card_img1]+=1
                else: deck.current_deck[self.card_img1]=1
                return True
        elif deck.focused_cards[1]:
            if self.card1.live((kx*self.screen_scale,290*self.screen_scale)):
                if self.card_img1 in deck.current_deck.keys():
                    deck.current_deck[self.card_img1]+=1
                else:
                    deck.current_deck[self.card_img1]=1
                return True
            if self.card3.live((kx*self.screen_scale+2*(self.card1.get_width()+self.card_x_offset), 290*self.screen_scale)):
                if self.card_img3 in deck.current_deck.keys():
                    deck.current_deck[self.card_img3]+=1
                else:
                    deck.current_deck[self.card_img3]=1
                return True
            if self.card2.live((kx*self.screen_scale+self.card1.get_width()+self.card_x_offset, 290*self.screen_scale)):
                if self.card_img2 in deck.current_deck.keys(): deck.current_deck[self.card_img2]+=1
                else: deck.current_deck[self.card_img2]=1
                return True
        else:
            if self.card1.live((kx*self.screen_scale,290*self.screen_scale)):
                if self.card_img1 in deck.current_deck.keys():
                    deck.current_deck[self.card_img1]+=1
                else:
                    deck.current_deck[self.card_img1]=1
                return True
            if self.card2.live((kx*self.screen_scale+self.card1.get_width()+self.card_x_offset, 290*self.screen_scale)):
                if self.card_img2 in deck.current_deck.keys():
                    deck.current_deck[self.card_img2]+=1
                else:
                    deck.current_deck[self.card_img2]=1
                return True
            if self.card3.live((kx*self.screen_scale+2*(self.card1.get_width()+self.card_x_offset), 290*self.screen_scale)):
                if self.card_img3 in deck.current_deck.keys(): deck.current_deck[self.card_img3]+=1
                else: deck.current_deck[self.card_img3]=1
                return True
    
    def draw(self):
        self.background.draw((0, 0))
        if self.mouse_check():
            return True
        # The carder text