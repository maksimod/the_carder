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
    deck.hand_cards_col = deck.hand_max_cards_col
    
    deck.focused_cards = [False for _ in range(deck.hand_cards_col)]

def null_parameters():
    null_deck_parameters()

def next_level_parameters():
    restore_deck_parameters()