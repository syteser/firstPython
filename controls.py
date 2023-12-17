import pygame, sys

def events(gun):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                gun.mright=True
            if event.key==pygame.K_LEFT:
                gun.mleft=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                gun.mright=False
            if event.key == pygame.K_LEFT:
                gun.mleft = False
