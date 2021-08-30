import random
import time
from pygame import *
lost = 0

E = time.Clock()
global start_time
start_time = 0
global Magazin
Magazin = 10
global PiyPiy
PiyPiy = True


class GameSprite1(sprite.Sprite):
    def __init__(self, player_image, player_x1, player_y1, player_speed1,x,y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x,y))
        self.speed1 = player_speed1
        self.rect = self.image.get_rect()
        self.rect.x = player_x1
        self.rect.y = player_y1
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player_1(GameSprite1):
    def move_sprite1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_d] and self.rect.x < 1350:
            self.rect.x += self.speed1
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed1
    def FIRE(self):
        if y == 0:
            bullets.add(Bullet_1('bullet.png', self.rect.centerx-20/2,self.rect.top,2,20,35))
        if y == 1:
            bullets.add(Bullet_1('bullet.png', self.rect.x,self.rect.top,2,20,35))
            bullets.add(Bullet_1('bullet.png', self.rect.right-20,self.rect.top,2,20,35))
        if y == 2:
            bullets.add(Bullet_1('bullet.png', self.rect.centerx-20/2,self.rect.top,2,20,35))
            bullets.add(Bullet_1('bullet.png', self.rect.x,self.rect.top+20,2,20,35))
            bullets.add(Bullet_1('bullet.png', self.rect.right-20,self.rect.top+20,2,20,35))
        Piy.play()



class UFO_1(GameSprite1):
    def update(self):
        self.rect.y += self.speed1
        #global deth_pos
        global lost
        if self.rect.y >= 1000: #or sprite.collide_rect(Player_sprite)
            self.rect.y = -100#
            self.rect.x = random.randint(0,1300)#if sprite.collide_rect(Player_sprite):
            self.speed1 += 0.005
            lost += 1
        #deth_pos = [self.rect.x,self.rect.y]


class Bullet_1(GameSprite1):
    def update(self):
        self.rect.y -= 3
        if self.rect.y <=-35:
            self.kill()

class Level_UP_1(GameSprite1):
    def update(self):
        self.rect.y += self.speed1
        if self.rect.y >=1000:
            self.kill()





Barrier_lost = 100
window = display.set_mode((1400,1000))
display.set_caption("Шутер")
background = transform.scale(image.load("background.jpg"), (1400,1000))
life = 3
finish = False
game = True
Player_sprite = Player_1('pngwing.com.png',0,890,3,100,100)
monsters = sprite.Group()
font.init()
font1 = font.Font(None,36)
font2 = font.Font(None,100)
bullets = sprite.Group()
for i in range(5):
    monsters.add(UFO_1('UFO.png',random.randint(0,1300),random.randint(-100,200),1,100,100))
score = 0
Bonus = sprite.Group()
mixer.init()
mixer.music.load('Ultramariny_-_Gimn_Ultramarinov_66625730.ogg')
#mixer.music.play()
Bambambam = mixer.Sound('vyigruzili-nenujnyiy-metall.ogg')
Piy = mixer.Sound('vyistrel-iz-avtomata-ocheredyu.ogg')
y = 0
while game:
    if finish != True:
        window.blit(background, (0, 0))
        Player_sprite.move_sprite1()
        Player_sprite.reset()
        bullets.update()
        monsters.update()
        bullets.draw(window)
        monsters.draw(window)
        Bonus.update()
        Bonus.draw(window)
        My_time = time.get_ticks()
        sprite_list = sprite.groupcollide(bullets,monsters,True,True)
        sprite_list1 = sprite.spritecollide(Player_sprite,monsters,True)
        sprite_list2 = sprite.spritecollide(Player_sprite,Bonus,True)
        for i in sprite_list:
            #Bonus.add(Level_UP_1('lvl up.png',deth_pos[0],deth_pos[1],1,30,30))
            score += 1
            monsters.add(UFO_1('UFO.png', random.randint(0, 1300), -100, 1, 100, 100))
        for i in sprite_list1:
            if life > 0:
                life -= 1
                monsters.add(UFO_1('UFO.png', random.randint(0, 1300), -100, 1, 100, 100))
                Bambambam.play()
        for i in sprite_list2:
            y = 1
        text_lost = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
        text_score = font1.render('Счёт: ' + str(score), 1, (255,255,255))
        text_life = font1.render('Жизни: ' + str(life), 1, (255, 255, 255))
        window.blit(text_score,(5,30))
        window.blit(text_lost,(5,5))
        window.blit(text_life, (5, 55))
        if life == 0:
            finish = True
        if lost == Barrier_lost:
            finish = True
    elif life==0:
        text_FAIL = font2.render("Вы погибли!", 100, (255,255,255))
        window.blit(text_FAIL,(300,450))
    elif lost == Barrier_lost:
        text_FAIL = font2.render("Вы провалили миссию!", 100, (255, 255, 255))
        window.blit(text_FAIL, (300, 450))
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_e:
                if y < 2:
                    y += 1
                else:
                    y = 0
            if e.key == K_SPACE:
                if PiyPiy == True:
                    Magazin -= 1
                    Player_sprite.FIRE()
                    if Magazin == 0:
                        PiyPiy = False
                        Magazin = 10
                        start_time = time.get_ticks() // 1000
                else:
                    if start_time + 1 <= time.get_ticks() // 1000:
                        PiyPiy = True

    print(E.get_time())

    display.update()


