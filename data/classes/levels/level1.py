# backgrounds
import random


class Level1:
    def __init__(self):
        self.background = 'data/images\\lev1\\backs\\back' + str(random.randrange(2)) + '.png'
        self.ways = "FD"
        self.enemy_type = 'images\\lev1\\enemies\\guard' + str(random.randrange(4)) + '.png'

    def return_lev_info(self):
        return self.background, self.ways, self.enemy_type