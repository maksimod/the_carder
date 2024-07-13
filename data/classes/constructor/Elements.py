import pygame
import keyboard

from data.global_vars.button_focus import menu_buttons

class Surface:
    def get_size(self):
        return self.surface.get_size()

    def get_width(self):
        return self.surface.get_width()

    def get_height(self):
        return self.surface.get_height()

    def get_surface(self):
        return self.surface

    def draw(self, screen, pos):
        screen.blit(self.surface, pos)

    def scale(self, ex, k):
        self.surface = pygame.transform.scale(self.surface,
                                              (ex.get_width() * k, ex.get_height() * k)
                                              )
    def rotate(self,angle):
        self.surface = pygame.transform.rotate(self.surface, angle)

class Img(Surface):
    def __init__(self, screen_info, src, k=1):
        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]

        self.surface = pygame.image.load(src)
        self.surface = pygame.transform.scale(self.surface,
                                              (self.surface.get_width() * k * self.screen_scale,
                                               self.surface.get_height() * k * self.screen_scale
                                               )
                                              )

    def loadImg(self, src):
        self.surface = pygame.image.load(src)


class CardImg(Img):
    def __init__(self, screen_info,default_src, img_src, k=1):
        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]

        img_scale = 1
        self.img_surface = pygame.image.load(img_src)
        self.img_surface = pygame.transform.scale(self.img_surface,
                                              (self.img_surface.get_width() * k * self.screen_scale * img_scale,
                                               self.img_surface.get_height() * k * self.screen_scale * img_scale
                                               )
                                              )
        self.surface = pygame.image.load(default_src)
        self.surface = pygame.transform.scale(self.surface,
                                              (self.surface.get_width() * k * self.screen_scale,
                                               self.surface.get_height() * k * self.screen_scale
                                               )
                                              )

    def draw(self, screen, pos):
        screen.blit(self.surface, pos)
        screen.blit(self.img_surface, pos)

    def scale(self, ex, k):
        self.surface = pygame.transform.scale(self.surface,
                                              (ex.get_width() * k, ex.get_height() * k)
                                              )
        # img_scale = 1
        self.img_surface = pygame.transform.scale(self.img_surface,
                                              (self.img_surface.get_width() * k, self.img_surface.get_height() * k)
                                              )




class Text(Surface):
    def __init__(self, text, k=1, font=None, color=[255, 255, 255], sysFont = None):
        text_font = pygame.font.Font('data/text_fonts/menu_font.otf', int(150 * k))
        if font is not None:
            text_font = pygame.font.Font(font, int(150 * k))
        elif sysFont is not None:
            text_font = pygame.font.SysFont(font, int(150 * k))

        self.surface = text_font.render(text, False, color)

class CText(Surface):
    def __init__(self, text, k=1, font=None, color=[255, 255, 255], sysFont = None):
        if font is None and sysFont is None: sysFont='arial'

        text_font = pygame.font.Font('data/text_fonts/menu_font.otf', int(150 * k))
        if font is not None:
            text_font = pygame.font.Font(font, int(150 * k))
        elif sysFont is not None:
            text_font = pygame.font.SysFont(font, int(150 * k))

        self.surface = text_font.render(text, False, color)


class Button:

    def __init__(self, pos):
        self.pos = pos
        self.was_pressed = False
        self.was_pressed_enter = False
        self.was_pressed_down = False
        self.was_pressed_up = False

    @staticmethod
    def make_size(mode, surface, ex, src=None, txt=None, k=0.9, font='data/text_fonts/menu_font.otf', color=None):
        if color is None: color = [0, 0, 0]

        if type(surface) == Text:
            if mode == 'S':
                surface.scale(ex, k)
            elif mode == 'N':
                surface = Text(txt, k, font, color)
                surface.scale(ex, 1)
        elif type(surface) == Img:
            if mode == 'S':
                surface.scale(ex, k)
            elif mode == 'N':
                surface.loadImg(src)
                surface.scale(ex, 1)
        return surface

    def get_size(self):
        return self.surface.get_size()

    def get_w(self):
        return self.surface.get_width()

    def get_h(self):
        return self.surface.get_height()


