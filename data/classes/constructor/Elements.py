import pygame
import keyboard

class Img:
    def __init__(self, screen_info, src, k=1):
        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]

        self.surface = pygame.image.load(src)
        self.surface = pygame.transform.scale(self.surface,
                                              (self.surface.get_width() * k * self.screen_scale,
                                               self.surface.get_height() * k * self.screen_scale
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


class Text:
    def __init__(self, screen_info, text, k=1, font=None, color=[0, 0, 0]):
        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]

        text_font = pygame.font.Font('data/text_fonts/menu_font.otf', int(150 * k))
        if font is not None: text_font = pygame.font.Font(font, int(150 * k))
        self.text_surface = text_font.render(text, False, color)

    def get_w(self):
        return self.text_surface.get_width()

    def get_h(self):
        return self.text_surface.get_height()

    def draw(self, pos):
        self.screen.blit(self.text_surface, pos)

    def get_surface(self):
        return self.text_surface


class TextButton:
    def __init__(self, button_text_info, pos, screen, font=None):
        self.text, self.text_size_scale, self.text_color = button_text_info

        self.screen = screen
        self.pos = pos

        self.was_pressed = False

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
            self.screen.blit(self.light_text_surface, (
                px+(self.text_surface.get_width()-self.light_text_surface.get_width())//3,
                py - bh + (self.text_surface.get_height()-self.light_text_surface.get_height())//2)
            )
            if pygame.mouse.get_pressed()[0]:
                self.light_text_surface = pygame.transform.scale(self.light_text_surface,
                        (self.text_surface.get_width() * 0.9,
                        self.text_surface.get_height() * 0.9
                    )
                )
                self.was_pressed = True
            else:
                self.light_text_surface = pygame.transform.scale(self.light_text_surface,
                        (self.text_surface.get_width(), self.text_surface.get_height())
                )
                if self.was_pressed: return True
        else:
            self.was_pressed = False
            self.screen.blit(self.text_surface, (px, py - bh))

    def get_size(self):
        return self.text_surface.get_size()

    def get_w(self):
        return self.text_surface.get_width()

    def get_h(self):
        return self.text_surface.get_height()


class ImgButton:
    def __init__(self, screen_info, src, pos, k=1):
        self.src_dark,self.src_light = src

        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]

        self.k = k
        self.pos = pos

        self.was_pressed = False

        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]

        self.surface = pygame.image.load(self.src_dark)
        self.surface = pygame.transform.scale(self.surface,
                                              (self.surface.get_width() * k * self.screen_scale,
                                               self.surface.get_height() * k * self.screen_scale
                                               )
        )

        self.surface_light = pygame.image.load(self.src_light)
        self.surface_light = pygame.transform.scale(self.surface_light,
                                              (self.surface_light.get_width() * k * self.screen_scale,
                                               self.surface_light.get_height() * k * self.screen_scale
                                               )
        )

    def draw_check_click(self, hotkey=None):
        px, py = self.pos
        bw, bh = self.surface.get_width(), self.surface.get_height() // 2
        mpx, mpy = pygame.mouse.get_pos()

        rpy = py - int(10.1 * self.k)
        if (px <= mpx <= px + bw) and (rpy - bh <= mpy <= rpy + bh):
            self.screen.blit(self.surface_light, (
                px + (self.surface.get_width()-self.surface_light.get_width())//2,
                py - bh + (self.surface.get_height()-self.surface_light.get_height())//2)
            )
            if pygame.mouse.get_pressed()[0]:
                self.surface_light = pygame.transform.scale(self.surface_light,
                        (self.surface.get_width() * 0.9,
                        self.surface.get_height() * 0.9
                    )
                )
                self.was_pressed = True
            else:
                self.surface_light = pygame.image.load(self.src_light)
                self.surface_light = pygame.transform.scale(self.surface_light,
                                                            (self.surface.get_width(), self.surface.get_height()))
                if self.was_pressed: return True
        else:
            self.screen.blit(self.surface, (px, py - bh))

        if hotkey is not None:
            if keyboard.is_pressed(hotkey):
                return True

    def get_size(self):
        return self.surface.get_size()

    def get_w(self):
        return self.surface.get_width()

    def get_h(self):
        return self.surface.get_height()
