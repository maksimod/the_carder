# backgrounds
import random
import pygame


class Level1:
    def __init__(self,screen_scale):
        self.background = pygame.image.load('data/images\\lev1\\backs\\back' + str(random.randrange(2)) + '.png')
        self.background = pygame.transform.scale(self.background, (
            self.background.get_size()[0] * screen_scale,
            self.background.get_size()[1] * screen_scale))
        self.ways = 'FD'
        self.enemy_type = 'images\\lev1\\enemies\\guard' + str(random.randrange(4)) + '.png'

    def return_lev_info(self):
        return self.background, self.ways, self.enemy_type
