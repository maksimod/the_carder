from data.global_vars.screen_info import *


class Line:
    def line_scale(self, surface, cstate, mstate):
        return (screen_scale / 1.5 * surface.get_width() * cstate / mstate,
                screen_scale / 1.5 * surface.get_height())
    
    # pars(parameters) = [hp,df,rage]
    def __init__(self, aim_pos, aim_size, font=None, k=1):
        self.font = font
        
        self.aim_pos = aim_pos
        self.aim_size = aim_size
        
        self.h = screen_size[1]
        self.w = screen_size[0]
    
    def draw(self, hp_max_hp_def, mirror=False):
        aim_pos, aim_size = self.aim_pos, self.aim_size
        font = self.font
        
        chp = hp_max_hp_def[0]
        mhp = hp_max_hp_def[1]
        self.df = hp_max_hp_def[2]
        
        if not font:
            font = pygame.font.Font(None, int(30 * screen_scale))
        
        self.hero_hp_text_surface = font.render(str(chp) + '/' + str(mhp) + ' HP', False, (255, 255, 255))
        self.hero_df_text_surface = font.render(str(self.df), False, (255, 255, 255))
        self.hero_hp_text_w = self.hero_hp_text_surface.get_width()
        self.hero_hp_text_h = self.hero_hp_text_surface.get_height()
        self.hero_df_text_w = self.hero_df_text_surface.get_width()
        self.hero_df_text_h = self.hero_df_text_surface.get_height()
        
        r_scrn_scl = screen_scale * 0.8
        hp_line_surface = pygame.image.load('data/images\\elements\\hp_def\\hp_line.png')
        hp_line_surface = pygame.transform.scale(hp_line_surface, (
        hp_line_surface.get_width() * r_scrn_scl, hp_line_surface.get_height() * r_scrn_scl))
        
        self.hp_trace_surface = pygame.image.load('data/images\\elements\\hp_def\\hp_tracing.png')
        self.hp_trace_surface = pygame.transform.scale(self.hp_trace_surface, (
        self.hp_trace_surface.get_width() * r_scrn_scl, self.hp_trace_surface.get_height() * r_scrn_scl))
        self.hp_trace_w = self.hp_trace_surface.get_width()
        self.hp_trace_h = self.hp_trace_surface.get_height()
        
        if not mirror:
            lines_position = (aim_pos[0] - aim_size[1] // 3, aim_pos[1] - 50 * screen_scale)
        else:
            lines_position = (aim_pos[0] + aim_size[1] // 8, aim_pos[1] - 50 * screen_scale)
        
        screen.blit(hp_line_surface, lines_position,
                    (0, 0, hp_line_surface.get_width() * chp / mhp, hp_line_surface.get_height()))
        screen.blit(self.hp_trace_surface, lines_position)
        
        if self.df > 0:
            shield_icon_surface = pygame.image.load('data/images\\elements\\hp_def\\shield_icon.png')
            shield_icon_surface = pygame.transform.scale(shield_icon_surface, (
                shield_icon_surface.get_width() * r_scrn_scl, shield_icon_surface.get_height() * r_scrn_scl))
            shield_icon_h = shield_icon_surface.get_height()
            shield_line_surface = pygame.image.load('data/images\\elements\\hp_def\\def_line.png')
            shield_line_surface = pygame.transform.scale(shield_line_surface, (
                shield_line_surface.get_width() * r_scrn_scl, shield_line_surface.get_height() * r_scrn_scl))
            df_trace_surface = pygame.image.load('data/images\\elements\\hp_def\\df_tracing.png')
            df_trace_surface = pygame.transform.scale(df_trace_surface, (
                df_trace_surface.get_width() * r_scrn_scl, df_trace_surface.get_height() * r_scrn_scl))
            
            # if not mirror:
            shield_icon_pos = (
                lines_position[0] + self.hp_trace_surface.get_width() - shield_icon_surface.get_width() // 1,
                lines_position[1])
            df_text_pos = (shield_icon_pos[0] + shield_icon_h - self.hero_df_text_surface.get_width() * 1.2,
                           shield_icon_pos[1] + self.hero_df_text_h // 2.5)
            
            screen.blit(shield_line_surface, (lines_position[0], lines_position[1]))
            screen.blit(df_trace_surface, (lines_position[0], lines_position[1]))
            screen.blit(shield_icon_surface, shield_icon_pos)
            screen.blit(self.hero_df_text_surface, df_text_pos)
        
        screen.blit(self.hero_hp_text_surface,
                    (lines_position[0] + self.hp_trace_w // 2 - self.hero_hp_text_w // 2,
                     lines_position[1] + self.hp_trace_h // 2 - self.hero_hp_text_h // 2))
        
        self.lines_position = lines_position
