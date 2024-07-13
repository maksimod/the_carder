from random import shuffle

# Card characteristics:
hand_cards_col = 6
hand_max_cards_col = 6

# [cost, attack, defense, screen/hero/enemy(0/1/2),par1, par2,...,par99]
cards = {
    'attack': [1, 6, 0, 0],
    'defense': [1, 0, 5, 0]
}

input = [['attack','defense'][i%2] for i in range(12)]
shuffle(input)
output = []

cards_input = 12
cards_output = 0

# [description, src]
cards_view = {
    'attack': ['Deal ' + str(cards['attack'][1]) + ' damage', 'data/images/cards/bercerk/attack.png'],
    'defense': ['Gain ' + str(cards['defense'][2]) + ' block', 'data/images/cards/bercerk/defense.png']
}

current_deck = {
    'attack': 6,
    'defense': 6
}

def get_deck_cards_col():
    sm = 0
    for el in current_deck.keys():
        sm+=current_deck[el]
    return sm

current_active_card = 0
focused_cards = [False for i in range(len(input))]
focus_freeze = None
