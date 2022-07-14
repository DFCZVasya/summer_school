from math import fabs
import pygame
from button import Button
animCount = 0
isJump = False
isRight = False
isLeft = False
width = 500
height = 500 
x = 100
y = 100
dy = 2
dx = 2
screen = pygame.display.set_mode([width,height])
bg = pygame.image.load("img/pygame_bg.jpg")

player_stand = pygame.image.load("img/pygame_idle.png")

player_right = [pygame.image.load("img/pygame_right_1.png"), pygame.image.load("img/pygame_right_2.png"),
pygame.image.load("img/pygame_right_3.png"),pygame.image.load("img/pygame_right_4.png"),
pygame.image.load("img/pygame_right_5.png"),pygame.image.load("img/pygame_right_6.png")]

player_left = [pygame.image.load("img/pygame_left_1.png"), pygame.image.load("img/pygame_left_2.png"),
pygame.image.load("img/pygame_left_3.png"),pygame.image.load("img/pygame_left_4.png"),
pygame.image.load("img/pygame_left_5.png"),pygame.image.load("img/pygame_left_6.png")]

def test():
    print("button pressed")

jumpCount = 10

def drawWindow():
    global isLeft, isRight, animCount
    screen.blit(bg,(0,0))
    #b = Button(screen, 100,100, 200, 200, pygame.font.SysFont('Arial', 40))
    if isRight:
        screen.blit(player_right[animCount//6],(x,y))
    elif isLeft:
        screen.blit(player_left[animCount//6],(x,y))
    else:
        screen.blit(player_stand,(x,y))
    #b.process()
    pygame.display.update()



def main():
    global x,y,dx,dy, isRight, isLeft, animCount, isJump, jumpCount
    pygame.init()
    
    running = True
    while running:
        animCount += 1
        if animCount > 30:
            animCount = 0
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT] and x > 0:
            x -= dx
            isLeft = True
        else:
            isLeft = False
        if keys[pygame.K_RIGHT] and x < 440:
            x += dx
            isRight = True
        else:
            isRight = False
        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
            if keys[pygame.K_UP] and y > 0:
                y -= dy
            if keys[pygame.K_DOWN] and y < 429:
                y += dy
        else:
            if jumpCount > 0:
                y -= (jumpCount**2)/2
            else:
                y += (jumpCount**2)/2
            jumpCount -= 1
            if jumpCount == -11:
                isJump = False
                jumpCount = 10
        drawWindow() 
        
    pygame.quit()

if __name__ == "__main__":
    main()