import pygame
import random

from data.classes.constructor.Elements import Img, Text, ImgButton, TextButton

from data import MusicPlayer

from data.global_vars.screen_info import *

class Menu:
    # Menu_variables
    def __init__(self):
        bercerk_src = 'data/images/elements/hero_cards/bercerk.png', 'data/images/elements/hero_cards/bercerk_light.png'
        # isolda_src = 'data/images/elements/hero_cards/isolda.png', 'data/images/elements/hero_cards/isolda_light.png'
        # joker_src = 'data/images/elements/hero_cards/Joker.png', 'data/images/elements/hero_cards/Joker_light.png'
        # princess_src = 'data/images/elements/hero_cards/the_princess.png', 'data/images/elements/hero_cards/the_princess_light.png'
        y_k = 1.47
        self.bercerk = ImgButton(bercerk_src, (200, 200), 1)
        # self.isolda = ImgButton(screen_info, isolda_src, (self.bercerk.get_w(), self.h // y_k), button_scale)
        # self.joker = ImgButton(screen_info, joker_src, (self.bercerk.get_w()*2, self.h // y_k), button_scale)
        # self.princess = ImgButton(screen_info, princess_src, (self.bercerk.get_w()*3, self.h // y_k), button_scale)

        self.next_level = False
        self.text_size_scale = 1 * screen_scale

        self.screen_size = screen_size
        self.h = self.screen_size[1]
        self.w = self.screen_size[0]

        # Surfaces
        self.background = Img('data/images/menu/back.png')

        button_text_scale = 0.6 * screen_scale
        bp = (60, 300)
        tc = [random.randrange(256 - 50), random.randrange(256 - 50), random.randrange(256 - 50)]
        buttons_text_info = [
            ("New game", button_text_scale, tc),
            ("Continue", button_text_scale, tc),
            ("Settings", button_text_scale, tc),
            ("Exit", button_text_scale, tc)
        ]
        self.the_carder = Text("The carder", k=self.text_size_scale, color=tc)
        self.new_game = TextButton(buttons_text_info[0], bp, 0)
        self.contin = TextButton(buttons_text_info[1], (bp[0], bp[1] + self.new_game.get_h()), 1)
        self.settings = TextButton(buttons_text_info[2], (bp[0], bp[1] + self.new_game.get_h() * 2), 2)
        self.exit = TextButton(buttons_text_info[3], (bp[0], bp[1] + self.new_game.get_h() * 3), 3)

        # Actions
        self.create_clouds()
        # MusicPlayer.play('data/music/lev0.mp3')

    # Menu_clouds
    def create_clouds(self):
        self.cloud1 = Img('data/images\\menu\\cloud.png', k=0.25)
        self.cloud2 = Img('data/images\\menu\\cloud.png', k=0.25)
        self.cloud_h1 = random.randrange(self.h - self.cloud1.get_height())
        self.last_cloud_h1 = self.cloud_h1
        self.is_collide1 = True
        self.cloud_h2 = random.randrange(self.h - self.cloud2.get_height())
        self.last_cloud_h2 = self.cloud_h2
        self.is_collide2 = True
        self.cloud_x1 = random.randint(0, self.w)
        self.cloud_speed_x1 = random.random() * 2 + 0.3
        self.cloud_x2 = random.randint(0, self.w)
        self.cloud_speed_x2 = random.random() * 2 + 0.3

    # this function draw menu buttons

    def draw_clouds(self):
        offset = 90

        self.cloud1.draw((self.cloud_x1, self.cloud_h1))
        self.cloud2.draw((self.cloud_x2, self.cloud_h2))

        self.cloud_x1 += self.cloud_speed_x1
        self.cloud_x2 += self.cloud_speed_x2

        # If cloud go out of the screen it will be teleported to another side and change its speed and position
        if self.cloud_x1 > self.h + self.cloud1.get_width() + offset:
            self.cloud_x1 = -self.cloud1.get_width() - offset
            self.cloud_h1 = random.randrange(self.h - self.cloud1.get_height())
            self.cloud_speed_x1 = random.random() * 2 + 0.3
        if self.cloud_x2 > self.h + self.cloud1.get_width() + offset:
            self.cloud_x2 = -self.cloud1.get_width() - offset
            self.cloud_h2 = random.randrange(self.h - self.cloud1.get_height())
            self.cloud_speed_x2 = random.random() * 2 + 0.3

    def mouse_check(self):
        if self.new_game.draw_check_click():
            self.next_level = True
            MusicPlayer.stop()
            return True
        if self.contin.draw_check_click():
            pass
        if self.settings.draw_check_click():
            pass
        if self.exit.draw_check_click():
            pygame.quit()
            exit()

    def player_action_check(self):
        if self.next_level: return True

    def draw(self):
        if self.bercerk.draw_check_click():
            pass

        self.background.draw((0, 0))
        self.draw_clouds()
        self.mouse_check()
        # The carder text

        self.the_carder.draw((self.w // 2 - self.the_carder.get_width() // 2, -self.the_carder.get_width() // 16))