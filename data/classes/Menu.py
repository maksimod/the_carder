import pygame
import random


class Menu:
    # Menu_variables
    def __init__(self, screen, screen_scale, screen_size):
        self.next_level = False
        self.back1_image_name = 'data/images/menu/back.png'
        self.menu_buttons_size = 100
        self.text_color = [random.randrange(256 - 50), random.randrange(256 - 50), random.randrange(256 - 50)]
        self.tc0 = self.text_color[0]
        self.tc1 = self.text_color[1]
        self.tc2 = self.text_color[2]
        self.text_size_scale = 1 * screen_scale
        self.menu_text_the_carder = pygame.font.Font('data/text_fonts/menu_font.otf', int(150 * self.text_size_scale))
        self.menu_text_new_game = pygame.font.Font('data/text_fonts/menu_font.otf',
                                                   int(self.menu_buttons_size * self.text_size_scale))
        self.menu_text_continue = pygame.font.Font('data/text_fonts/menu_font.otf',
                                                   int(self.menu_buttons_size * self.text_size_scale))
        self.menu_text_settings = pygame.font.Font('data/text_fonts/menu_font.otf',
                                                   int(self.menu_buttons_size * self.text_size_scale))
        self.menu_text_autors = pygame.font.Font('data/text_fonts/menu_font.otf',
                                                 int(self.menu_buttons_size * self.text_size_scale))
        self.menu_text_exit = pygame.font.Font('data/text_fonts/menu_font.otf',
                                               int(self.menu_buttons_size * self.text_size_scale))
        # Surfaces
        self.menu_text_the_carder_surface = self.menu_text_the_carder.render('The Carder', False, self.text_color)
        self.menu_text_new_game_surface = self.menu_text_new_game.render('New game', False, self.text_color)
        self.menu_text_continue_surface = self.menu_text_continue.render('Continue', False, self.text_color)
        self.menu_text_settings_surface = self.menu_text_settings.render('Settings', False, self.text_color)
        self.menu_text_exit_surface = self.menu_text_settings.render('Exit', False, self.text_color)
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
        self.bp = [self.w // 64, self.w // 64 + self.menu_text_new_game_surface.get_width(),
                                      self.h // 4,
                                      self.h // 4 + self.menu_text_new_game_surface.get_height(), self.w // 64,
                                      self.w // 64 + self.menu_text_continue_surface.get_width(),
                                      self.h // 4 + self.h // 6,
                                      self.h // 4 + self.h // 6 + self.menu_text_continue_surface.get_height(),
                                      self.w // 64,
                                      self.w // 64 + self.menu_text_settings_surface.get_width(),
                                      self.h // 4 + self.h // 6 * 2,
                                      self.h // 4 + self.h // 6 * 2 + self.menu_text_settings_surface.get_height(),
                                      self.w // 64,
                                      self.w // 64 + self.menu_text_exit_surface.get_width(),
                                      self.h // 4 + self.h // 6 * 3,
                                      self.h // 4 + self.h // 6 * 3 + self.menu_text_exit_surface.get_height()]
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
    def draw_menu_buttons(self, screen):
        screen.blit(self.menu_text_the_carder_surface, (
        (self.w // 2) - self.menu_text_the_carder_surface.get_size()[0] // 2,
        -self.menu_text_the_carder_surface.get_size()[0] // 16))
        screen.blit(self.menu_text_new_game_surface, (self.bp[0], self.bp[2]))
        screen.blit(self.menu_text_continue_surface, (self.bp[4], self.bp[6]))
        screen.blit(self.menu_text_settings_surface, (self.bp[8], self.bp[10]))
        screen.blit(self.menu_text_exit_surface, (self.bp[12], self.bp[14]))

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
        mp = pygame.mouse.get_pos()
        bp = self.bp
        if (mp[0] >= bp[0] and mp[0] <= bp[9]) and (mp[1] >= bp[2] and mp[1] <= bp[15]):
            self.text_color[0] = self.tc0 + 50
            self.text_color[1] = self.tc1 + 50
            self.text_color[2] = self.tc2 + 50
            if (mp[0] >= bp[0] and mp[0] <= bp[1]) and (mp[1] >= bp[2] and mp[1] <= bp[3]):
                self.menu_text_new_game_surface = self.menu_text_new_game.render('New game', False, self.text_color)
                self.text_color[0] = self.tc0
                self.text_color[1] = self.tc1
                self.text_color[2] = self.tc2
                self.menu_text_the_carder_surface = self.menu_text_the_carder.render('The Carder', False, self.text_color)
                self.menu_text_continue_surface = self.menu_text_continue.render('Continue', False, self.text_color)
                self.menu_text_settings_surface = self.menu_text_settings.render('Settings', False, self.text_color)
                self.menu_text_exit_surface = self.menu_text_settings.render('Exit', False, self.text_color)
                if pygame.mouse.get_pressed()[0] == True:
                    self.next_level = True
                    pygame.mixer_music.stop()
            elif (mp[0] >= bp[4] and mp[0] <= bp[5]) and (mp[1] >= bp[6] and mp[1] <= bp[7]):
                self.menu_text_continue_surface = self.menu_text_continue.render('Continue', False, self.text_color)
                self.text_color[0] = self.tc0
                self.text_color[1] = self.tc1
                self.text_color[2] = self.tc2
                self.menu_text_the_carder_surface = self.menu_text_the_carder.render('The Carder', False, self.text_color)
                self.menu_text_new_game_surface = self.menu_text_new_game.render('New game', False, self.text_color)
                self.menu_text_settings_surface = self.menu_text_settings.render('Settings', False, self.text_color)
                self.menu_text_exit_surface = self.menu_text_settings.render('Exit', False, self.text_color)
            elif (mp[0] >= bp[8] and mp[0] <= bp[9]) and (mp[1] >= bp[10] and mp[1] <= bp[11]):
                self.menu_text_settings_surface = self.menu_text_settings.render('Settings', False, self.text_color)
                self.text_color[0] = self.tc0
                self.text_color[1] = self.tc1
                self.text_color[2] = self.tc2
                self.menu_text_the_carder_surface = self.menu_text_the_carder.render('The Carder', False,self.text_color)
                self.menu_text_new_game_surface = self.menu_text_new_game.render('New game', False, self.text_color)
                self.menu_text_continue_surface = self.menu_text_continue.render('Continue', False, self.text_color)
                self.menu_text_exit_surface = self.menu_text_settings.render('Exit', False, self.text_color)
            else:
                self.menu_text_exit_surface = self.menu_text_settings.render('Exit', False, self.text_color)
                self.text_color[0] = self.tc0
                self.text_color[1] = self.tc1
                self.text_color[2] = self.tc2
                self.menu_text_the_carder_surface = self.menu_text_the_carder.render('The Carder', False, self.text_color)
                self.menu_text_new_game_surface = self.menu_text_new_game.render('New game', False, self.text_color)
                self.menu_text_continue_surface = self.menu_text_continue.render('Continue', False, self.text_color)
                self.menu_text_settings_surface = self.menu_text_settings.render('Settings', False, self.text_color)
                if pygame.mouse.get_pressed()[0] == True:
                    pygame.quit()
                    exit()
        else:
            self.text_color[0] = self.tc0
            self.text_color[1] = self.tc1
            self.text_color[2] = self.tc2
            self.menu_text_the_carder_surface = self.menu_text_the_carder.render('The Carder', False, self.text_color)
            self.menu_text_new_game_surface = self.menu_text_new_game.render('New game', False, self.text_color)
            self.menu_text_continue_surface = self.menu_text_continue.render('Continue', False, self.text_color)
            self.menu_text_settings_surface = self.menu_text_settings.render('Settings', False, self.text_color)
            self.menu_text_exit_surface = self.menu_text_settings.render('Exit', False, self.text_color)

    def player_action_check(self):
        if self.next_level:
            return True
        return False

    def draw(self, screen):
        screen.blit(self.background1_surface, (0, 0))
        self.draw_clouds(screen)
        self.mouse_check()
        self.draw_menu_buttons(screen)