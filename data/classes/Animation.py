import pygame
from data.global_vars.screen_info import *
import time
class Animation:
    def __init__(self, frames_number, fps, folder_path, position, frame_scale = 1, looped = True):
        self.looped = looped
        self.hide = False
        
        self.millis = time.time()
        
        self.frames_number = frames_number
        self.counter = 0
        self.fps = fps
        
        self.position = position
        
        # список для хранения кадров и таймер
        self.animation_frames = []
        self.timer = pygame.time.Clock()
        
        # создаем экран и загружаем изображение в переменную sprite, установив методом convert_alpha необходимую прозрачность
        # self.scr = pygame.display.set_mode((800, 800), 0, 32)
        self.scr = screen
        
        
        for i in range(frames_number):
            fr_num = str(i)
            if i<10:
                fr_num = '0'+fr_num
            
            self.animation_frames.append(pygame.image.load(folder_path+'/frame_'+fr_num+'.png'))
            self.animation_frames[-1] = pygame.transform.scale(self.animation_frames[-1],(
                self.animation_frames[-1].get_width() * frame_scale,
                self.animation_frames[-1].get_height() * frame_scale,
            ))
        
    def is_hide(self):
        return self.hide
    
    def restart(self):
        self.hide = False
        self.counter = 0
    
    def draw_default_frame(self):
        self.scr.blit(self.animation_frames[0], self.position)
    
    def draw(self):
        
        time_difference = time.time() - self.millis
        
        if time_difference>(1/self.fps):
            self.counter += 1
            if self.counter>=self.frames_number:
                if self.looped:
                    self.counter=0
                else:
                    self.hide = True
            
            self.millis = time.time()
        
        if not self.hide: self.scr.blit(self.animation_frames[self.counter], self.position)