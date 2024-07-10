import pygame


class Button:
    def __init__(self, text, text_size_scale, text_color, pos, screen, font=None):
        self.screen = screen
        self.pos = pos

        self.light_text_color = [text_color[0] - 50, text_color[1] - 50, text_color[2] - 50]

        if not font:
            self.text = pygame.font.Font('data/text_fonts/menu_font.otf', int(150 * text_size_scale))
        else:
            self.text = pygame.font.Font(font, int(150 * text_size_scale))

        self.text_surface = self.text.render(text, False, text_color)
        self.light_text_surface = self.text.render(text, False, text_color)

    def draw_check_click(self):
        px = self.pos[0]
        py = self.pos[0]
        bw, bh = self.text_surface.get_size()
        mpx, mpy = pygame.mouse.get_pos()

        if (px <= mpx <= px + bw) and (py <= mpy <= py + bh):
            self.screen.blit(self.light_text_surface, self.pos)
        else:
            self.screen.blit(self.text_surface, self.pos)