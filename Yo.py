import pygame
from pygame.constants import K_x

player_img = pygame.image.load("player.png")

class Player(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        #1 - Вызов конструктора род-го класса
        pygame.sprite.Sprite.__init__(self)
        #2 - картинка
        self.image = img
        img = pygame.transform.scale(img, (100,100))
        #Замена цвета
        color = self.image.get_at((0, 0))
        self.image.det_colorkey(color)
        #3 - Прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
        self.speedx = 1
        self.speedy = 1

    # Написать как ходить
    def Update(self):
        pass


player = Player(player_img, 350, 350)
group = pegame.sprite.Group()
group.add(player)



hits = pygame.sprite.spritecollide(player, tubes, True)
if hits:
    in_game = False