import pygame

from data.global_vars.enemies import *

from data.classes.constructor.Lines_constructor import Line

# enemyes
enemy_scale = 0.5
enemy_position = (1000, 400)

from data.classes.constructor.Elements import Img
class Enemy:
    def __init__(self, enemy_type, screen_info):
        self.screen_info = screen_info

        screen = screen_info[0]
        screen_scale = screen_info[1]
        screen_size = screen_info[2]

        self.screen = screen
        self.h = screen_size[1]
        self.w = screen_size[0]
        self.screen_scale = screen_scale

        self.enemy_type = enemy_type
        self.enemy_hp = enemies[self.enemy_type][0][0]
        self.enemy_max_hp = enemies[self.enemy_type][1][0]
        self.enemy_intentions = enemies[self.enemy_type][1]

        self.enemy_surface = pygame.image.load(enemies[enemy_type][3])
        self.enemy_surface = pygame.transform.scale(self.enemy_surface, (
            self.enemy_surface.get_size()[0] * self.screen_scale * enemy_scale,
            self.enemy_surface.get_size()[1] * self.screen_scale * enemy_scale))

        self.enemy_size = self.enemy_surface.get_size()
        self.enemy_type = enemy_type

        #initialize enemy hp df rage line
        self.enemy_line = Line(screen_info, enemies[self.enemy_type], enemy_position, self.enemy_surface.get_size())

    def draw_enemy_intention(self, current_enemy_intention):
        # down to zero
        if current_enemy_intention + 1 > len(enemies[self.enemy_type][2]):
            current_enemy_intention = 0
        current_intention = enemies[self.enemy_type][2][current_enemy_intention]

        enemy_intention_images = enemy_intentions[current_intention[0]]

        intentions_pos = (self.w-310*self.screen_scale, 130*self.screen_scale)
        intention_scale = 0.5

        if (len(enemy_intention_images)>1) and (type(enemy_intention_images) is not str):
            for el in enemy_intention_images.keys():
                if int(current_intention[1:])<=int(el):
                    intention = Img(self.screen_info, enemy_intention_images[el], k=intention_scale)
                    intention.draw(intentions_pos)
                    break
        else:
            intention = Img(self.screen_info, enemy_intention_images, k=intention_scale)
            intention.draw(intentions_pos)

    def draw_enemy(self):
        self.screen.blit(self.enemy_surface, enemy_position)
        self.enemy_line.draw()
        self.draw_enemy_intention(0)


# def enemy_turn(current_enemy_intention):
#     # down to zero
#     if current_enemy_intention + 1 > len(enemy_intentions_dict[rand_1_enemy_number]):
#         current_enemy_intention = 0
#     current_intention = enemy_intentions_dict[rand_1_enemy_number][current_enemy_intention]
#     if current_intention[0] == 'A':
#         enemy_dict[enemy_type][0] -= int(current_intention[1:])
#         pass
#
#     current_enemy_intention += 1
#     return current_enemy_intention