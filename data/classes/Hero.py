import pygame

from data.global_vars.hero import hero

from data.classes.Lines_constructor import Line

# heroes
hero_scale = 0.5
hero_position = (-200, 400)


class Hero:
    def __init__(self, hero_class, screen_info):
        screen = screen_info[0]
        screen_scale = screen_info[1]
        screen_size = screen_info[2]

        self.screen = screen
        self.h = screen_size[1]
        self.w = screen_size[0]
        self.screen_scale = screen_scale

        self.hero_mp_text = pygame.font.Font(None, int(50 * self.screen_scale))
        self.hero_poison_text = pygame.font.Font(None, int(50 * self.screen_scale))

        self.player_surface = pygame.image.load(hero[hero_class][2])
        self.player_surface = pygame.transform.scale(self.player_surface, (
            self.player_surface.get_size()[0] * self.screen_scale * hero_scale,
            self.player_surface.get_size()[1] * self.screen_scale * hero_scale))

        self.hero_size = self.player_surface.get_size()
        self.hero_class = hero_class

        self.hero_states = hero[self.hero_class][0]
        self.hero_max_states = hero[self.hero_class][1]

        #initialize hero hp df rage line
        self.hero_line = Line(screen_info, hero[self.hero_class], hero_position, self.player_surface.get_size())

    # Draws rage, poison, mp texts
    def draw_hero_text(self):
        hero_poison_text_surface = self.hero_poison_text.render(str(self.hero_states[4]) + ' POISON', False,
                                                                (255, 255, 255))
        self.screen.blit(hero_poison_text_surface, (0, hero_poison_text_surface.get_height() * 1))
        hero_attack_text_surface = self.hero_poison_text.render(str(self.hero_states[5]) + ' ATK', False,
                                                                (255, 255, 255))
        self.screen.blit(hero_attack_text_surface, (0, hero_attack_text_surface.get_height() * 2))
        hero_mp_text_surface = self.hero_mp_text.render(
            str(self.hero_states[3]) + '/' + str(self.hero_max_states[3]) + ' MP', False, (255, 255, 255))
        self.screen.blit(hero_mp_text_surface, (0, hero_mp_text_surface.get_height() * 3))

    def draw_hero(self):
        self.screen.blit(self.player_surface, hero_position)
        self.draw_hero_text()
        self.hero_line.draw()
