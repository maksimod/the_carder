#Variables
hero_dict = {
    #[hp, def, rage, mp,poison, attack]
    "bercerk": [140,0,0,4,0,0]
}
hero_dict_max = {
    "bercerk": [140,0,0,4,0,0]
}
#hero
hero_class = "bercerk"

#heroes
hero_scale = 0.5
bercerc_surface = pygame.image.load('data/images\\heroes\\bercerk.png')
bercerc_surface = pygame.transform.scale(bercerc_surface, (bercerc_surface.get_size()[0]*screen_scale*hero_scale,bercerc_surface.get_size()[1]*screen_scale*hero_scale))
hero_position = (0, h//2-lev1_enemy_surface.get_height()//2)

def draw_hero(hero_class):
    if hero_class == "bercerk":
        screen.blit(bercerc_surface, (hero_position))

def draw_hero_states(hero_class, card_size):
    hero_df_text_surface = hero_df_text.render(str(hero_dict[hero_class][1])  , False, (255,255,255))
    hero_rage_text_surface = hero_rage_text.render(str(hero_dict[hero_class][2])+' RAGE', False, (255,255,255))
    screen.blit(hero_rage_text_surface, (0,0))
    hero_poison_text_surface = hero_poison_text.render(str(hero_dict[hero_class][4])+' POISON', False, (255,255,255))
    screen.blit(hero_poison_text_surface, (0,hero_poison_text_surface.get_height()*1))
    hero_attack_text_surface = hero_poison_text.render(str(hero_dict[hero_class][5])+' ATK', False, (255,255,255))
    screen.blit(hero_attack_text_surface, (0,hero_attack_text_surface.get_height()*2))
    hero_mp_text_surface = hero_mp_text.render(str(hero_dict[hero_class][3])+'/'+str(hero_dict_max[hero_class][3])+' MP', False, (255,255,255))
    screen.blit(hero_mp_text_surface, (0,h-card_size[1]-hero_mp_text_surface.get_height()))
    #draw hp, def lines
    hp_line_surface = pygame.image.load('data/images\\elements\\hp_def\\hp_line.png')
    hp_line_surface = pygame.transform.scale(hp_line_surface,(screen_scale/1.5*hp_line_surface.get_width()*hero_dict[hero_class][0]/hero_dict_max[hero_class][0]-9, screen_scale/1.5*hp_line_surface.get_height()))
    hp_trace_surface = pygame.image.load('data/images\\elements\\hp_def\\hp_tracing.png')
    screen.blit(hp_line_surface, (hp_trace_surface.get_width()//2+9,h//2*screen_scale-screen_scale*350))
    screen.blit(hp_trace_surface, (hp_trace_surface.get_width()//2,h//2*screen_scale-screen_scale*350))
    if hero_dict[hero_class][1]>0:
        shield_icon_surface = pygame.image.load('data/images\\elements\\hp_def\\shield_icon.png')
        shield_line_surface = pygame.image.load('data/images\\elements\\hp_def\\def_line.png')
        df_trace_surface = pygame.image.load('data/images\\elements\\hp_def\\df_tracing.png')
        screen.blit(shield_line_surface, (hp_line_surface.get_width()//2,h//2*screen_scale-screen_scale*350))
        screen.blit(df_trace_surface, (hp_trace_surface.get_width()//2,h//2*screen_scale-screen_scale*350))
        screen.blit(shield_icon_surface, (hp_trace_surface.get_width()//2-shield_icon_surface.get_height()//2+hero_df_text_surface.get_width()//2,h//2*screen_scale-screen_scale*350+hero_df_text_surface.get_height()//2-shield_icon_surface.get_height()//4))
        screen.blit(hero_df_text_surface, (hp_trace_surface.get_width()//2,h//2*screen_scale-screen_scale*350+hero_df_text_surface.get_height()//2))
    hero_hp_text_surface = hero_hp_text.render(str(hero_dict[hero_class][0])+'/'+str(hero_dict_max[hero_class][0])+' HP', False, (255,255,255))
    screen.blit(hero_hp_text_surface, (hp_trace_surface.get_width()-hero_hp_text_surface.get_width()//2,h//2*screen_scale-screen_scale*350+hp_trace_surface.get_height()//2-hero_hp_text_surface.get_height()//2))

vulnerable = False