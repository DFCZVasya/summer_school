import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode([500,500])
    running = True
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(100,100,100,100))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()