import pygame

from data.global_vars.enemies import *

from data.classes.constructor.Lines_constructor import Line
from data.global_vars.screen_info import *
from time import *

from data.global_vars import hero

from data.classes.constructor.Elements import Img,Text

class Enemies:
    def __init__(self, enemy_types):
        enemy_name = []
        start_ind = 0
        end_ind = -1
        if '&' in enemy_types:
            for i in range(len(enemy_types)):
                if enemy_types[i] == '&':
                    end_ind = i
                    enemy_name.append(enemy_types[start_ind:end_ind])
                    start_ind = i+1
        enemy_name.append(enemy_types[start_ind:])
        self.enemy_name = enemy_name

        #Now create enemies:
        self.enemies = []
        index = 0
        for el in enemy_name:
            self.enemies.append(Enemy(el, index))
            index+=1

    def get_names(self):
        return self.enemy_name

    def draw_enemies(self):
        for i in range(len(self.enemies)):
            if self.enemies[i].get_hp()>0:
                self.enemies[i].draw_enemy()

    def make_turn(self):
        for i in range(len(self.enemies)):
            if self.enemies[i].get_hp() > 0:
                self.enemies[i].make_turn()

class Enemy:
    def __init__(self, enemy_type, index):
        self.curent_intention_index = 0

        self.h = screen_size[1]
        self.w = screen_size[0]

        self.enemy_type = enemy_type
        self.enemy_hp = enemies[self.enemy_type][0][0]
        self.enemy_max_hp = enemies[self.enemy_type][1][0]
        self.enemy_intentions = enemies[self.enemy_type][1]

        self.enemy_scale = 0.3
        if 'AI' in enemies[self.enemy_type][3]:
            self.enemy_scale = 0.4

        self.enemy_surface = pygame.image.load(enemies[enemy_type][3])
        self.enemy_surface = pygame.transform.scale(self.enemy_surface, (
            self.enemy_surface.get_size()[0] * screen_scale * self.enemy_scale,
            self.enemy_surface.get_size()[1] * screen_scale * self.enemy_scale))

        self.enemy_size = self.enemy_surface.get_size()
        self.enemy_type = enemy_type


        self.enemy_position = (750*screen_scale-index*400*screen_scale, 230*screen_scale)

        #initialize enemy hp df rage line
        self.enemy_line = Line(self.enemy_position, self.enemy_surface.get_size())

        if 'AI' in enemies[self.enemy_type][3]:
            pass
            self.enemy_position = [self.enemy_position[0]+120*screen_scale,self.enemy_position[1]]


    def get_type(self):
        return self.enemy_type

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

        intentions_list = []
        start_ind = 0
        end_ind = -1
        if '&' in current_intention:
            for i in range(len(current_intention)):
                if current_intention[i] == '&':
                    end_ind = i
                    intentions_list.append(current_intention[start_ind:end_ind])
                    start_ind = i+1
        intentions_list.append(current_intention[start_ind:])

        for current_intention in intentions_list:
            if current_intention[0]=='A':
                attack = int(current_intention[1:])
                # Add strength to attack
                attack+=enemies[self.enemy_type][0][-2][buffs_indexes['S']]

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

                #if H/D/P/etc. - intent_val_strt_indx=1; if C/L/P/B/etc. - intent_val_strt_indx=1
                for i in range(len(str(current_intention))):
                    if str(current_intention)[i] in ['1','2','3','4','5','6','7','8','9','0']:
                        intent_val_strt_indx = i
                        break

                command = str(int_text[:-1]) + str(int_text[-1]) + '=' + str(current_intention[intent_val_strt_indx:])
                exec(command)

        self.check_impossible_values()

        self.curent_intention_index+=1

    def draw_enemy_intention(self):
        # down to zero
        if self.curent_intention_index + 1 > len(enemies[self.enemy_type][2]):
            self.curent_intention_index = 0
        current_intention = enemies[self.enemy_type][2][self.curent_intention_index]

        enemy_intention_images = enemy_intentions[current_intention[0]]

        intention_scale = 0.2 * screen_scale

        value_amount = ''
        # current intention = A/D/H/P/etc.
        if current_intention[1] in ['1','2','3','4','5','6','7','8','9','0']:
            value_amount = int(current_intention[1:])
            if current_intention[0] == 'A':
                value_amount += enemies[self.enemy_type][0][-2][buffs_indexes['S']]

        self.intention_text = Text(str(value_amount),sysFont='arial', k=0.2*screen_scale)

        if (len(enemy_intention_images)>1) and (type(enemy_intention_images) is not str):
            for el in enemy_intention_images.keys():
                if int(current_intention[1:])<=int(el):
                    inten_surf_ex = pygame.image.load(enemy_intention_images[el])
                    inten_surf_ex = pygame.transform.scale(inten_surf_ex, (
                    inten_surf_ex.get_width() * intention_scale, inten_surf_ex.get_height() * intention_scale))
                    print(inten_surf_ex.get_height())
                    intentions_pos = (
                    self.enemy_line.lines_position[0] + self.enemy_line.hp_trace_surface.get_width() // 4
                    + inten_surf_ex.get_width() // 1,
                    self.enemy_line.lines_position[1] - inten_surf_ex.get_height()*1*screen_scale)

                    intention = Img(enemy_intention_images[el], k=intention_scale)
                    intention.draw(intentions_pos)
                    break
        else:
            inten_surf_ex = pygame.image.load(enemy_intention_images)
            inten_surf_ex = pygame.transform.scale(inten_surf_ex, (inten_surf_ex.get_width()*intention_scale, inten_surf_ex.get_height()*intention_scale))
            print(inten_surf_ex.get_height())
            intentions_pos = (
                self.enemy_line.lines_position[0] + self.enemy_line.hp_trace_surface.get_width() // 4
                + inten_surf_ex.get_width() // 1,
                self.enemy_line.lines_position[1] - inten_surf_ex.get_height()*1*screen_scale)

            intention = Img(enemy_intention_images, k=intention_scale)
            intention.draw(intentions_pos)

        self.intention_text.draw((
            intentions_pos[0]+intention.get_width()//2-self.intention_text.get_width()//2,
            intentions_pos[1]+intention.get_height()//2-self.intention_text.get_height()//2)
        )

    def check_focus(self):
        mx,my = pygame.mouse.get_pos()
        
        if mx>self.enemy_position:
            print('OK')
        else:
            print('NOK')

    def draw_enemy(self):
        self.check_focus
        screen.blit(self.enemy_surface, self.enemy_position)
        self.enemy_line.draw(enemies[self.enemy_type], mirror=True)
        self.draw_enemy_intention()

    def get_type(self):
        return self.enemy_type