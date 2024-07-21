import pygame

from data.global_vars.enemies import *

from data.classes.constructor.Lines_constructor import Line
from data.global_vars.screen_info import *
from time import *

from data.global_vars import hero

from data.classes.constructor.Elements import Img, Text


class Enemies:
    def __init__(self, enemy_types, player):
        enemy_name = []
        start_ind = 0
        end_ind = -1
        if '&' in enemy_types:
            for i in range(len(enemy_types)):
                if enemy_types[i] == '&':
                    end_ind = i
                    enemy_name.append(enemy_types[start_ind:end_ind])
                    start_ind = i + 1
        enemy_name.append(enemy_types[start_ind:])
        self.enemy_name = enemy_name
        
        # Now create enemies:
        self.enemies = []
        index = 0
        for el in enemy_name:
            self.enemies.append(Enemy(el, index, player, (750 * screen_scale - index * 400 * screen_scale, 230 * screen_scale)))
            self.enemies[-1].enemies = self
            index += 1
        self.last_index = index
    
    def get_names(self):
        return self.enemy_name
    
    def get_enemies(self):
        return self.enemies
    
    def draw_enemies(self):
        for i in range(len(self.enemies)):
            if self.enemies[i].get_hp() > 0:
                self.enemies[i].draw_enemy()
    
    def make_turn(self):
        for i in range(len(self.enemies)):
            if self.enemies[i].get_hp() > 0:
                self.enemies[i].make_turn()


