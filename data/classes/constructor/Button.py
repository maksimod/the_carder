import pygame


class Button:
    def __init__(self, button_text_info, pos, screen, font=None):
        self.text, self.text_size_scale, self.text_color = button_text_info

        self.screen = screen
        self.pos = pos

        self.light_text_color = [self.text_color[0] + 50, self.text_color[1] + 50, self.text_color[2] + 50]

        self.text_font = pygame.font.Font('data/text_fonts/menu_font.otf', int(150 * self.text_size_scale))
        if font is not None: self.text_font = pygame.font.Font(font, int(150 * self.text_size_scale))

        self.text_surface = self.text_font.render(self.text, False, self.text_color)
        self.light_text_surface = self.text_font.render(self.text, False, self.light_text_color)

    def draw_check_click(self):
        px, py = self.pos
        bw, bh = self.text_surface.get_width(), self.text_surface.get_height() // 2
        mpx, mpy = pygame.mouse.get_pos()

        rpy = py - int(10.1 * self.text_size_scale)
        if (px <= mpx <= px + bw) and (rpy <= mpy <= rpy + bh):
            self.screen.blit(self.light_text_surface, (px, py - bh))
            if pygame.mouse.get_pressed()[0]: return True
        else:
            self.screen.blit(self.text_surface, (px, py - bh))

    def get_size(self):
        return self.text_surface.get_size()

    def get_w(self):
        return self.text_surface.get_width()

    def get_h(self):
        return self.text_surface.get_height()
