from pygame import *


screen = display.set_mode((700, 500))
clock = time.Clock()
bg = transform.scale(image.load('background.jpg'), (700, 500))

class Creator(sprite.Sprite):
    def __init__(self, image_name, x, y, w, h, speed):
        self.image = transform.scale(image.load(image_name),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(Creator):
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < 300:
            self.rect.y += self.speed

    def move_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed


racket = Player('racket.png', 0, 0, 35, 200, 10)
racket2 = Player('racket.png', 665, 0, 35, 200, 10)
ball = Creator('tenis_ball.png', 350, 250, 100, 100, 10)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    screen.blit(bg, (0, 0))
    racket.update()
    racket2.update()
    racket.move_l()
    racket2.move_r()
    ball.update()


    display.update()
    clock.tick(40)