import pygame, sys
from bullet import Bullet
from ino import Ino
import time

logVisible = False  # видимость лога


def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False
    # дальшще - логирование в консоль
    if logVisible:
        print(len(bullets))


def update(bg_color, screen, gun, inos, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, inos, bullets):
    """обвновляем позиции пуль и если они вышли за жэкран - удаляем их"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos,True, True) #Эти труе говорят что нужно из исходных словарей удалять и пули и пришельцев. Нужно будет поэксперементировать!
    if len(inos)==0:
        bullets.empty
        create_army(screen, inos)

def gun_kiil(stats, screen, gun, inos, bullets):
    """столкновение пушки и армии"""
    stats.guns_left-=1
    inos.empty()
    bullets.empty()
    create_army(screen, inos)
    gun.create_gun()
    time.sleep(1)


def update_inos(stats, screen, gun, inos, bullets):
    """обновляет позицию инопланетян"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kiil(stats, screen, gun, inos, bullets)
    inos_chek(stats, screen, gun, inos, bullets)

def inos_chek(stats, screen, gun, inos, bullets):
    """дошли ли пришельцы до низа экрана?"""
    screen_rect=screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom>= screen_rect.bottom:
            gun_kiil(stats, screen, gun, inos, bullets)
            break




def create_army(screen, inos):
    """создание армии пришельцев"""
    ino = Ino(screen)
    ino_width=ino.rect.width
    ino_height=ino.rect.height
    #заменить 500 на ширину экрана и 650 на высоту!!!
    number_ino_x = int((500-2*ino_width)/ino_width)
    number_ino_y=int((650-100-2*ino_height)/ino_height)
    for row_number in range(number_ino_y-1):
        for ino_number in range(number_ino_x):
            ino=Ino(screen)
            ino.x=ino_width+ino_width*ino_number
            ino.y=ino_height+ino_height*row_number
            ino.rect.x=ino.x
            ino.rect.y=ino.rect.height+ino.rect.height*row_number
            inos.add(ino)


