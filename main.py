from pygame import *


font.init()
screen = display.set_mode((700, 500))
clock = time.Clock()
bg = transform.scale(image.load('background.jpg'), (700, 500))

class Creator(sprite.Sprite):
    def __init__(self, image_name, x, y, w, h, speed):
        self.image = transform.scale(image.load(image_name),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed
        self.speed_y = speed

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    

class Player(Creator):
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        elif keys[K_s] and self.rect.y < 300:
            self.rect.y += self.speed_y

    def move_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        elif keys[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed_y


racket = Player('racket.png', 0, 0, 20, 150, 10)
racket2 = Player('racket.png', 680, 0, 20, 150, 10)
ball = Creator('tenis_ball.png', 350, 250, 50, 50, 3)
font1 = font.Font(None, 60)
text_win1 = font1.render('Player 1 lose', 1, (255, 0, 0))
text_win2 = font1.render('Player 2 lose', 1, (255, 0, 0))
move_right = False
move_left = True
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

    if move_right:
        ball.rect.x += ball.speed_x
    elif move_left:
        ball.rect.x -= ball.speed_x


    ball.rect.y += ball.speed_y
    if ball.rect.y > 0 or ball.rect.y < 450:
        ball.rect.y += ball.speed_y



    if ball.rect.y <= 0 or ball.rect.y >= 450:
        ball.speed_y *= -1
    elif sprite.collide_rect(ball, racket) or sprite.collide_rect(ball, racket2):
        if move_left:
            move_right = True
            move_left = False
        elif move_right:
            move_right = False
            move_left = True

    if ball.rect.x < 0:
        screen.blit(text_win1, (0, 0))
    elif  ball.rect.x > 700:
        screen.blit(text_win2, (0, 0))
        



    display.update()
    clock.tick(40)