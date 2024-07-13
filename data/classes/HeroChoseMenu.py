import pygame
import random

from data.classes.constructor.Elements import Img, ImgButton

from data import MusicPlayer

from data.global_vars import hero

class HeroChoseMenu:
    # Menu_variables
    def __init__(self, screen_info):
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

        bercerk_src = 'data/images/elements/hero_cards/bercerk.png', 'data/images/elements/hero_cards/bercerk_light.png'
        isolda_src = 'data/images/elements/hero_cards/isolda.png', 'data/images/elements/hero_cards/isolda_light.png'
        joker_src = 'data/images/elements/hero_cards/Joker.png', 'data/images/elements/hero_cards/Joker_light.png'
        princess_src = 'data/images/elements/hero_cards/the_princess.png', 'data/images/elements/hero_cards/the_princess_light.png'
        y_k = 1.47
        self.bercerk = ImgButton(screen_info,bercerk_src, (0, self.h//y_k), button_scale)
        self.isolda = ImgButton(screen_info, isolda_src, (self.bercerk.get_w(), self.h // y_k), button_scale)
        self.joker = ImgButton(screen_info, joker_src, (self.bercerk.get_w()*2, self.h // y_k), button_scale)
        self.princess = ImgButton(screen_info, princess_src, (self.bercerk.get_w()*3, self.h // y_k), button_scale)

        # Actions
        # self.create_clouds()
        MusicPlayer.play('data/music/lev0.mp3')

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