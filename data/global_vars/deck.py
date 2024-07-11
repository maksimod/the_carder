# Card characteristics:
cards_col = 6

# [cost, attack, defense, par1, par2,...,par99]
cards = {
    'attack': [1,6,0,0],
    'defense': [1,0,5,0]
}

# [description, src]
cards_view = {
    'attack': ["Attack enemy by "+str(cards['attack'][1]), 'data/images/cards/bercerk/attack.png'],
    'defense': ["Increase your defense by "+str(cards['defense'][2]), 'data/images/cards/bercerk/defense.png']
}

current_deck = {
    'attack': 6,
    'defense': 6
}

current_active_card = 0
focused_cards = [False for i in range(cards_col)]