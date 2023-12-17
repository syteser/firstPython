import pygame
import sys

game_name = "Название игры"

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption(game_name)
    bg_color=(0,0,0)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()

run()
