from random import Random

import pygame

pygame.init()
width = 800
height = 600

pygame.display.set_caption("LoooLLL")
display = pygame.display.set_mode((width, height))
usr_w = 60
usr_h = 10
usr_x = width // 3
usr_y = height - 100 - usr_h
yy = 10


bloch_with = 60
bloch_hight = 10

clock = pygame.time.Clock()

make_jump = False
pause = False
jump_counter = 30

bg_image = pygame.image.load(r'source\image\bg_image.png')



class Rectangle:
    width = 60
    hight = 15
    pos_x = 0
    pos_y = 0

    def __init__(self, x, y, color_r, color_g, color_b):
        self.pos_x = x
        self.pos_y = y
        self.color_r = color_r
        self.color_g = color_g
        self.color_b = color_b

def jump():
    global usr_y, make_jump, jump_counter
    if jump_counter >= -30:
        usr_y -= jump_counter / 2
        jump_counter -= 1

    else:
        jump_counter = 30
        make_jump = False


def moove(arg):
    global usr_x

    usr_x += arg

def check_event():
    global make_jump, pause, usr_x

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        make_jump = True

    if keys[pygame.K_LEFT]:
        if (usr_x >= 3):
            print('usr_x = {}'.format(usr_x))
            moove(-20)
        else:
            print('in else left')
            usr_x = 795

    if keys[pygame.K_RIGHT]:
        if (usr_x <= 795):
            print('usr_x = {}'.format(usr_x))
            moove(20)
        else:
            print('in else right')
            usr_x = 3

    if keys[pygame.K_UP]:
        make_jump = True




    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

def run_game():
    global usr_x
    const_x = 800
    const_y = 400
    coord_xx = 13
    list_rect = []
    coord_yy = 10
    random = Random()
    while ((coord_yy + 50) <= const_y):
        while ((coord_xx + 60) <= const_x):
            list_rect.append(
                Rectangle(coord_xx,
                          coord_yy,
                          random.randint(0,255),
                          random.randint(0,255),
                          random.randint(0,255)
                          )
            )
            coord_xx += 65
        coord_xx = 13
        coord_yy += 25

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()

        check_event()

        display.blit(bg_image, (0,0))
        pygame.draw.rect(display, (247, 240, 22), (usr_x, usr_y, usr_w, usr_h))
        for rect in list_rect:
            # print('x = {0}, y = {1}'.format(rect.pos_x, rect.pos_y))
            pygame.draw.rect(display, (rect.color_r, rect.color_g, rect.color_b), (rect.pos_x, rect.pos_y, rect.width, rect.hight))

        pygame.display.update()
        clock.tick(60)



run_game()