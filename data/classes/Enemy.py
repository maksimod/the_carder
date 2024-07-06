

class Enemy:
    def __init__(self,enemy_type):
        print("OK")


# current_enemy_intention = 0
#
#
# #enemies
# enemy_dict = {
#     #
#     11: [60, 60],
#     12: [50, 50],
#     13: [55, 55],
#     14: [40, 40]
# }
# # A - attack, H - heal, C - chars, D - def, B - buff, C - curse, P - low curse
# enemy_intentions_dict = {
#     11: ['A9','D10', 'A18'],
#     12: ['H20', 'D30', 'A20'],
#     13: ['P4', 'H20'],
#     14: ['S99', 'H15', 'A10']
# }
#
# #enemies
# rand_1_enemy_number = 10+random.randrange(1,5)
# lev1_enemy = 'data/images\\lev1\\enemies\\guard'+str(rand_1_enemy_number)+'.png'
# hero_hp_text = pygame.font.Font(None, int(25*text_size_scale))
# hero_mp_text = pygame.font.Font(None, int(50*text_size_scale))
# hero_df_text = pygame.font.Font(None, int(25*text_size_scale))
# hero_rage_text = pygame.font.Font(None, int(50*text_size_scale))
# hero_poison_text = pygame.font.Font(None, int(50*text_size_scale))
# hero_attack_text = pygame.font.Font(None, int(50*text_size_scale))
#
# #enemy_intentions_surfaces
# enemy_intention_attack_surface = pygame.image.load('data/images\\elements\\the_enemy_intentions\\attack.png')
# enemy_intention_chars_surface = pygame.image.load('data/images\\elements\\the_enemy_intentions\\chars.png')
# enemy_intention_def_surface = pygame.image.load('data/images\\elements\\the_enemy_intentions\\def.png')
# enemy_intention_hard_attack_surface = pygame.image.load('data/images\\elements\\the_enemy_intentions\\hard_attack.png')
# enemy_intention_heal_surface = pygame.image.load('data/images\\elements\\the_enemy_intentions\\heal.png')
# enemy_intention_really_hard_attack_surface = pygame.image.load(
#     'data/images\\elements\\the_enemy_intentions\\really_hard_attack.png')
# enemy_intention_small_attack_surface = pygame.image.load(
#     'data/images\\elements\\the_enemy_intentions\\small_attack.png')
#
# #enemies
# enemy_scale = 0.5
# lev1_enemy_surface = pygame.image.load(lev1_enemy)
# lev1_enemy_surface = pygame.transform.scale(lev1_enemy_surface, (lev1_enemy_surface.get_size()[0]*screen_scale*enemy_scale,lev1_enemy_surface.get_size()[1]*screen_scale*enemy_scale))
# enemy_position = (w//2, h//2-lev1_enemy_surface.get_height()//2)
#
# def draw_enemy(current_level):
#     if current_level == 1:
#         screen.blit(lev1_enemy_surface, enemy_position)
#     elif current_level == 2:
#         pass
#     #draw hp/def lines
#     hp_line_surface = pygame.image.load('data/images\\elements\\hp_def\\hp_line.png')
#     hp_line_surface = pygame.transform.scale(hp_line_surface, (screen_scale/1.5*hp_line_surface.get_width()*enemy_dict[rand_1_enemy_number][0]/enemy_dict[rand_1_enemy_number][1]-9, hp_line_surface.get_height()))
#     hp_trace_surface = pygame.image.load('data/images\\elements\\hp_def\\hp_tracing.png')
#     screen.blit(hp_line_surface, (w-hp_trace_surface.get_width()*1.1*screen_scale+9,h//2*screen_scale-screen_scale*350))
#     screen.blit(hp_trace_surface, (w-hp_trace_surface.get_width()*1.1*screen_scale,h//2*screen_scale-screen_scale*350))
#     enemy_hp_text_surface = hero_hp_text.render(str(enemy_dict[rand_1_enemy_number][0])+'/'+str(enemy_dict[rand_1_enemy_number][1])+' HP', False, (255,255,255))
#     screen.blit(enemy_hp_text_surface, (w-hp_trace_surface.get_width()*1.1*screen_scale+hp_trace_surface.get_width()//2-enemy_hp_text_surface.get_width()//2,h//2*screen_scale-screen_scale*350+hp_trace_surface.get_height()//2-enemy_hp_text_surface.get_height()//2))
#
#
# def enemy_turn(current_enemy_intention):
#     # down to zero
#     if current_enemy_intention + 1 > len(enemy_intentions_dict[rand_1_enemy_number]):
#         current_enemy_intention = 0
#     current_intention = enemy_intentions_dict[rand_1_enemy_number][current_enemy_intention]
#     if current_intention[0] == 'A':
#         hero_dict[hero_class][0] -= int(current_intention[1:])
#         pass
#
#     current_enemy_intention += 1
#     return current_enemy_intention
#
#
# def draw_enemy_intention(current_enemy_intention):
#     #down to zero
#     if current_enemy_intention+1>len(enemy_intentions_dict[rand_1_enemy_number]):
#         current_enemy_intention = 0
#     current_intention = enemy_intentions_dict[rand_1_enemy_number][current_enemy_intention]
#     if current_intention[0] == 'A':
#         if int(current_intention[1:]) <= 10:
#             screen.blit(enemy_intention_small_attack_surface,(0,0))
#         elif int(current_intention[1:]) <= 20:
#             screen.blit(enemy_intention_attack_surface,(0,0))
#         elif int(current_intention[1:]) <= 30:
#             screen.blit(enemy_intention_hard_attack_surface,(0,0))
#         else:
#             screen.blit(enemy_intention_really_hard_attack_surface,(0,0))
#     elif current_intention[0] == 'D':
#         screen.blit(enemy_intention_def_surface,(0,0))
#     elif current_intention[0] == 'C':
#         screen.blit(enemy_intention_chars_surface,(0,0))
#     elif current_intention[0] == 'H':
#         screen.blit(enemy_intention_heal_surface,(0,0))
#     elif current_intention[0] == 'C':
#         pass
#     elif current_intention[0] == 'P':
#         pass