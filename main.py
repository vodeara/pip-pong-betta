from pygame import *

FPS = 60
FON = (255, 255, 255)
clock = time.Clock()
window = display.set_mode((700,600))
window.fill(FON)
game_over = False






class GameSprite(sprite.Sprite):
    def init (self, player_img, player_x, player_y,width, height, player_speed):
        super().init()
        self.image = transform.scale(image.load(player_img),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Hero(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 600 - 80:
            self.rect.x += self.speed
    

player1 = Hero('ff.jpg',600,350,10,)
player2 = Hero('kartoska.webp',600,300,10)


while not game_over:
    for e in event.get():
        if e.type == QUIT:
            game_over = True
    player1.update()
    player2.update()
    





display.update()
clock.tick(FPS)







