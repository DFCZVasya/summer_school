import pygame

width = 500
height = 500 
x = 100
y = 100
dy = 2
dx = 2
screen = pygame.display.set_mode([width,height])
bg = pygame.image.load("img/pygame_bg.jpg")

player_stand = pygame.image.load("img/pygame_idle.png")

def drawWindow():
    screen.blit(bg,(0,0))
    screen.blit(player_stand,(x,y))
    pygame.display.update()

def main():
    global x,y,dx,dy
    pygame.init()
    running = True
    while running:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= dx
        if keys[pygame.K_RIGHT] and x < 440:
            x += dx
        if keys[pygame.K_UP] and y > 0:
            y -= dy
        if keys[pygame.K_DOWN] and y < 429:
            y += dy
        drawWindow() 
    pygame.quit()

if __name__ == "__main__":
    main()