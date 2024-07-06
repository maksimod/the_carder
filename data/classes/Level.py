from data.classes.levels.level1 import Level1
from data.classes.Enemy import Enemy


class Level:
    def __init__(self):
        self.background = self.enemy_type = self.ways = None
        self.current_level = 1
        self.last_level = 0

        # self.background, self.ways, self.enemy_type
        self.level_characters = [i for i in range(3)]
        self.lev = eval("Level" + str(self.current_level))
        self.enemy = Enemy

    def level_was_changed(self):
        if self.last_level!=self.current_level:
            self.last_level = self.current_level
            return True
        return False

    def draw(self, screen,screen_scale):
        if self.level_was_changed():
            self.lev = eval("Level"+str(self.current_level))
            self.level_characters = self.lev(screen_scale).return_lev_info()
            self.background, self.ways, self.enemy_type = self.level_characters
            self.enemy(self.enemy_type)
            # print(self.level_characters)
        screen.blit(self.background, (0, 0))

        pass
