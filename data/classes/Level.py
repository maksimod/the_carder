from data.classes.levels.level1 import Level1


class Level:
    def __init__(self):
        self.current_level = 1
        self.back_image_name = 'data/images/menu/back.png'

        # self.background, self.ways, self.enemy_type
        self.level_characters = [i for i in range(3)]
        self.draw("dd")

    def level_was_changed(self): return True

    def draw(self, screen):
        if self.level_was_changed():
            self.level_characters = eval("Level"+str(self.current_level)+"()").return_lev_info()
            print(self.level_characters)
        # screen.blit(self.menu_text_new_game_surface, (0, 0))
        pass
