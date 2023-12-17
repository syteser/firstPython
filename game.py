import pygame
import sys
from gun import Gun

game_name = "Космические защитники"

def run():
    """инициализация главного окна игры
    устанавливапем разрешение экрана, цвет фона, заголовок окна..."""
    pygame.init()
    screen = pygame.display.set_mode((1200, 650))
    pygame.display.set_caption(game_name)
    bg_color=(0,0,0)
    gun = Gun(screen)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()

run()
