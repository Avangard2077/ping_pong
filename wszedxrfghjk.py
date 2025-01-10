from pygame import *
from random import randint
font.init()

w = display.set_mode((900, 550))
w.fill((102, 153, 255))
fon = transform.scale(image.load('8c501ccde62b374f36d9d33deff5c9d8.jpg'), (900, 550))
clock = time.Clock()
p = True


class Game(sprite.Sprite):
    def __init__(self, mage, speed, x, y, w, h):
        super().__init__()
        self.speed = speed
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(mage), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        w.blit(self.image, (self.rect.x, self.rect.y))


class Play1(Game):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]:
            self.rect.y += self.speed
        if self.rect.y > 440:
            self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.y += self.speed
        self.reset()

class Play2(Game):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= self.speed
        if keys_pressed[K_s]:
            self.rect.y += self.speed
        if self.rect.y > 440:
            self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.y += self.speed
        self.reset()

class FliMonster(Game):
    def __init__(self, mage, speed, x, y, w, h):
        super().__init__(mage, speed, x, y, w, h)
        self.speedx = 3
        self.speedy = -1

    def update(self):
        global o
        global g
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if GplayR.rect.colliderect(self.rect):
            self.speedx *= -1
            self.rect.x -= self.speed
        if GplayL.rect.colliderect(self.rect):
            self.speedx *= -1
            self.rect.x += self.speed
        if self.rect.y > 500:
            self.rect.y -= self.speed
            self.speedy *= -1
        if self.rect.y < 0:
            self.rect.y += self.speed
            self.speedy *= -1
        if self.rect.x > 800:
            self.rect.x = 425
            self.rect.y = 350
            self.speedx *= -1
            g += 1
            o = 50
        if self.rect.x < 0:
            self.rect.x = 425
            self.rect.y = 350
            self.speedx *= -1
            g += 1
            o = 50

class Sfer(Game):
    def __init__(self, mage, speed, x, y, w, h):
        super().__init__(mage, speed, x, y, w, h)
        self.f = 80
        self.l = 50

    def update(self):
        if self.f > 0:
            self.f -= 1
            self.rect.y -= self.speed
        if self.f == 0:
            Evill.reset()
        self.reset()

class Wall(sprite.Sprite):
    def __init__(self, x, y, color, w, h):
        self.color = color
        self.w = w
        self.h = h
        self.image = Surface((w, h))
        self.image.fill((self.color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drow(self):
        draw.rect(w, (1, 150, 128), self.rect)
        if GSfen.rect.colliderect(Evill.rect):
            self.rect.width -= 50
            Evill.rect.x = 425
            Evill.rect.y = 380
            Evill.speedx *= -1
            if Evill.speedy > 0:
                Evill.speedy *= -1
            if HP.rect.width == 300:
                Evill.speedx += 1
                if Evill.speedy > 0:
                    Evill.speedy += 1
                if Evill.speedy < 0:
                    Evill.speedy -= 1
            if HP.rect.width == 150:
                Evill.speedx += 1
                if Evill.speedy > 0:
                    Evill.speedy += 1
                if Evill.speedy < 0:
                    Evill.speedy -= 1

GplayR = Play1('Dgr.png', 7, 820, 300, 70, 120)
GplayL = Play2('Dgl.png', 7, 0, 135, 70, 120)
Evill = FliMonster('голуб.png', 6, 250, 380, 50, 50)
GSfen = Sfer('Doom.png', 2.5, 400, 600, 100, 100)
HP = Wall(220, 20, (245, 0, 20), 450, 20)
g = 0
o = 50
T = 9
l = 0
a = 450
f = 10
while p:
    y = randint(50, 400)
    w.blit(fon, (0, 0))
    clock.tick(90)
    for e in event.get():
        if e.type == QUIT:
            p = False
    HP.drow()
    point2 = font.SysFont('Arial', 30)
    win2 = point2.render(str(T), True, (0, 0, 0))
    w.blit(win2, (460, 12))
    point4 = font.SysFont('Arial', 30)
    win4 = point4.render('/', True, (0, 0, 0))
    w.blit(win4, (440, 12))
    if HP.rect.width == a - l:
        f -= 1
        l += 50
    point3 = font.SysFont('Arial', 30)
    win3 = point3.render(str(f), True, (0, 0, 0))
    w.blit(win3, (410, 12))
    if HP.rect.width > 0 and g != 3:
        GSfen.update()
        GplayR.update()
        GplayL.update()
        Evill.update()
    if HP.rect.width == 0:
        point = font.SysFont('Arial', 70)
        win = point.render("You Win", True, (255, 140, 0))
        w.blit(win, (310, 200))
    if g == 3:
        point1 = font.SysFont('Arial', 70)
        win1 = point1.render("You Lose", True, (255, 140, 0))
        w.blit(win1, (310, 200))
    display.update()
