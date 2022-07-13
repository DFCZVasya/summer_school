import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode([500,500])
    running = True
    x = 100
    y = 100
    dy = 5
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,100,100))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y += dy
                    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,100,100))
                    pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()