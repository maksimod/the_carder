import copy

from data.global_vars import hero
from data.global_vars.screen_info import *

from data.classes.constructor.Lines_constructor import Line
from data.classes.constructor.Elements import Img, CText

# heroes
hero_scale = 0.3
hero_position = (80*screen_scale, 200*screen_scale)

from data.global_vars.screen_info import *

from data.classes.Animation import Animation

from data.global_vars import enemy_turn
class Hero:
    def __init__(self, hero_class):
        #add mp animation
        self.def_anim_to_play = False
        
        self.mp_anim = Animation(38, 30, 'data/animations/heroes/bercerk/mp', (45*screen_scale,400*screen_scale), frame_scale=0.6)
        self.df_anim = Animation(10, 30, 'data/animations/elements/defense', (260*screen_scale,120*screen_scale), frame_scale=0.6, looped=False)
        self.hero_anim = Animation(38, 30, f'data/animations/heroes/{hero_class}/anim', hero_position, frame_scale=1.2)
        
        
        self.defense_was_done = False
        self.defense_was_waited = False
        
        self.poison_first_time = True
        self.can_poison = False
        self.previous_poison = 0

        self.h = screen_size[1]
        self.w = screen_size[0]

        self.hero_mp_text = pygame.font.Font(None, int(50 * screen_scale))
        self.hero_poison_text = pygame.font.Font(None, int(50 * screen_scale))

        self.player_surface = pygame.image.load(hero.hero[hero.hero_class][2])
        self.player_surface = pygame.transform.scale(self.player_surface, (
            self.player_surface.get_size()[0] * screen_scale * hero_scale,
            self.player_surface.get_size()[1] * screen_scale * hero_scale))

        self.hero_size = self.player_surface.get_size()
        self.hero_class = hero_class

        self.hero_hp_mp = copy.copy(hero.hero[self.hero_class][0])
        self.hero_max_hp_mp = copy.copy(hero.hero[self.hero_class][1])
        self.df = copy.copy(hero.hero[self.hero_class][0][1])

        # initialize hero hp df rage line
        self.hero_line = Line(hero_position, self.player_surface.get_size())
        
        self.states = {
            #buffs: strength, mp increase (just to next turn)
            'BS': 0,
            'BI': 0,
            #Talents: barricade, dexterity
            'TB': 0,
            'TD': 0,
            #debuffs: vulnerable, bleeding, weak, poison, fragile
            'LV': 0,
            'LB': 0,
            'LW': 0,
            'LP': 0,
            'LF': 0,
            #low curses: anti-dexterity
            'PD':0
        }
        
        state_image_k = 0.1
        self.states_img = {
            # buffs: strength, mp increase (just to next turn)
            'BS': Img('data/images/elements/states/positive/strength.png', state_image_k),
            # Talents: barricade, dexterity
            'TB': 0,
            'TD': 0,
            # debuffs: vulnerable, bleeding, weak, poison, fragile
            'LV': Img('data/images/elements/states/negative/vulnerable.png', state_image_k),
            'LB': 0,
            'LW': 0,
            'LP': 0,
            'LF': 0,
            # low curses: anti-dexterity
            'PD': 0
        }

    def get_defense(self,defence):
        self.df += defence
        self.def_anim_to_play = True

    def make_turn(self):
        self.hero_hp_mp[3] = hero.hero[hero.hero_class][1][1]

        if self.can_poison:
            self.hero_hp_mp[0] -= self.previous_poison
            self.previous_poison = self.states['LP']
        if (self.states['LP']>0) and (self.poison_first_time):
            self.poison_first_time = False
            self.can_poison = True
            self.previous_poison = self.states['LP']
        
        # Delete defense
        self.df = 0
        
        # LOW ALL DEBUFF BY 1
        for el in self.states:
            if el[0] == 'L':
                if int(self.states[el]) > 0:
                    self.states[el] = self.states[el] - 1

    def draw_hero_text(self):
        hero_poison_text_surface = self.hero_poison_text.render(
            str(self.states['LP']) + ' POISON', False,
            (255, 255, 255))
        screen.blit(hero_poison_text_surface, (0, hero_poison_text_surface.get_height() * 1))

    def update_hero(self):
        
        # screen.blit(self.player_surface, hero_position)
        
        if not enemy_turn.enemy_turn:
            self.hero_anim.draw()
        else:
            self.hero_anim.draw_default_frame()
        
        self.draw_hero_text()
        
        pars = [self.hero_hp_mp[0], self.hero_max_hp_mp[0], self.df]
        
        self.hero_line.draw(pars)
        
        # self.hero_mp_img.draw((65*screen_scale,420*screen_scale))

        self.mp_anim.draw()
        
        self.current_mp_text = CText(str(self.hero_hp_mp[3])+'/', k=0.3*screen_scale)
        self.max_mp_text = CText(str(self.hero_max_hp_mp[1]), k=0.3 * screen_scale)
        self.current_mp_text.draw((85*screen_scale,450*screen_scale))
        self.max_mp_text.draw((110 * screen_scale, 450 * screen_scale))

        if self.def_anim_to_play:
            self.df_anim.draw()
            if self.df_anim.is_hide():
                self.def_anim_to_play = False
                self.df_anim.restart()