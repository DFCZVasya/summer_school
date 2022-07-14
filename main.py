import pygame

width = 500
height = 500 

bg = pygame.image.load("img/pygame_bg.jpg")

player_stand = pygame.image.load("img/pygame_idle.png")

def main():
    pygame.init()
    screen = pygame.display.set_mode([width,height])
    running = True
    x = 100
    y = 100
    dy = 2
    dx = 2

    pygame.display.update()
    while running:
        screen.blit(bg,(0,0))
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

        screen.blit(player_stand,(x,y))
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()