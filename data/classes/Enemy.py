import pygame

from data.global_vars.enemies import *

from data.classes.constructor.Lines_constructor import Line

# enemyes
enemy_scale = 0.3
enemy_position = (1150, 350)

from time import *

from data.global_vars import hero

from data.classes.constructor.Elements import Img,Text
class Enemy:
    def __init__(self, enemy_type, screen_info):
        self.curent_intention_index = 0

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
        self.enemy_line = Line(screen_info, enemy_position, self.enemy_surface.get_size())


    def get_hp(self):
        return enemies[self.enemy_type][0][0]

    def clear_values(self):
        enemies[self.enemy_type][0][1] = 0

    def check_impossible_values(self):
        if enemies[self.enemy_type][0][0]>enemies[self.enemy_type][1][0]:
            enemies[self.enemy_type][0][0]=enemies[self.enemy_type][1][0]

    def make_turn(self):
        self.clear_values()

        current_intention = enemies[self.enemy_type][2][self.curent_intention_index]

        if current_intention[0]=='A':
            attack = int(current_intention[1:])
            if hero.hero[hero.hero_class][0][1] <= 0:
                hero.hero[hero.hero_class][0][0] -= attack
            elif hero.hero[hero.hero_class][0][1] >= attack:
                hero.hero[hero.hero_class][0][1] -= attack
            else:
                attack -= hero.hero[hero.hero_class][0][1]
                hero.hero[hero.hero_class][0][1] = 0
                hero.hero[hero.hero_class][0][0] -= attack
        else:
            int_text = intention_actions[current_intention[0]][0]
            command = str(int_text[:-1]) + str(int_text[-1]) + '=' + str(current_intention[1:])
            exec(command)

        self.check_impossible_values()

        self.curent_intention_index+=1

    def draw_enemy_intention(self):
        # down to zero
        if self.curent_intention_index + 1 > len(enemies[self.enemy_type][2]):
            self.curent_intention_index = 0
        current_intention = enemies[self.enemy_type][2][self.curent_intention_index]

        enemy_intention_images = enemy_intentions[current_intention[0]]


        intention_scale = 0.3

        self.intention_text = Text(current_intention[1:],sysFont='arial', k=0.5)

        if (len(enemy_intention_images)>1) and (type(enemy_intention_images) is not str):
            for el in enemy_intention_images.keys():
                if int(current_intention[1:])<=int(el):
                    inten_surf_ex = pygame.image.load(enemy_intention_images[el])
                    intentions_pos = (
                    self.enemy_line.lines_position[0] + self.enemy_line.hp_trace_surface.get_width() // 4
                    + inten_surf_ex.get_width() // 4,
                    self.enemy_line.lines_position[1] - inten_surf_ex.get_height() // 2)

                    intention = Img(self.screen_info, enemy_intention_images[el], k=intention_scale)
                    intention.draw(self.screen,intentions_pos)
                    break
        else:
            inten_surf_ex = pygame.image.load(enemy_intention_images)
            intentions_pos = (
                self.enemy_line.lines_position[0] + self.enemy_line.hp_trace_surface.get_width() // 4
                + inten_surf_ex.get_width() // 4,
                self.enemy_line.lines_position[1] - inten_surf_ex.get_height() // 2)

            intention = Img(self.screen_info, enemy_intention_images, k=intention_scale)
            intention.draw(self.screen,intentions_pos)

        self.intention_text.draw(self.screen, (
            intentions_pos[0]+intention.get_width()//2-self.intention_text.get_width()//2,
            intentions_pos[1]+intention.get_height()//2-self.intention_text.get_height()//2)
        )

    def draw_enemy(self):
        self.screen.blit(self.enemy_surface, enemy_position)
        self.enemy_line.draw(enemies[self.enemy_type], mirror=True)
        self.draw_enemy_intention()

    def get_type(self):
        return self.enemy_type


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