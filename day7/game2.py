import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("New Game!")

x = 220
y = 420
width = 40
height = 60
speed = 10

isJump = False
JumpCount = 10

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
    if not isJump:
        if keys[pygame.K_UP] and y > 5:
            isJump = True
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2    
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10    
    #if keys[pygame.K_DOWN] and y < 500 - height - 5 - 20:
    #    y += speed

    win.fill((0,0,0))
    pygame.draw.rect(win, (0,255,0), (x, y, width, height))
    pygame.draw.rect(win, (150,75,0), (0, 480, 500, 20))
    pygame.display.update()


pygame.quit()