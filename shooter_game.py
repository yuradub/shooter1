#Створи власний Шутер!

from pygame import *
from random import *
from time import time as timer 
#імпортуємо функцію для засікання часу, 
# щоб інтерпретатор не шукав цю функцію в pygame модулі time, 
# даємо їй іншу назву самі

clock = time.Clock()
x1 = 5
y1 = 5
x2 = 100
y2 = 100
x3 = 200
y3 = 200
# нам потрібні такі картинки:
img_back = "galaxy.jpg"  # фон гри
img_hero = "rocket.png"  # герой
img_bullet = "bullet.png" # куля
img_enemy = "ufo.png"  # ворог
lost = 0 #skiped
score = 0 #killed enemy
goal = 10 #how much we need
max_lost = 10 #if we skip 3 items > lost
life = 3 
FPS = 60
win_height = 500
win_width = 700
window = display.set_mode((700, 500))
display.set_caption('Shooter')
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
window.blit(background,(0,0))
mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')
#fire_sound.play() 
font.init()
font1 = font.SysFont("Arial", 80)
win = font1.render("YOU WIN!", True, (255, 255, 255))
lose = font1.render("YOU LOSE!", True, (188, 0, 0))
telife = font1.render(str (life), True, (0, 255, 0))
font2 = font.SysFont("Arial", 36)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, waight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (waight, waight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.waight=waight
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, -15, 30)
        bullets.add(bullet)
class Enemy(GameSprite):
# pyx Bopora
    def update(self):
        self.rect.y += self. speed
        global lost
#3HMKaE, AKuO Aiñge no Kpao expaHa
        if self.rect.y > win_height:
            self.rect.x = randint (80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

monsters = sprite.Group()
asteroids = sprite.Group()
for i in range(1, 3):
    asteroid = Enemy ("asteroid.png", randint(80, win_width - 80), -40, randint(1,3), 65)
    asteroids.add (asteroid)

for i in range(1, 6):
    monster = Enemy ("ufo.png", randint(80, win_width - 80), -40, randint(1,3), 65)
    monsters.add (monster)
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
    
            

bullets = sprite.Group()



Ssprite = Player('rocket.png', 5, win_height - 80, 4, 65)
game = True
finish = False
rel_time = False  # прапор, що відповідає за перезаряджання
num_fire = 0  # змінна для підрахунку пострілів   

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        
        elif e.type == KEYDOWN:    
            if e.key == K_SPACE:
                #перевіряємо, скільки пострілів зроблено і чи не відбувається перезаряджання
                if num_fire < 5 and rel_time == False:
                    num_fire = num_fire + 1
                    #fire_sound.play()
                    Ssprite.fire()
                   
                if num_fire >= 5 and rel_time == False : #якщо гравець зробив 5 пострілів
                    last_time = timer() #засікаємо час, коли це сталося
                    rel_time = True #ставимо прапор перезарядки


    if finish != True:
        window.blit(background, (0,0))
        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        text_lose = font2.render("Paxунок: " + str(score), 1, (255, 255, 255))
        window.blit(text_lose, (10, 20))

        Ssprite.update()
        monsters.update()
        asteroids.update()
        Ssprite.reset()
        bullets.update()
        asteroids.draw(window)
        monsters.draw(window)
        bullets.draw(window)
        # перевірка зіткнення кулі та монстрів (і монстр, і куля при зіткненні зникають)
        # перевірка зіткнення кулі та монстрів (і монстр, і куля при зіткненні зникають)
        # створення нової пулі



# перевірка, чи пулі виходять за межі екрану
        for bullet in bullets:
            if bullet.rect.bottom < 0:
                bullets.remove(bullet) 

        # перезарядка
        if rel_time == True:
            now_time = timer() # зчитуємо час
         
            if now_time - last_time < 3: #поки не минуло 3 секунди виводимо інформацію про перезарядку
                reload = font2.render('Wait, reload...', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0     #обнулюємо лічильник куль
                rel_time = False #скидаємо прапор перезарядки

        # перевірка зіткнення кулі та монстрів (і монстр, і куля при зіткненні зникають)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            # цей цикл повториться стільки разів, скільки монстрів збито
            score = score + 1
            monster = Enemy ("ufo.png", randint(80, win_width - 80), -40, randint(1,3), 65)
            monsters.add(monster)


        
        # можливий програш: пропустили занадто багато або герой зіткнувся з ворогом
        #if sprite.spritecollide(Ssprite, monsters, False) or lost >= max_lost:
        #    finish = True# програли, ставимо тло і більше не керуємо спрайтами.
        #    window.blit(lose, (200, 200))

        if sprite.spritecollide(Ssprite, monsters, False) or  sprite.spritecollide(Ssprite, asteroids, False):
            sprite.spritecollide(Ssprite, monsters, True)
            sprite.spritecollide(Ssprite, asteroids, True)
            life = life - 1 
           
        # перевірка виграшу: скільки очок набрали?
        if life <= 0 or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
      
        telife = font1.render(str (life), 1, (0, 255, 0)) #кількість життів нашого ігрока
        window.blit(telife, (650, 10))

        display.update()
    clock.tick(FPS)