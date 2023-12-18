import pygame
import controls
from gun import Gun
from pygame.sprite import Group


game_name = "Космические защитники"

def run():
    """инициализация главного окна игры
    устанавливапем разрешение экрана, цвет фона, заголовок окна..."""
    pygame.init()
    #700*800
    screen = pygame.display.set_mode((500, 650))
    pygame.display.set_caption(game_name)
    bg_color=(0,0,0)
    gun = Gun(screen)
    bullets=Group()
    inos=Group()
    controls.create_army(screen, inos)

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(bullets)
        controls.update_inos(inos)

run()
