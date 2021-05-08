import pygame
import random

pygame.init()
pygame.mixer.init() 
win = pygame.display.set_mode((600, 720))
pygame.display.set_caption("Welcome to the club buddy!")
background_color = (0,) * 3

WIDTH = 600
HEIGHT = 720

WHITE = (255,) * 3
BLACK = (0,) *3
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

            
class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("ing.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)
        self.speedx = 0

def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

all_sprites.update()

screen.fill(BLACK)
all_sprites.draw(screen)
pygame.display.flip()

pygame.quit()