import pygame

#класс пули

bullet_speed=15 #скорость пули
class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """создаем пули по текущей позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = (139, 195, 74)
        self.speed = bullet_speed
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх"""
        self.y -=self.speed
        self.rect.y=self.y

    def draw_bullet(self):
        """рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)

