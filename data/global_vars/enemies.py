
# A - attack, H - heal, B - buff, D - def, C - curse, P - low curse, S - Summon Slave
# 'enemy_name': [cur_hp,max_hp, ['intention1','intention2', 'intention3'], img_path]
enemies = {
    'guardian' : [[60,0],[60,999],['A9','D10', 'A18'],'data/images/enemies/guardian11.png'],
    'wizard' : [[50,0],[50,999],['H20','D30', 'A20'],'data/images/enemies/wizard11.png'],
    'snakes' : [[50,0],[50,999],['P4','H20'],'data/images/enemies/snakes11.png'],
    'joker' : [[40,0],[40,999],['S99','H15', 'A10'], 'data/images/enemies/joker11.png']
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
    'C': None,
    'S': 'data/images\\elements\\the_enemy_intentions\\question.png',
    'P': 'data/images\\elements\\the_enemy_intentions\\poison.png'
}

level_enemy_types = {
    1: ['guardian', 'wizard', 'snakes', 'joker'],
    2: None
}
