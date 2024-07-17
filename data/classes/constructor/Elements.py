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
        if type(ex) is tuple:
            self.surface = pygame.transform.scale(self.surface,
                                                  (ex[1].get_width() * k, ex[1].get_height() * k)
                                                  )
        else:
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

#for card class
class CardImg(Img):
    def __init__(self, screen_info,default_src, img_src, k=1):
        print(img_src)

        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]

        self.imageIsAI = False
        if 'AI' in img_src: self.imageIsAI = True

        if self.imageIsAI: img_scale = 0.3
        else: img_scale = 1
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
        if self.imageIsAI: screen.blit(self.img_surface, [pos[0]+self.surface.get_width()//4, pos[1]+self.surface.get_height()//6.5])
        else: screen.blit(self.img_surface, pos)
        screen.blit(self.surface, pos)

    def scale(self, ex, k):
        self.surface = pygame.transform.scale(self.surface,
                                              (ex.get_width() * k, ex.get_height() * k)
                                              )
        # img_scale = 1
        self.img_surface = pygame.transform.scale(self.img_surface,
                                              (self.img_surface.get_width() * k, self.img_surface.get_height() * k)
                                              )

from data.global_vars import deck, hero
class Card(Surface):

    def set_index(self,index):
        self.index = index

    def get_card(self):
        return self.card_src

    def collect_src(self):
        return deck.cards_view[self.card_src][1]

    def collect_src_name(self):
        return self.card_src

    def __init__(self, screen_info, card_src, k, index, card_chose = False, just_show=False):
        self.card_chose = card_chose
        self.just_show = just_show

        self.focus = False
        self.big_card_k = 1.5

        self.index = index

        # self.pos = pos
        self.are_pressed = False
        self.was_pressed = False
        self.was_pressed_enter = False
        self.was_pressed_down = False
        self.was_pressed_up = False

        self.card_src = card_src


        img = self.collect_src()
        default_src = 'data/images/cards/'+hero.hero_class+'/default.png'

        self.k = k
        self.surface = CardImg(screen_info, default_src,img)
        self.surface.scale(self.surface, k)

        self.big = CardImg(screen_info, default_src, img)
        self.big.scale(self.big, k * self.big_card_k)

    @staticmethod
    def transfer_description(description, number):
        res = []
        last_i = 0
        for i in range(1, len(description)):
            if i % number == 0:
                res.append(description[last_i:i])
                last_i = i
        res.append(description[last_i:])
        return res

    def draw_card_states(self):

        cost = str(deck.cards[self.card_src][0])
        self.cost = cost
        k, big_card_k = self.k, self.big_card_k
        description = deck.cards_view[self.card_src][0]

        descs = self.transfer_description(description, 13)

        cost_k = 0.6
        title_key = 0.5
        description_k = 0.5

        cost_text, f_cost_text = CText(cost, k=k * cost_k), CText(cost, k=k * cost_k * big_card_k)

        title = self.card_src
        title_text, f_title_text = CText(title, k=k * title_key), CText(title, k=k * title_key * big_card_k)

        descs_texts = []
        f_descs_texts = []
        for el in descs:
            descs_texts.append(CText(el, k=description_k * k))
            f_descs_texts.append(CText(el, k=description_k * k * big_card_k))

        # description, f_description = CText(description, k=description_k * k), CText(description, k=description_k * k * big_card_k)
        if not self.focus:
            cost_pos = (self.real_pos[0] + cost_text.get_width() // 2, self.real_pos[1] + cost_text.get_height() // 6)
            cost_text.draw(self.screen, cost_pos)

            title_pos = (self.real_pos[0]+self.surface.get_width()//2 - title_text.get_width() // 2, self.real_pos[1] + title_text.get_height() // 2)
            title_text.draw(self.screen, title_pos)

            description_pos = (self.real_pos[0] + self.bws // 8, self.real_pos[1] + self.bhs // 0.85)
            counter = 0
            for item in descs_texts:
                item.draw(self.screen, (description_pos[0], description_pos[1] + item.get_height() * counter))
                counter += 1
        else:
            f_cost_pos = (self.pxb + f_cost_text.get_width() // 2, self.pyb + f_cost_text.get_height() // 6)
            f_cost_text.draw(self.screen, f_cost_pos)

            f_title_pos = (self.pxb+self.big.get_width()//2-f_title_text.get_width()//2, self.pyb + f_title_text.get_height() // 2)
            f_title_text.draw(self.screen, f_title_pos)

            f_description_pos = (self.pxb + self.bwb//10, self.pyb + self.bhb // 0.85)
            counter = 0
            for item in f_descs_texts:
                item.draw(self.screen, (f_description_pos[0], f_description_pos[1] + item.get_height() * counter))
                counter += 1

    def live(self, screen, pos):
        self.screen = screen
        self.pos = pos
        self.screen = screen
        if self.draw_check_click(self.card_chose) == 'Play':
            return True
        self.draw_card_states()

    @staticmethod
    def make_size(mode, surface, ex, src=None, txt=None, k=1.2, font='data/text_fonts/menu_font.otf', color=None):
        if type(surface) == Img:
            if mode == 'B':
                surface.scale(ex, k)
            elif mode == 'N':
                surface.loadImg(src)
                surface.scale(ex, 1)
        return surface

    def draw_check_click(self, card_chose, hotkey=None):
        bws, bhs = self.surface.get_width(), self.surface.get_height() // 2
        bwb, bhb = self.big.get_width(), self.big.get_height() // 2
        mpx, mpy = pygame.mouse.get_pos()

        self.real_pos = [self.pos[0], self.pos[1]]

        # Check that at least one card is active
        flag = False
        for el in deck.focused_cards:
            if el:
                flag = True
                break
        if flag:
            if self.index < deck.current_active_card:
                self.real_pos[0] -= (bwb - bws) // 2
            if self.index > deck.current_active_card:
                self.real_pos[0] += (bwb - bws) // 2

        pxs, pys = self.real_pos
        pxb, pyb = pxs - (bwb - bws) // 2, self.screen.get_height() - bhb * 2

        if not (self.are_pressed) and self.was_pressed:
            if mpy > pyb:
                self.are_pressed = False
                self.was_pressed = False
                deck.focus_freeze = None
            else:
                deck.focus_freeze = None
                #check that if card apply to one of all enemies it focused at one of the enemy
                flag = True
                for el in deck.cards[self.card_src][1:]:
                    if 'E' in el:
                        flag = False
                        break
                if flag:
                    if int(self.cost)<=hero.hero[hero.hero_class][0][3]:
                        return 'Play'

        self.are_pressed = False
        if not self.focus:
            if not self.just_show:
                if (pxs <= mpx <= pxs + bws) and (pys <= mpy <= pys + bhs * 2):
                    if (deck.focus_freeze == self.index) or deck.focus_freeze is None:
                        self.focus = True
                        deck.current_active_card = self.index
                else:
                    self.focus = False
        else:
            if (deck.focus_freeze == self.index) or deck.focus_freeze is None:
                if pygame.mouse.get_pressed()[0]:
                    if not card_chose:
                        pxb, pyb = mpx - bwb // 2, mpy - bhb
                        self.are_pressed = True
                        self.was_pressed = True
                        deck.focus_freeze = self.index
                    else: return 'Play'
            if (pxb <= mpx <= pxb + bwb) and (pyb <= mpy <= pyb + bhb * 2):
                deck.current_active_card = self.index
                if (deck.focus_freeze == self.index) or deck.focus_freeze is None:
                    self.focus = True
            else:
                self.focus = False

        deck.focused_cards[self.index] = self.focus

        if self.focus:
            pass
            if card_chose: pyb -= self.surface.get_height()//6
            self.big.draw(self.screen, (pxb, pyb))
        else:
            pass
            self.surface.draw(self.screen, (pxs, pys))

        self.pxb, self.pyb = pxb, pyb
        self.bws, self.bhs, self.bwb, self.bhb = bws, bhs, bwb, bhb


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
                if self.was_pressed:
                    self.was_pressed = False
                    return True
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





class ImgButton(Button, Surface):
    def __init__(self, screen_info, src, pos, k=1):
        self.src_dark, self.src_light = src

        self.screen = screen_info[0]
        self.screen_scale = screen_info[1]

        self.k = k
        super().__init__(pos)

        self.surface = Img(screen_info, self.src_dark, k)
        self.surface_light = Img(screen_info, self.src_light, k)

    # def scale(self):

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
