import pygame

class Gun():

    def __init__(self, screen):
        self.screen=screen
        self.image=pygame.image.load('image/gun')
        self.rect=self.image.get_rect()
        self.screen_rect=self.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.buttom=self.screen_rect.buttom


    def output(self):
        pass
