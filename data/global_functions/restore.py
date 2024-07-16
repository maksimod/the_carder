from random import shuffle
from data.global_vars import deck, hero, enemies

def null_deck_parameters():
    deck.current_deck = deck.null_current_deck
    deck.input = []
    for el in deck.current_deck.keys():
        for i in range(deck.current_deck[el]):
            deck.input.append(el)
    shuffle(deck.input)
    deck.output = []

    deck.cards_input = len(deck.input)
    deck.cards_output = 0

    deck.hand_cards_col = deck.hand_max_cards_col

def restore_deck_parameters():
    deck.input = []
    for el in deck.current_deck.keys():
        for i in range(deck.current_deck[el]):
            deck.input.append(el)
    shuffle(deck.input)
    deck.output = []

    deck.cards_input = len(deck.input)
    deck.cards_output = 0

def restore_hero_parameters():
    hero.hero[hero.hero_class][0][0] = hero.hero[hero.hero_class][1][0]
    hero.hero[hero.hero_class][0][1] = 0
    for i in range(len(hero.hero_debuffs)): hero.hero[hero.hero_class][0][-1][i] = 0
    for i in range(len(hero.hero_buffs)): hero.hero[hero.hero_class][0][-2][i] = 0

def restore_enemy_parameters():
    #restore hp
    for type in enemies.enemies.keys():
        if '&' in type: continue
        enemies.enemies[type][0][0] = enemies.enemies[type][1][0]
        #restore buffs/debuffs
        for i in range(len(enemies.enemy_debuffs)): enemies.enemies[type][0][-1][i] = 0
        for i in range(len(enemies.enemy_buffs)): enemies.enemies[type][0][-2][i] = 0


def null_parameters():
    null_deck_parameters()
    restore_hero_parameters()
    restore_enemy_parameters()

def next_level_parameters():
    restore_deck_parameters()
    restore_hero_parameters()
    restore_enemy_parameters()