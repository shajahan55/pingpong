# ping pong - developed by Shajahan Iqbal

import pygame
import random

pygame.init()


# character configuration using classes

class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 100
        self.colour = (255, 255, 255)
        self.velocity = 1
        self.isturn = True

    def create(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width + 2, self.height + 2)
        pygame.draw.rect(window, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, width=2)

    def move(self, up, down):  # movement function

        keys = pygame.key.get_pressed()

        if keys[up] and self.y >= 0:
            self.y -= self.velocity
        elif self.y < 0:
            self.y = 0

        if keys[down] and self.y <= 500 - self.height:
            self.y += self.velocity

        elif self.y > 500:
            self.y = 500


class Ball():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 7
        self.colour = (255, 255, 255)
        self.direction = 1
        self.velocity_x = 3/4
        self.velocity_y = 1

    def move(self):  # movement mechanism/ ball redraw
        if self.hitbox[1] + self.hitbox[3] >= 500 or self.hitbox[1] <= 0:
            self.direction = self.direction * -1

        if self.hitbox[0] + self.hitbox[2] == player2.hitbox[0] and self.hitbox[1] + self.hitbox[3] > player2.hitbox[
            1] and self.hitbox[1] < player2.hitbox[1] + player2.hitbox[3]:
            self.velocity_x = self.velocity_x * -1

        if self.hitbox[0] == player1.hitbox[0] + player1.hitbox[2] and self.hitbox[1] + self.hitbox[3] > player1.hitbox[
            1] and self.hitbox[1] < player1.hitbox[1] + player1.hitbox[3]:
            self.velocity_x = self.velocity_x * -1

        if self.x == 520:
            global score_player1
            score_player1 += 1



            self.x = 250
            self.y = 250

        if self.x == -20:
            global score_player2
            score_player2 += 1



            self.x = 250
            self.y = 250

        self.x += self.velocity_x
        self.y += self.velocity_y * self.direction

    def draw(self):
        self.hitbox = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, width=2)
        pygame.draw.circle(window, self.colour, (self.x, self.y), self.radius)


# sound and music
pygame.mixer.init()
music = pygame.mixer.music.load('D:\pong game\music.mp3')
pygame.mixer.music.play(-1)
winsound = pygame.mixer.Sound('D:\pong game\win.wav')

# characters

player1 = Player(20, 200)
player2 = Player(480, 200)
ball = Ball(250, 250)

# screen initialization + score system
comic_sans = pygame.font.SysFont('comicsans', 45, True)
comic_sans1 = pygame.font.SysFont('comicsans', 90, True)
window = pygame.display.set_mode([500, 500])
score_player1 = 0
score_player2 = 0

# main loop

run = True

while run:
    global shoulddraw
    shoulddraw = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((0, 0, 0))

    if score_player1 == 10:
        shoulddraw = False
        window.blit(player2_win, (10, 100))
        window.blit(thankyou, (50, 400))
        pygame.mixer.music.stop()
        winsound.play()





    elif score_player2 == 10:
        shoulddraw = False
        window.blit(player1_win, (10, 100))
        window.blit(thankyou, (10, 400))
        pygame.mixer.music.stop()
        winsound.play()

    player1_win = comic_sans1.render('Player1 WINS!!', True, (255, 255, 0))
    player2_win = comic_sans1.render('Player2 WINS!!', True, (255, 255, 0))
    thankyou = comic_sans1.render('Thank You', True, (255,255,0))
    score1 = comic_sans.render(str(score_player2), True, (255, 255, 0))
    score2 = comic_sans.render(str(score_player1), True, (255, 255, 0))
    window.blit(score1, (280, 20))
    window.blit(score2, (220, 20))
    player1.create()
    player2.create()
    ball.draw()
    if shoulddraw == True:
        ball.move()
    player1.move(pygame.K_w, pygame.K_s)
    player2.move(pygame.K_UP, pygame.K_DOWN)

    pygame.display.update()

pygame.quit()
