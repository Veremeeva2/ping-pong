from pygame import *
window = display.set_mode((600, 500))

class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
     def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Hero(GameSprite):
     def update_r(self):
          keys_pressed = key.get_pressed()        
          if keys_pressed[K_UP] and self.rect.y > 5:
               self.rect.y -=self.speed
          if keys_pressed[K_DOWN] and self.rect.y < 500 - 80:
               self.rect.y += self.speed
     def update_l(self):
          keys_pressed = key.get_pressed()
          if keys_pressed[K_w] and self.rect.y > 5:
               self.rect.y -= self.speed
          if keys_pressed[K_s] and self.rect.y < 500 - 80:
               self.rect.y += self.speed

back = (200, 255, 255)
window.fill(back)

game =True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Hero('raket.png', 30, 200,  50, 150,4)
racket2 = Hero('raket.png', 520, 200, 50, 150, 4)
ball = GameSprite('ma.png', 200, 200, 50, 50, 4)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
     for e in event.get():
          if e.type == QUIT:
               game = False
     if finish != True:
          window.fill(back)
          racket1.update_l()
          racket2.update_r()
          ball.rect.x += speed_x
          ball.rect.y += speed_y

          if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
               speed_x *= -1
               speed_y *= 1
          
          if ball.rect.y > 500 - 50 or ball.rect.y < 0:
               speed_y *= -1
          if ball.rect.x < 0:
               finish = True
               window.blit(lose1, (200, 200))
               game_over = True
          if ball.rect.x > 700:
               finish = True
               window.blit(lose2, (200, 200))
          racket1.reset()
          racket2.reset()
          ball.reset()
     display.update()
     clock.tick(60)

    

