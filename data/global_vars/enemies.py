
# A - attack, H - heal, B - buff, D - def, C - (boss) curse, L - (debuff), P - low curse, S - Summon Slave

#B buffs: S - strength (always increase current attack by strength)
#L debuffs (every turn decreases by 1):
    # V - vulnerable (hero will get x% more damage), PV3  hero will vulnerable 3 turns
    # B - sleeding (hero will lose (bleeding) hp)
    # W - attacks will deal 25% less damage
#P low curse (static, all battle with player, it can increase):
    # F - fragile (1 fragile point = hero will get 1 less defense), PF3 = hero will get 3 less damage every time


#[poison, vulnerable, fragile, weak]
enemy_debuffs = [0,0,0,0]
debuffs_indexes = {
    'poison':0,
    'vulnerable':1,
    'fragile':2,
    'weak':3
}

#[strength, barricade]
enemy_buffs = [0,0]
buffs_indexes = {
    'S': 0,
    'B': 1
}

# 'enemy_name': [cur_hp,cur_df, ], [max_hp,max_df] ['intention1','intention2', 'intention3'], img_path]
enemies = {
    'guardian' : [[60,0, enemy_buffs, enemy_debuffs],[60],['A9','D15', 'A18'],'data/images/enemies/guardian11.png'],
    'wizard' : [[50,0,enemy_buffs, enemy_debuffs],[50],['A20', 'D12', 'A13','H18'],'data/images/enemies/wizard11.png'],
    'snakes' : [[50,0, enemy_buffs, enemy_debuffs],[50],['P5','H10'],'data/images/enemies/snakes11.png'],
    'joker' : [[40,0, enemy_buffs, enemy_debuffs],[40],['S99','A10', 'D15'], 'data/images/enemies/joker11.png'],
    'fear': [[60, 0, enemy_buffs, enemy_debuffs], [60], ['BS3', 'A1'], 'data/images/enemies/AI/fear.png'],
    'fear_ghost': [[50, 0, enemy_buffs, enemy_debuffs], [50], ['LV3', 'A15', 'A12', 'A9', 'D10'], 'data/images/enemies/AI/fear_ghost.png'],
    'flowers': [[50, 0, enemy_buffs, enemy_debuffs], [50], ['PF2', 'A12','LV2', 'A10', 'BS2'], 'data/images/enemies/AI/flowers.png'],
    'flowers2': [[40, 0, enemy_buffs, enemy_debuffs], [40], ['BS4', 'A4','LW2', 'A9'], 'data/images/enemies/AI/flowers2.png'],


    'buff_check': [[40, 0, enemy_buffs, enemy_debuffs], [40], ['BS4', 'A4','LW2', 'A9'], 'data/images/enemies/AI/flowers2.png'],
}

# [-player_hp, +enemy_hp, +enemy_df, +player_poison, +slave ...]

enemy_buff_index = 'buffs_indexes[current_intention[1]]'

intention_actions = {
    'D': ['enemies[self.enemy_type][0][1]+'],
    'H': ['enemies[self.enemy_type][0][0]+'],
    'P': ['hero.hero[hero.hero_class][0][-1][hero.debuffs_indexes["poison"]]+'],
    'B': ['enemy_buffs['+enemy_buff_index+']+']

}
enemy_intentions = {
    'A': {
        '10': 'data/images\\elements\\the_enemy_intentions\\small_attack.png',
        '20': 'data/images\\elements\\the_enemy_intentions\\attack.png',
        '40': 'data/images\\elements\\the_enemy_intentions\\hard_attack.png',
        '100000': 'data/images\\elements\\the_enemy_intentions\\really_hard_attack.png'
    },
    'H': 'data/images\\elements\\the_enemy_intentions\\heal.png',
    'B': 'data/images\\elements\\the_enemy_intentions\\chars.png',
    'D': 'data/images\\elements\\the_enemy_intentions\\def.png',
    'C': 'data/images\\elements\\the_enemy_intentions\\def.png',
    'S': 'data/images\\elements\\the_enemy_intentions\\question.png',
    'P': 'data/images\\elements\\the_enemy_intentions\\poison.png'
}

level_enemy_types = {
    # 1: ['guardian', 'wizard', 'snakes', 'joker'],
    # 2: ['fear', 'fear_ghost', 'flowers', 'flowers2']
    3: ['buff_check']
}
