import pygame


def play(src, mode=-1):
    pygame.mixer_music.load(src)
    pygame.mixer_music.play(mode)


def stop(): pygame.mixer_music.stop()