class TextButton(Button):
    def __init__(self, button_text_info, pos, screen, index, font=None):
        text, text_size_scale, text_color = button_text_info
        self.text, self.text_size_scale, self.text_color = text, text_size_scale, text_color

        self.index = index

        self.screen = screen
        super().__init__(pos)

        light_text_color = [self.text_color[0] + 50, self.text_color[1] + 50, self.text_color[2] + 50]
        self.light_text_color = light_text_color

        self.surface = Text(text, k=text_size_scale, color=text_color)
        self.light_surface = Text(text, k=text_size_scale, color=light_text_color)

    def draw_check_click(self):
        px, py = self.pos
        bw, bh = self.surface.get_width(), self.surface.get_height() // 2
        mpx, mpy = pygame.mouse.get_pos()

        rpy = py - int(10.1 * self.text_size_scale)

        if ((px <= mpx <= px + bw) and (rpy <= mpy <= rpy + bh)):
            for i in range(len(menu_buttons)): menu_buttons[i] = False
            menu_buttons[self.index] = True

            self.light_surface.draw(self.screen, (
                px + (self.surface.get_width() - self.light_surface.get_width()) / 2,
                py - bh + (self.surface.get_height() - self.light_surface.get_height()) / 2)
                                    )
            if pygame.mouse.get_pressed()[0]:
                self.light_surface = self.make_size('S', self.light_surface, self.surface)
                self.was_pressed = True
            else:
                self.light_surface = self.make_size('N', self.light_surface, self.surface,
                                                    txt=self.text, color=self.light_text_color, k=self.text_size_scale)
                if self.was_pressed: return True
        else:
            # if self.was_pressed: return True
            self.light_surface = self.make_size('N', self.light_surface, self.surface,
                                                txt=self.text, color=self.light_text_color, k=self.text_size_scale)
            self.was_pressed = False
            if not (menu_buttons[self.index]):
                self.surface.draw(self.screen, (px, py - bh))

        # Если все еще в фокусе
        if menu_buttons[self.index]:

            if keyboard.is_pressed('up'):
                self.was_pressed_up = True
            else:
                if self.was_pressed_up:
                    self.was_pressed_up = False
                    for i in range(len(menu_buttons)): menu_buttons[i] = False
                    if self.index == 0:
                        menu_buttons[-1] = True
                    else:
                        menu_buttons[self.index - 1] = True

            if keyboard.is_pressed('down'):
                self.was_pressed_down = True
            else:
                if self.was_pressed_down:
                    self.was_pressed_down = False
                    for i in range(len(menu_buttons)): menu_buttons[i] = False
                    if self.index >= len(menu_buttons)-1:
                        menu_buttons[0] = True
                    else: menu_buttons[self.index+1] = True

            if keyboard.is_pressed('enter'):
                self.light_surface = self.make_size('S', self.light_surface, self.surface)
                self.was_pressed_enter = True
            else:
                if self.was_pressed_enter == True: return True

            self.light_surface.draw(self.screen, (
                px + (self.surface.get_width() - self.light_surface.get_width()) / 2,
                py - bh + (self.surface.get_height() - self.light_surface.get_height()) / 2)
                                    )
            #     return True





class ImgButton(Button):
    def __init__(self, screen_info, src, pos, k=1):
        self.src_dark, self.src_light = src

        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]

        self.k = k
        super().__init__(pos)

        self.surface = Img(screen_info, self.src_dark, k)
        self.surface_light = Img(screen_info, self.src_light, k)

    def draw_check_click(self, hotkey=None):
        px, py = self.pos
        bw, bh = self.surface.get_width(), self.surface.get_height() // 2
        mpx, mpy = pygame.mouse.get_pos()

        rpy = py - int(10.1 * self.k)
        if (px <= mpx <= px + bw) and (rpy - bh <= mpy <= rpy + bh):
            self.surface_light.draw(self.screen, (
                px + (self.surface.get_width() - self.surface_light.get_width()) // 2,
                py - bh + (self.surface.get_height() - self.surface_light.get_height()) // 2)
                                    )
            if pygame.mouse.get_pressed()[0]:
                self.surface_light = self.make_size('S', self.surface_light, ex=self.surface)
                self.was_pressed = True
            else:
                self.surface_light = self.make_size('N', self.surface_light, ex=self.surface, src=self.src_light)
                if self.was_pressed:
                    self.was_pressed = False
                    return True
        else:
            self.surface_light = self.make_size('N', self.surface_light, ex=self.surface, src=self.src_light)
            self.surface.draw(self.screen, (px, py - bh))
            self.was_pressed = False

        if hotkey is not None:
            if keyboard.is_pressed(hotkey):
                return True
