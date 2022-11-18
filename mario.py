import pygame
import random
pygame.init()

screen_height = 600
screen_width = 800
blue = (135, 206, 235)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
fps = 10
velocity = 30
clock = pygame.time.Clock()

gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("NARUTOOO")

bgimg = pygame.image.load("ground.jpg")
bgimg = pygame.transform.scale(
    bgimg, (screen_width, screen_height * 0.25)).convert_alpha()

bgimg2 = pygame.image.load("ground.jpg")
bgimg2 = pygame.transform.scale(
    bgimg2, (screen_width * 1.02, screen_height * 0.25)).convert_alpha()

building1 = pygame.image.load("building.png")
building2 = pygame.image.load("building.png")

naruto = pygame.image.load("naruto.png")
naruto2 = pygame.image.load("naruto2.png")

naruto_1_loaded = True

cloud = pygame.image.load("cloud.png")
cloud2 = pygame.image.load("cloud2.png")
cactus = pygame.image.load("cactus.png")


kishame = pygame.image.load("kishame.png")
tobi = pygame.image.load("tobi.png")
itachi = pygame.image.load("itachi.png")
pain = pygame.image.load("pain.png")
orochimaru = pygame.image.load("orochimaru.png")
konan = pygame.image.load("konan.png")
kakuzu = pygame.image.load("kakuzu.png")
sasuke = pygame.image.load("sasuke.png")
hidan = pygame.image.load("hidan.png")
sasori = pygame.image.load("sasori.png")
deidara = pygame.image.load("deidara.png")


exitgame = False
cloud1X = 0
cloud2X = 600

bgimgX = 0
bgimg2X = -800

building1x = 0
building2x = -800

game_over = False

tile1x = 0
tile1y = 300

tile2x = 400
tile2y = 200


cactus1x = 100
cactus1y = 360

kishame1x = 0
kishame1y = 330

itachi1x = 0
itachi1y = 330

jump = False

naruto_jump_pos = 350
naruto_fall_pos = 250

time_const = 0
time_const2 = 0

enemy_to_blit = kishame

while not exitgame:
    gamewindow.fill(blue)

    if(bgimgX > 790):
        bgimgX = -790
    else:
        bgimgX += 10

    if(bgimg2X > 790):
        bgimg2X = -790
    else:
        bgimg2X += 10

    gamewindow.blit(bgimg, (bgimgX, 450))
    gamewindow.blit(bgimg2, (bgimg2X, 450))

    if(cloud1X > 800):
        cloud1X = -400
    else:
        cloud1X += 10

    if(cloud2X > 800):
        cloud2X = -400
    else:
        cloud2X += 10
    gamewindow.blit(cloud, (cloud1X, 30))
    gamewindow.blit(cloud2, (cloud2X, 200))

    if(building1x > 790):
        building1x = -790
    else:
        building1x += 10

    if(building2x > 790):
        building2x = -790
    else:
        building2x += 10

    gamewindow.blit(building1, (building1x, 68))
    gamewindow.blit(building2, (building2x, 68))

    if(not jump):
        if(abs(550 - kishame1x) < 50 and abs(350 - kishame1y) < 50):
            exitgame = True
    else:
        if(abs(550 - kishame1x) < 50 and naruto_jump_pos > 250):
            exitgame = True

    # if(not jump):
        # if(abs(550 - cactus1x) < 40 and abs(350 - cactus1y) < 40):
            #exitgame = True
    # else:
        # if(abs(550 - cactus1x) < 40 and naruto_jump_pos > 250):
           # exitgame = True

    if(not jump):
        if(naruto_1_loaded):
            gamewindow.blit(naruto2, (550, 350))
            naruto_1_loaded = False
        else:
            gamewindow.blit(naruto, (550, 350))
            naruto_1_loaded = True
    else:
        if(naruto_jump_pos > 250):
            time_const += 1
            distance = 0.5*-10*(time_const ** 2)
            naruto_jump_pos += distance
            gamewindow.blit(naruto2, (550, naruto_jump_pos))
        elif(time_const < 15):
            time_const += 1
            gamewindow.blit(naruto2, (550, 250))
        elif(naruto_fall_pos < 350):
            time_const2 += 1
            distance = 0.5*3*(time_const2 ** 2)
            naruto_fall_pos += distance
            gamewindow.blit(naruto2, (550, naruto_fall_pos))
        elif(naruto_fall_pos > 350):
            naruto_jump_pos = 350
            naruto_fall_pos = 250
            time_const = 0
            time_const2 = 0
            jump = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True
        if event.type == pygame.KEYDOWN:
            jump = True

    if(cactus1x > 800):
        cactus1x = -400
        cactus1x = random.choice([-400, -600, -750, -950, -1000])
    else:
        cactus1x += 10

    if(kishame1x > 800):
        kishame1x = -400
        kishame1x = random.choice([-400, -500, -450, -550, -600])
        enemy_to_blit = random.choice(
            [kishame, itachi, tobi, deidara, sasuke, sasori, hidan, kakuzu, orochimaru, pain, konan])
    else:
        kishame1x += 10

    gamewindow.blit(cactus, (cactus1x, cactus1y))
    gamewindow.blit(enemy_to_blit, (kishame1x, kishame1y))

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
