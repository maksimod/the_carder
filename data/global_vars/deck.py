# Card characteristics:
cards_col = 6
max_cards_col = 6
cards_input = 12
cards_output = 0

# [cost, attack, defense, screen/hero/enemy(0/1/2),par1, par2,...,par99]
cards = {
    'attack': [1, 6, 0, 0],
    'defense': [1, 0, 5, 0]
}

# [description, src]
cards_view = {
    'attack': ['Deal ' + str(cards['attack'][1]) + ' damage', 'data/images/cards/bercerk/attack.png'],
    'defense': ['Gain ' + str(cards['defense'][2]) + ' block', 'data/images/cards/bercerk/defense.png']
}

current_deck = {
    'attack': 6,
    'defense': 6
}

current_active_card = 0
focused_cards = [False for i in range(cards_col)]
focus_freeze = None
