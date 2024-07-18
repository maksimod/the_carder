from data.classes.constructor.Elements import Card
from data.global_vars.screen_info import *
from data.global_vars import deck, hero, enemies

from time import *
from random import shuffle


class Deck:

    def __init__(self, enemy, player):
        self.enemy,self.player = enemy,player

        if deck.hand_cards_col<=6:
            k = 0.4
        else:
            k = 0.4 - (deck.hand_cards_col-6)*0.03

        #convert card names to real cards!
        for i in range(len(deck.input)):
            deck.input[i] = Card(deck.input[i], k, i)

        self.cards = []
        for i in range(deck.hand_cards_col):
            self.cards.append(deck.input[0])
            deck.input.pop(0)
            deck.cards_input-=1

    def take_cards(self):
        for i in range(len(self.cards)):
            deck.output.append(self.cards[0])
            del self.cards[0]
            deck.cards_output+=1

        for i in range(deck.hand_max_cards_col):
            if deck.input:
                self.cards.append(deck.input[0])
                deck.input.pop(0)
                deck.cards_input-=1
            else:
                deck.input = deck.output
                deck.output = []
                deck.cards_output = 0
                deck.cards_input = len(deck.input)
                shuffle(deck.input)
                self.cards.append(deck.input[0])
                deck.input.pop(0)
                deck.cards_input-=1

        deck.hand_cards_col = deck.hand_max_cards_col

        for i in range(len(self.cards)):
            self.cards[i].set_index(i)

    def play_card(self, src, card):
        cost = deck.cards[src][0]

        #Check for elements and make actions
        for action in deck.cards[src][1:]:
            if action[0] == 'A':
                #ATTACK ENEMY
                if action[1] == 'A':
                    attack = int(action[2:])
                    for el in self.enemy.get_names():
                        if enemies.enemies[el][0][1] <= 0:
                            enemies.enemies[el][0][0] -= attack
                        else:
                            if enemies.enemies[el][0][1] - attack >= 0:
                                enemies.enemies[el][0][1] -= attack
                            else:
                                attack -= enemies.enemies[el][0][1]
                                enemies.enemies[el][0][1] = 0
                                enemies.enemies[el][0][0] -= attack
                # elif
            elif action[0] == 'P':
                if action[1] == 'D':
                    defence = int(action[2:])
                    hero.hero[hero.hero_class][0][1] += defence
            else:
                raise NameError('You did not add E support already')

        hero.hero[hero.hero_class][0][3] -= cost

        deck.output.append(card)
        deck.cards_output+=1

        return True

    def draw(self):
        # print(deck.hand_cards_col)
        
        cards = self.cards
        focused_card_index = -1
        flag = False
        index_rewrite = False
        rewrite_index = -1
        for i in range(len(deck.focused_cards)):
            # print(deck.focused_cards, i)
            if not (deck.focused_cards[i]):
                card_pos_x = screen_size[0] // 2 - (cards[0].get_width() * deck.hand_cards_col) // 2 + i * cards[
                    0].get_width()
                card_pos_y = screen_size[1] - cards[0].get_height()
                if cards[i].live((card_pos_x, card_pos_y)) == True:
                    if self.play_card(cards[i].get_card(), cards[i]):
                        # pass
                        del cards[i]
                        deck.hand_cards_col -= 1
                        deck.focused_cards = [False for i in range(deck.hand_cards_col)]
                        index_rewrite = True
                        rewrite_index = i
                        break
            else:
                focused_card_index = i
                flag = True
        if flag:
            i = focused_card_index
            card_pos_x = screen_size[0] // 2 - (cards[0].get_width() * deck.hand_cards_col) // 2 + i * cards[
                0].get_width()
            card_pos_y = screen_size[1] - cards[0].get_height()
            if cards[i].live((card_pos_x, card_pos_y)) == True:
                if self.play_card(cards[i].get_card(), cards[i]):
                    del cards[i]
                    deck.hand_cards_col -= 1
                    deck.focused_cards = [False for i in range(deck.hand_cards_col)]
                    index_rewrite = True
                    rewrite_index = i
                    
        # rewrite card indexes:
        if index_rewrite:
            for i in range(len(deck.focused_cards)):
                if cards[i].index > rewrite_index:
                    cards[i].index -= 1