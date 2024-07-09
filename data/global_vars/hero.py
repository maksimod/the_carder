# player_type: [[hp,def,rage,mp,poison,attack]
hero_states = {
    'bercerk': [140,0,0,4,0,0]
}
# player_type: [(current)[hp,def,rage,mp,poison,attack],(max)[hp,def,rage,mp,poison,attack], image_path]
hero = {
    'bercerk': [hero_states['bercerk'],hero_states['bercerk'],'data/images\\heroes\\bercerk.png']
}


# #hero
# hero_class = 'bercerk'
#
# #heroes
# hero_scale = 0.5
# bercerc_surface = pygame.image.load('data/images\\heroes\\bercerk.png')
# bercerc_surface = pygame.transform.scale(bercerc_surface, (bercerc_surface.get_size()[0]*screen_scale*hero_scale,bercerc_surface.get_size()[1]*screen_scale*hero_scale))
# hero_position = (0, h//2-lev1_enemy_surface.get_height()//2)