# 'enemy_name': [cur_hp,cur_df, [buffs], [debuffs]], [max_hp] ['intention1','intention2', 'intention3'], img_path]
enemies = {
    'guardian' : [[60,0],[60],['A9','D15', 'A18'],'data/images/enemies/guardian11.png'],
    'wizard' : [[50,0],[50],['A20', 'D12', 'A13','H18'],'data/images/enemies/wizard11.png'],
    'snakes' : [[50,0],[50],['P5','H10'],'data/images/enemies/snakes11.png'],
    'joker' : [[40,0],[40],['S99','A10', 'D15'], 'data/images/enemies/joker11.png'],
    'fear': [[60, 0], [60], ['BS3', 'A1'], 'data/images/enemies/AI/fear.png'],
    'fear_ghost': [[50, 0], [50], ['LV3', 'A15', 'A12', 'A9', 'D10'], 'data/images/enemies/AI/fear_ghost.png'],
    'flowers': [[50, 0], [50], ['PF2', 'A12','LV2', 'A10', 'BS2'], 'data/images/enemies/AI/flowers.png'],
    'flowers2': [[40, 0], [40], ['BS4', 'A4','LW2', 'A9'], 'data/images/enemies/AI/flowers2.png'],

    'buff_check': [[40, 0], [40], ['A4','BS4'], 'data/images/enemies/AI/flowers2.png'],

    'wizard&guardian': ['wizard','guardian']
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
    # 1: ['wizard&guardian'],
    1: ['snakes'],
    # 1: ['guardian', 'wizard', 'snakes', 'joker'],
    2: ['fear', 'fear_ghost', 'flowers', 'flowers2']
    # 3: ['wizard&guardian']
}
