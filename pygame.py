#.........
import pygame ,random,sys,os,time
from pygame.locals import*

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR =(255,255,255)
BACKGROUNDCOLOR = (45,0,0)
FPS = 40
BADDIEMINSIZE =10
BADDIEMAXSIZE =40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE= 6
PLAYERMOVERATE= 5
COUNT=3


def terminate():
    pygame.quit()
    sys.exit()
    def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                terminate()
              if event.key == KEYDOWN:
                  if event.key == k_ESCAPE:
                      terminate()
                    return

def playerHashitbaddie(playerrect,beddies):
     for b in baddies:
         if playerrect.colliderect(b['rect']):
             return True
         return False

def drawText(text,font,surface,x,y):
    textobj = font.render(text,1,TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)

#set up pygame,the window




#to make input in center x axis yaxis
#def geting():
# conn.execute("INSERT INTO score(SRNO,SCORE) VALUES(count.get())")



def car(x,y):
    gameDisplay.blit(carImg, (x,y))

#caImg= pygame.image.load('lamb.jpg')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('CAR RACING')
clock = pygame.time.Clock()

carImg = pygame.image.load('car1.png')
#gameDisplay.blit(carImg.(250,380))

pause = False
def things_dodged(count):
    font=pygame.font.SysFont('italic', 25)
    text = font.render("score:" + str(count),True,red)
    gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh):
    carImg = pygame.image.load('racecar.png')

gameDisplay.blit(carImg, (thingx, thingy ,thingw ,thingh))







def car(x,y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()


def display_msg(text):
    largeText = pygame.font.Font("freesansbold.ttf",40)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash():
    display_msg("bomm!! U CRASHED")

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    Exit = False

    while not Exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(red)
        car(x, y)

        if x > display_width - car_width or x < 0:
            crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.q
import time
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 70

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('CAR RACING')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')


def car(x,y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()


def display_msg(text):
    largeText = pygame.font.Font("freesansbold.ttf",40)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash():
    display_msg("bomm!! U CRASHED")

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    Exit = False

    while not Exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(red)
        car(x, y)

        if x > display_width - car_width or x < 0:
            crash()

        pygame.display.update()
        clock.tick(60)

#game_details()
game_intro()
game_loop()
pygame.quit
quit()