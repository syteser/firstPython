import pygame, controls
from gun import Gun

game_name = "Космические защитники"

def run():
    """инициализация главного окна игры
    устанавливапем разрешение экрана, цвет фона, заголовок окна..."""
    pygame.init()
    screen = pygame.display.set_mode((500, 650))
    pygame.display.set_caption(game_name)
    bg_color=(0,0,0)
    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()

run()
