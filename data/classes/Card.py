#Cards
menu_text_the_carder_surface = menu_text_the_carder.render('The Carder', False, text_color)
card_scale = 1.5
bercerc_attack_card_surface = pygame.image.load('data/images\\cards\\bercerk\\attack.png')
bercerc_attack_card_surface = pygame.transform.scale(bercerc_attack_card_surface, (bercerc_attack_card_surface.get_size()[0]*screen_scale//2,bercerc_attack_card_surface.get_size()[1]*screen_scale//2))
bercerc_defense_card_surface = pygame.image.load('data/images\\cards\\bercerk\\defense.png')
bercerc_defense_card_surface = pygame.transform.scale(bercerc_defense_card_surface, (bercerc_defense_card_surface.get_size()[0]*screen_scale//2,bercerc_defense_card_surface.get_size()[1]*screen_scale//2))
card_size = bercerc_attack_card_surface.get_size()
all_cards = {
    0: bercerc_attack_card_surface,
    1: bercerc_defense_card_surface
}
all_cards_states = {
    #[mp, attk, def, rage, sv1,sv2]
    0: [1,6,0,0,'',''],
    1: [1,0,5,0,'','']
}
all_cards_descriptions = {
    #[mp, attk, def, opisanie, rage, sv1,sv2]
    0: "Attack enemy by "+str(all_cards_states[0][1]),
    1: "Increase your defense by "+str(all_cards_states[1][2])
}
given_cards_surfaces = []
given_cards_surfaces_names = []
for i in range(6):
    rand_surface = random.randint(0, len(all_cards)-1)
    given_cards_surfaces.append(all_cards[rand_surface])
    given_cards_surfaces_names.append(rand_surface)

def draw_card_text(card_index, card_size, card_scale, card_translation, is_active):
    text_energy_size = 30
    text_description_size = 20
    card_energy = all_cards_states[card_index][0]
    card_description = all_cards_descriptions[given_cards_surfaces_names[counter]]
    card_description_text_mas = []
    #\n doesn not working in ... .render("cmcmc \n nhii")!
    sym_col = 20
    for i in range(0,len(card_description), sym_col):
        card_description_text_mas.append(card_description[i:i+sym_col])
    if vulnerable:
        card_energy *= 2
    if is_active:
        card_energy_text = pygame.font.Font(None, int(text_energy_size*text_size_scale*card_scale))
        card_description_text = pygame.font.Font(None, int(text_description_size*text_size_scale*card_scale))
        for i in range(len(card_description_text_mas)):
            card_description_text_surface = card_description_text.render(card_description_text_mas[i], False, (255,255,255))
            screen.blit(card_description_text_surface,(card_translation[0]+10*card_scale,card_translation[1]+card_size[1]//1.2+card_description_text_surface.get_height()*i))
    else:
        card_energy_text = pygame.font.Font(None, int(text_energy_size*text_size_scale))
        card_description_text = pygame.font.Font(None, int(text_description_size*text_size_scale))
        card_description_text_surface = card_description_text.render(str(card_description), False, (255,255,255))
        for i in range(len(card_description_text_mas)):
            card_description_text_surface = card_description_text.render(card_description_text_mas[i], False, (255,255,255))
            screen.blit(card_description_text_surface,(card_translation[0]+10*card_scale,card_translation[1]+card_size[1]//2+card_description_text_surface.get_height()+card_description_text_surface.get_height()*i))
    card_energy_text_surface = card_energy_text.render(str(card_energy), False, (255,255,255))
    screen.blit(card_energy_text_surface,(card_translation[0]+card_energy_text_surface.get_width()//2,card_translation[1]+card_energy_text_surface.get_height()//4))
