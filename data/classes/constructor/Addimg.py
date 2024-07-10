import pygame
class Addimg:
    def __init__(self, screen_info, src, k=1):
        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]

        self.surface = pygame.image.load(src)
        if k!=1: self.surface = pygame.transform.scale(self.surface,
      (self.surface.get_width()*k*self.screen_scale,
            self.surface.get_height()*k*self.screen_scale
            )
        )

    def draw(self, pos):
        self.screen.blit(self.surface, pos)

    def get_size(self):
        return self.surface.get_size()

    def get_w(self):
        return self.surface.get_width()

    def get_h(self):
        return self.surface.get_height()

    def get_surface(self):
        return self.surface