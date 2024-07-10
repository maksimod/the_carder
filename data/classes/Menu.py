import pygame
import random

from data.classes.constructor.Button import Button

class Menu:
    # Menu_variables
    def __init__(self, screen, screen_scale, screen_size):
        self.next_level = False
        self.back1_image_name = 'data/images/menu/back.png'
        self.text_size_scale = 1 * screen_scale
        self.menu_text_the_carder = pygame.font.Font('data/text_fonts/menu_font.otf', int(150 * self.text_size_scale))
        # Surfaces
        ctc = [random.randrange(256 - 50), random.randrange(256 - 50), random.randrange(256 - 50)]
        self.menu_text_the_carder_surface = self.menu_text_the_carder.render('The Carder', False, ctc)
        self.menu_surface = pygame.image.load('data/images\\menu\\back.png')
        self.menu_surface = pygame.transform.scale(self.menu_surface, (
            self.menu_surface.get_size()[0] * screen_scale, self.menu_surface.get_size()[1] * screen_scale))
        self.menu_cloud_surface = pygame.image.load('data/images\\menu\\cloud.png')
        self.menu_cloud_surface = pygame.transform.scale(self.menu_cloud_surface, (
            self.menu_cloud_surface.get_size()[0] * screen_scale // 4,
            self.menu_surface.get_size()[1] * screen_scale // 3))
        self.background1_surface = pygame.image.load(self.back1_image_name)
        self.background1_surface = pygame.transform.scale(self.background1_surface, (
            self.background1_surface.get_size()[0] * screen_scale,
            self.background1_surface.get_size()[1] * screen_scale))
        self.screen_size = screen_size
        self.h = self.screen_size[1]
        self.w = self.screen_size[0]

        button_text_scale = 0.6*screen_scale
        bp = (60,300)
        tc = [random.randrange(256 - 50), random.randrange(256 - 50), random.randrange(256 - 50)]
        buttons_text_info = [
            ("New game", button_text_scale, tc),
            ("Continue", button_text_scale, tc),
            ("Settings", button_text_scale, tc),
            ("Exit", button_text_scale, tc)
        ]
        self.new_game = Button(buttons_text_info[0], bp, screen)
        self.contin = Button(buttons_text_info[1], (bp[0], bp[1]+self.new_game.get_h()), screen)
        self.settings = Button(buttons_text_info[2], (bp[0], bp[1]+self.new_game.get_h()*2), screen)
        self.exit = Button(buttons_text_info[3], (bp[0], bp[1]+self.new_game.get_h()*3), screen)

        # Actions
        self.create_clouds()
        pygame.mixer_music.load('data/music/lev0.mp3')
        pygame.mixer_music.play(-1)

    # Menu_clouds
    def create_clouds(self):
        self.cloud_h1 = random.randrange(self.h - self.menu_cloud_surface.get_size()[1])
        self.last_cloud_h1 = self.cloud_h1
        self.is_collide1 = True
        self.cloud_h2 = random.randrange(self.h - self.menu_cloud_surface.get_size()[1])
        self.last_cloud_h2 = self.cloud_h2
        self.is_collide2 = True
        self.cloud_x1 = random.randint(0, self.w)
        self.cloud_speed_x1 = random.random() * 2 + 0.3
        self.cloud_x2 = random.randint(0, self.w)
        self.cloud_speed_x2 = random.random() * 2 + 0.3

    # this function draw menu buttons

    def draw_clouds(self, screen):
        offset = 90
        screen.blit(self.menu_cloud_surface, (self.cloud_x1, self.cloud_h1))
        screen.blit(self.menu_cloud_surface, (self.cloud_x2, self.cloud_h2))
        self.cloud_x1 += self.cloud_speed_x1
        self.cloud_x2 += self.cloud_speed_x2
        if self.cloud_x1 > self.h + self.menu_cloud_surface.get_size()[0] + offset:
            self.cloud_x1 = -self.menu_cloud_surface.get_size()[0] - offset
            self.cloud_h1 = random.randrange(self.h - self.menu_cloud_surface.get_size()[1])
            self.cloud_speed_x1 = random.random() * 2 + 0.3
        if self.cloud_x2 > self.h + self.menu_cloud_surface.get_size()[0] + offset:
            self.cloud_x2 = -self.menu_cloud_surface.get_size()[0] - offset
            self.cloud_h2 = random.randrange(self.h - self.menu_cloud_surface.get_size()[1])
            self.cloud_speed_x2 = random.random() * 2 + 0.3

    def mouse_check(self):
        if self.new_game.draw_check_click():
            self.next_level = True
            pygame.mixer_music.stop()
        elif self.contin.draw_check_click():
            pass
        elif self.settings.draw_check_click():
            pass
        elif self.exit.draw_check_click():
            pygame.quit()
            exit()

    def player_action_check(self):
        if self.next_level:
            return True
        return False

    def draw(self, screen):
        screen.blit(self.background1_surface, (0, 0))
        self.draw_clouds(screen)
        self.mouse_check()

        # The carder text
        screen.blit(self.menu_text_the_carder_surface, (
        (self.w // 2) - self.menu_text_the_carder_surface.get_size()[0] // 2,
        -self.menu_text_the_carder_surface.get_size()[0] // 16))