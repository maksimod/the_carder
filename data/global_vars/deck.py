from random import shuffle

# Card characteristics:
hand_cards_col = 6
hand_max_cards_col = 6

# [cost, attack, defense, screen/hero/enemy(0/1/2),
#   enemy_negatives, enemy_positives, player_negatives, player_positivs]

# ~ before number means that this parameter will save during battle;
# - means that it will be decreased by 1 every turn
# + means that it will be increased by 1 every turn
# you can use --/---/... or ++/+++... to say on ehat value it will decrease/increase
#enemy_negatives: [vulnerable, weak, poison, bleeding, anxiety, strength_lost]
#enemy_positievs: [strength, dexterity, barricade]

#player_negatives: [vulnerable, weak, poison, bleeding, anxiety, strength_lost]
#player_positievs: [strength, dexterity, barricade, ..., more_cards_col]

#player talants: [poison,]

#M2 - hero lose 2 mp;
#AA2 - attack all (enemies) by 2
#D5 - defense by 5
#H - heal
#EFFECTS:
#B - buff, C - (boss) curse, L - (debuff), P - low curse, S - Summon Slave

#B buffs: S - strength (always increase current attack by strength)
#L debuffs (every turn decreases by 1):
    # V - vulnerable (hero will get x% more damage), PV3  hero will vulnerable 3 turns
    # B - sleeding (hero will lose (bleeding) hp)
    # W - attacks will deal 25% less damage
#P low curse (static, all battle with player, it can increase):
    # F - fragile (1 fragile point = hero will get 1 less defense), PF3 = hero will get 3 less damage every time

#HOW IT COMMAND? BSH5 - increase hero strength by 5; BSA5 - increase all enemies strength by 5
# first letter - A(all enemies)/E(current enemy)/P(hero action)
cards = {
    'attack': [1,'AA6'],
    'defense': [1,'PD5'],
    'crushHead': [2, 'AA9', 'ALV2']
}

null_current_deck = {
    'attack': 6,
    'defense': 6,
}

current_deck = {
    'attack': 6,
    'defense': 6,
}

input = []
for el in current_deck.keys():
    for i in range(current_deck[el]):
        input.append(el)
shuffle(input)
output = []

cards_input = len(input)
cards_output = 0


described_characteristics = {
    'vulnerable': 'target will get 25% more damage'
}


# [description, src]
cards_view = {
    'attack': ['Deal ' + str(cards['attack'][1][2:]) + ' damage. I am a big fan of fan to eat boob', 'data/images/cards/bercerk/attack.png'],
    'defense': ['Gain ' + str(cards['defense'][1][2:]) + ' block', 'data/images/cards/bercerk/defense.png'],
    'crushHead': ['Attack ' + str(cards['crushHead'][1][2:]) + ' and apply ' + str(cards['crushHead'][2][3:]) +
                 ' vulnerable to enemy', 'data/images/cards/bercerk/AI/crushHead.jpeg'],
}
get_cards_depend_hero_class = {
    'bercerk': ['attack','defense','crushHead']
    # 'bercerk': ['crushHead', 'evilDeal', 'bandage', 'ironAttack', 'barricade', 'attackDefense',
    #             'forrager', 'rageAttack', 'rageDefense', 'screamer', 'stranger', 'breakfast', 'myCuteDragon'],
    # 'isolda': ['judje', 'magicIce', 'magicFire', 'magicHypno', 'mysteryPotion', 'darkMagic', 'dead'],
    # 'joker': ['marshmallion', 'gruminion', 'sleep', 'blackJack', 'joke', 'FUN', 'chaos',
    #           'wordplay'],
    # 'princess': ['removeCrown', 'throwCrown', 'putOnTheCrown', 'turn away', 'cry', 'hysterics',
    #              'depression', 'calm', 'curseGod', 'thankGod', 'scream', 'shutup', 'inject', 'rage', 'betweenLifeAndDeath']
}

current_active_card = 0
focused_cards = [False for i in range(len(input))]
focus_freeze = None
