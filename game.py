import pygame

import bullet
import controls

from gun import Gun
from pygame.sprite import Group

game_name = "Космические защитники"

def run():
    """инициализация главного окна игры
    устанавливапем разрешение экрана, цвет фона, заголовок окна..."""
    pygame.init()
    screen = pygame.display.set_mode((500, 650))
    pygame.display.set_caption(game_name)
    bg_color=(0,0,0)
    gun = Gun(screen)
    bullets=Group()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, bullets)
        controls.update_bullets(bullets)

run()
