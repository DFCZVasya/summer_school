import pygame

width = 500
height = 500 

def main():
    pygame.init()
    screen = pygame.display.set_mode([width,height])
    running = True
    x = 100
    y = 100
    dy = 2
    dx = 2
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,100,100))
    pygame.display.update()
    while running:
        screen.fill((0,0,0))
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= dx
        if keys[pygame.K_RIGHT] and x < 400:
            x += dx
        if keys[pygame.K_UP] and y > 0:
            y -= dy
        if keys[pygame.K_DOWN] and y < 400:
            y += dy

        pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,100,100))
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()