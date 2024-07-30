import sys

import pygame
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN


# pygame.constants необходим для создания условия выхода из цикла


# далее создаем функцию my_animation, принимающая следующие аргументы w1, h1 - количество спрайтов в строке и столбце изображения, k - это общее количество кадров в изображении, fps - количество кадров в секунду, name - название и путь к изображению, position - положение анимации на игровом экране.

class Animation:
    def __init__(self, w1, h1, k, fps, name, position):
        self.counter = 0
        self.fps = fps
        self.k = k
        
        self.position = position
        
        # список для хранения кадров и таймер
        self.animation_frames = []
        self.timer = pygame.time.Clock()
        
        # создаем экран и загружаем изображение в переменную sprite, установив методом convert_alpha необходимую прозрачность
        self.scr = pygame.display.set_mode((800, 800), 0, 32)
        sprite = pygame.image.load("{0}.png".format(name)).convert_alpha()
        
        # находим длину, ширину изображения и размеры каждого кадра
        width, height = sprite.get_size()
        w, h = width / w1, height / h1
        
        # счетчик положения кадра на изображении
        row = 0
        
        # итерация по строкам
        for j in range(int(height / h)):
            # производим итерацию по элементам строки
            for i in range(int(width / w)):
                # добавляем  в список отдельные кадры
                self.animation_frames.append(sprite.subsurface(pygame.Rect(i * w, row, w, h)))
            # смещаемся на высоту кадра, т.е. переходим на другую строку
            row += int(h)
    
    
    def draw(self):
        self.scr.fill((255, 0, 0))
        self.scr.blit(self.animation_frames[self.counter], self.position)
        
        self.counter = (self.counter + 1) % self.k
        
        # обновляем экран
        pygame.display.update()
        self.timer.tick(self.fps)
        

if __name__ == "__main__":
    x = float(input("Fps:"))
    my_anim = Animation(8, 1, 8, x, "data/animations/primer/primer", (300, 300))
    
    while True:
        # условие выхода из цикла - нажатие клавиши ESCAPE
        for evt in pygame.event.get():
            if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
                sys.exit()
        
        my_anim.draw()
