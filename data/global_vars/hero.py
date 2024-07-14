# player_type: [[hp,def,rage,mp,poison,attack]

#[poison, vulnerable, fragile, weak]
hero_debuffs = [0,0,0,0]

debuffs_indexes = {
    'poison':0,
    'vulnerable':1,
    'fragile':2,
    'weak':3
}

#[strength, barricade, card_increase, mp_increase]
hero_buffs = [0,0,0,0]

buffs_indexes = {
    'strength':0,
    'barricade':1,
    'card_increase':2,
    'mp_increase':3
}

# player_type: [(current)[hp,def,rage,mp, hero_debuffs],(max)[hp,mp], image_path]
hero = {
    'bercerk': [[140,0,0,3,hero_buffs,hero_debuffs],[140,3],'data/images\\heroes\\bercerk_hero.png'],
    'isolda': [[110,0,0,4,hero_buffs,hero_debuffs],[110,3],'data/images\\heroes\\isolda.png'],
    'joker': [[90,0,0,3,hero_buffs,hero_debuffs],[90,3],'data/images\\heroes\\joker.png'],
    'princess': [[80,0,0,3,hero_buffs,hero_debuffs],[80,3],'data/images\\heroes\\princess.png']
}
# #hero
hero_class = 'bercerk'