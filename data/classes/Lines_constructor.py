import pygame

class Line:
    def line_scale(self, surface,cstate,mstate):
        return (self.screen_scale / 1.5 * surface.get_width() * cstate / mstate - 9,
                self.screen_scale / 1.5 * surface.get_height())
    
    #pars(parameters) = [hp,df,rage]
    def __init__(self, screen_info, pars, aim_pos, aim_size, font=None):
        screen = screen_info[0]
        screen_scale = screen_info[1]
        screen_size = screen_info[2]

        self.screen = screen
        self.h = screen_size[1]
        self.w = screen_size[0]
        self.screen_scale = screen_scale


        self.hero_states = pars[0]
        self.hero_max_states = pars[1]
        self.df = self.hero_states[1]
        if len(self.hero_states)>2: self.rage = self.hero_states[2]
        chp = self.hero_states[0]
        mhp = self.hero_max_states[0]

        if not font:
            font = pygame.font.Font(None, int(25 * screen_scale))

        self.hero_hp_text_surface = font.render(str(chp) + '/' + str(mhp) + ' HP', False, (255, 255, 255))
        self.hero_df_text_surface = font.render(str(self.df), False, (255, 255, 255))
        self.hero_hp_text_w = self.hero_hp_text_surface.get_width()
        self.hero_hp_text_h = self.hero_hp_text_surface.get_height()
        self.hero_df_text_w = self.hero_df_text_surface.get_width()
        self.hero_df_text_h = self.hero_df_text_surface.get_height()


        hp_line_surface = pygame.image.load('data/images\\elements\\hp_def\\hp_line.png')
        hp_line_surface = pygame.transform.scale(hp_line_surface, self.line_scale(hp_line_surface,chp,mhp))
        
        self.hp_trace_surface = pygame.image.load('data/images\\elements\\hp_def\\hp_tracing.png')
        self.hp_trace_w = self.hp_trace_surface.get_width()
        self.hp_trace_h = self.hp_trace_surface.get_height()

        lines_position = (aim_pos[0] + self.hp_trace_w // 2 + 9, self.h - aim_size[1] - 100)
        
        #prepare vars for draw function
        self.hp_line_surface = hp_line_surface
        self.lines_position = lines_position

    def draw(self):
        self.screen.blit(self.hp_line_surface, self.lines_position)
        self.screen.blit(self.hp_trace_surface, self.lines_position)

        if self.df > 0:
            shield_icon_surface = pygame.image.load('data/images\\elements\\hp_def\\shield_icon.png')
            shield_icon_h = shield_icon_surface.get_height()
            shield_line_surface = pygame.image.load('data/images\\elements\\hp_def\\def_line.png')
            df_trace_surface = pygame.image.load('data/images\\elements\\hp_def\\df_tracing.png')

            shield_icon_pos = (
            self.hp_trace_w // 2 - shield_icon_h // 2 + self.hero_df_text_w // 2,
            self.h // 2 * self.screen_scale - self.screen_scale * 350 + self.hero_df_text_h // 2 - shield_icon_h // 4)
            df_text_pos = (self.hp_trace_w // 2,
            self.h // 2 * self.screen_scale - self.screen_scale * 350 + self.hero_df_text_h // 2)

            self.screen.blit(shield_line_surface, (self.hp_line_surface.get_width() // 2, self.lines_position[1]))
            self.screen.blit(df_trace_surface, (self.hp_trace_w // 2, self.lines_position[1]))
            self.screen.blit(shield_icon_surface, shield_icon_pos)
            self.screen.blit(self.hero_df_text_surface, df_text_pos)

        self.screen.blit(self.hero_hp_text_surface,
                         (self.lines_position[0] + self.hp_trace_w // 2 - self.hero_hp_text_w // 2,
                          self.lines_position[1] + self.hp_trace_h // 2 - self.hero_hp_text_h // 2))