class Enemy:
    def __init__(self, enemy_type, index, player, enemy_position):
        self.player = player
        #to delete defense after turn
        self.defense_was_done = False
        self.defense_was_waited = False
        
        self.curent_intention_index = 0
        
        self.h = screen_size[1]
        self.w = screen_size[0]
        
        self.enemy_type = enemy_type
        self.enemy_hp = enemies[self.enemy_type][0][0]
        self.enemy_max_hp = enemies[self.enemy_type][1][0]
        self.enemy_df = enemies[self.enemy_type][0][1]
        self.enemy_intentions = enemies[self.enemy_type][1]
        
        self.enemy_scale = 1
        self.x_offset = 0
        if self.enemy_type == 'guardian' or self.enemy_type == 'snakes' or self.enemy_type == 'wizard' or self.enemy_type == 'joker':
            self.enemy_scale = 0.3
        if 'AI' in enemies[self.enemy_type][3]:
            self.enemy_scale = 0.4
        if 'slave' in self.enemy_type:
            self.enemy_scale*=0.2
            self.x_offset = 50*screen_scale
        
        self.enemy_surface = pygame.image.load(enemies[enemy_type][3])
        self.enemy_surface = pygame.transform.scale(self.enemy_surface, (
            self.enemy_surface.get_size()[0] * screen_scale * self.enemy_scale,
            self.enemy_surface.get_size()[1] * screen_scale * self.enemy_scale))
        
        self.enemy_size = self.enemy_surface.get_size()
        self.enemy_type = enemy_type
        
        #enemy pos must also depends on another enemies
        self.enemy_position = enemy_position
        
        # initialize enemy hp df rage line
        self.enemy_line = Line(self.enemy_position, self.enemy_surface.get_size(), k=self.enemy_scale*3)
        
        self.focus_img = Img('data/images/elements/enemy_countur.png', k=0.2)
        
        if 'AI' in enemies[self.enemy_type][3]:
            pass
            self.enemy_position = [self.enemy_position[0] + 120 * screen_scale, self.enemy_position[1]]
        
        self.states = {
            # buffs: strength, mp increase (just to next turn)
            'BS': 0,
            # Talents: barricade
            'TB': 0,
            # debuffs: vulnerable, bleeding, weak, poison, fragile
            'LV': 0,
            'LB': 0,
            'LW': 0,
            'LP': 0,
            'LF': 0,
            # low curses: anti-dexterity
            'PD': 0
        }
    
    def check_focus(self):
        mx, my = pygame.mouse.get_pos()
        
        if self.enemy_position[0] < mx < self.enemy_position[0] + self.enemy_surface.get_width():
            if self.enemy_position[1] < my < self.enemy_position[1] + self.enemy_surface.get_height():
                self.focus_img.draw(
                    (self.enemy_position[0] + self.enemy_surface.get_width() // 4, self.enemy_position[1]))
                return True
        return False
    
    def get_type(self):
        return self.enemy_type
    
    def get_hp(self):
        return self.enemy_hp
    
    def clear_values(self):
        enemies[self.enemy_type][0][1] = 0
    
    def check_impossible_values(self):
        if self.enemy_hp > self.enemy_max_hp:
            self.enemy_hp = self.enemy_max_hp
    
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
                    start_ind = i + 1
        intentions_list.append(current_intention[start_ind:])
        
        for current_intention in intentions_list:
            #Apply to enemy
            #also if edfense we add 'timer' to delete it
            if current_intention[0] == 'D':
                self.defense_was_done = True
                self.defense_was_waited = False
                self.enemy_df = int(current_intention[1:])
            elif current_intention[0] == 'H': self.enemy_hp += int(current_intention[1:])
            elif current_intention[0] == 'B': self.states[current_intention[:2]] = int(current_intention[2:])
            elif current_intention[0] == 'S':
                #to understand slave size
                slave_surface = pygame.image.load('data/images/enemies/jokerslave.png')
                x_offset = 40*screen_scale
                y_offset = 60*screen_scale
                
                slave_pos_x = self.enemies.enemies[-1].enemy_position[0]-slave_surface.get_width()*0.3-x_offset
                slave_pos_y = self.enemies.enemies[-1].enemy_position[1]+y_offset
                self.enemies.enemies.append(Enemy(self.enemy_type+'slave', self.enemies.last_index, self.player, (slave_pos_x,slave_pos_y)))
                self.enemies.last_index += 1
            #apply to hero
            elif current_intention[0] == 'P':
                self.player.states['LP'] += int(current_intention[1:])
            elif current_intention[0] == 'A':
                attack = int(current_intention[1:])
                # Check week
                # Add strength to attack
                attack += self.states['BS']
                
                # hero_hp = self.player.hero_hp_mp[0]
                # hero_df = self.player.hero_hp_mp[3]
                
                if self.player.df <= 0:
                    self.player.hero_hp_mp[0] = self.player.hero_hp_mp[0] - attack
                elif self.player.df >= attack:
                    self.player.df = self.player.df - attack
                else:
                    attack = attack - self.player.df
                    self.player.df = 0
                    self.player.hero_hp_mp[0] = self.player.hero_hp_mp[0] - attack
            else:
                raise ValueError('NOT STATED')
        
        self.check_impossible_values()
        
        self.curent_intention_index += 1
        
        #Delete defense
        if self.defense_was_done:
            if self.defense_was_waited:
                self.enemy_df=0
                self.defense_was_done = False
                self.defense_was_waited = False
            else:
                self.defense_was_waited = True
        
        #LOW ALL DEBUFF BY 1
        print('OK')
        for el in self.states:
            print(el)
            print('el[0] is', el[0])
            if el[0]=='L':
                if int(self.states[el])>0:
                    self.states[el] = self.states[el] - 1
                    print('NOW', self.states[el])
    
    def draw_enemy_intention(self):
        # down to zero
        if self.curent_intention_index + 1 > len(enemies[self.enemy_type][2]):
            self.curent_intention_index = 0
        current_intention = enemies[self.enemy_type][2][self.curent_intention_index]
        
        enemy_intention_images = enemy_intentions[current_intention[0]]
        
        intention_scale = 0.2 * screen_scale
        
        if (len(enemy_intention_images) > 1) and (type(enemy_intention_images) is not str):
            for el in enemy_intention_images.keys():
                if int(current_intention[1:]) <= int(el):
                    inten_surf_ex = pygame.image.load(enemy_intention_images[el])
                    inten_surf_ex = pygame.transform.scale(inten_surf_ex, (
                        inten_surf_ex.get_width() * intention_scale, inten_surf_ex.get_height() * intention_scale))
                    intentions_pos = (
                        self.enemy_line.lines_position[0] + self.enemy_line.hp_trace_surface.get_width() // 4
                        + inten_surf_ex.get_width() // 1,
                        self.enemy_line.lines_position[1] - inten_surf_ex.get_height() * 1 * screen_scale)
                    
                    intention = Img(enemy_intention_images[el], k=intention_scale)
                    intention.draw(intentions_pos)
                    break
        else:
            inten_surf_ex = pygame.image.load(enemy_intention_images)
            inten_surf_ex = pygame.transform.scale(inten_surf_ex, (
                inten_surf_ex.get_width() * intention_scale, inten_surf_ex.get_height() * intention_scale))
            intentions_pos = (
                self.enemy_line.lines_position[0] + self.enemy_line.hp_trace_surface.get_width() // 4
                + inten_surf_ex.get_width() // 1,
                self.enemy_line.lines_position[1] - inten_surf_ex.get_height() * 1 * screen_scale)
            
            intention = Img(enemy_intention_images, k=intention_scale)
            intention.draw(intentions_pos)
        
        value_amount = None
        # current intention = A/D/H/P/etc.
        if current_intention[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            value_amount = int(current_intention[1:])
            self.intention_text = Text(str(value_amount), sysFont='arial', k=0.2 * screen_scale)
            self.intention_text.draw((
                intentions_pos[0] + intention.get_width() // 2 - self.intention_text.get_width() // 2,
                intentions_pos[1] + intention.get_height() // 2 - self.intention_text.get_height() // 2)
            )
    
    def draw_enemy(self):
        self.check_focus()
        screen.blit(self.enemy_surface, (self.enemy_position[0]+self.x_offset, self.enemy_position[1]))
        
        pars = [self.enemy_hp, self.enemy_max_hp, self.enemy_df]
        self.enemy_line.draw(pars, mirror=True)
        
        self.draw_enemy_intention()
    
    def get_type(self):
        return self.enemy_type

    #effects
    def get_damage(self, attack):
        if self.states['LV']>0: attack*=1.5
        if self.enemy_df <= 0:
            self.enemy_hp -= attack
        else:
            if self.enemy_df - attack >= 0:
                self.enemy_df -= attack
            else:
                attack -= self.enemy_df
                self.enemy_df = 0
                self.enemy_hp -= attack