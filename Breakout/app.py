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

clock = pygame.time.Clock()

make_jump = False
pause = False
jump_counter = 30


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
    global make_jump, pause

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        make_jump = True

    if keys[pygame.K_LEFT]:
        moove(-20)

    if keys[pygame.K_RIGHT]:
        moove(20)

    if keys[pygame.K_UP]:
        make_jump = True




    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

def run_game():
    global usr_x
    i = 1

    color_1 = 1
    color_2 = 88
    color_3 = 40

    while 1:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()

        if usr_x <= 0 + usr_w:
            usr_x += 5
        elif usr_x >= width - usr_w:
            print("In elif!")
            usr_x -= 5

        check_event()

        if make_jump:
            jump()
        if color_1 >= 200:
            i *= -1
        elif color_1 <= 0:
            i *= -1
        display.fill((color_1, color_2, color_3))

        pygame.draw.rect(display, (247, 240, 22), (usr_x, usr_y, usr_w, usr_h))

        pygame.display.update()
        clock.tick(60)
        color_1+=i




run_game()