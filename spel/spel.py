import pygame
import time
import random

pygame.init()


width = 800
height = 600
spelruta = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hungriga Katter')

klocka = pygame.time.Clock()

mus_width = 100

kattBild = pygame.transform.scale(pygame.image.load("cat.png"), (100,100))
musBild = pygame.transform.scale(pygame.image.load("mouse.png"), (mus_width,100))


def mus(x, y):
    spelruta.blit(musBild, (x, y))

def katt(x, y):
    spelruta.blit(kattBild, (x, y))

def points(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Poäng: " + str(count), True, (0,0,0))
    spelruta.blit(text, (10, 10))

def text_objects(text, font):
    text_yta = font.render(text, True, (0,0,0))
    return text_yta, text_yta.get_rect()

def display_message(text):
    stor_text = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, stor_text)
    TextRect.center = ((width/2), (height/2))
    spelruta.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    spela()

def sluta_spela():
    display_message('Du förlorade!')

def spela():
    x = 400
    y = 500
    x_change = 0
    spelet_slut = False

    katt_start_x = random.randint(0, width - 100)
    katt_start_y = -500
    katt_speed = 4

    kommit_undan = 0

    while not spelet_slut:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        spelruta.fill((255, 255, 255))
        katt(katt_start_x, katt_start_y)
        katt_start_y += katt_speed

        mus(x, y)
        points(kommit_undan)

        if x > width - mus_width or x < 0:
            sluta_spela()

        if katt_start_y > height:
            katt_start_y = -500
            katt_start_x = random.randint(0, width - 100)
            kommit_undan += 1
            katt_speed += 1

        if y < katt_start_y + 100:
            if x > katt_start_x and x < katt_start_x + 100 or x + mus_width > katt_start_x and x + mus_width < katt_start_x + 100:
                sluta_spela()

        pygame.display.update()
        klocka.tick(60)

spela()
pygame.quit()
quit()