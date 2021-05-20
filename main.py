import pygame
import random

pygame.init()
pygame.mixer.init() 
win = pygame.display.set_mode((600, 720))
pygame.display.set_caption("Welcome to the club!")
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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(self.image, (50,38))
        transColor = self.image.get_at((0, 0))
        self.image.set_colorkey(transColor) 
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(W)
        self.rect.bottom = random.randrange(H)
        self.speedx = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

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

in_game = True

while in_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()   

hits = pygame.sprite.spritecollide(player, tubes, True)
if hits:
    in_game = False
    player.zero

pygame.draw.line(win, color, start_pos = (x0, y0), end_pos = (x1, y1), width = 1)

pygame.draw.rect(win, color, (top, left, width, height), width = 1)

pygame.draw.circle(win, color, center = (x0, y0), radius = radius, width = 1)

all_sprites.update()

screen.fill(BLACK)

all_sprites.draw(screen)
pygame.display.flip()

pygame.quit()