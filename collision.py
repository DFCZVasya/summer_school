import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screensize = (800, 600)
screen = pygame.display.set_mode(screensize)
colour = [(0, 0, 0), (255, 0, 0), (255, 255, 255), (114, 216, 242), (200, 200, 200), (255, 199, 241), (50, 50, 50)]
          # black 0    #red   1     #white    2      #light_blue 3    #gray   4        #light_pink  5   #dark_gray 6
moving_up = False
moving_down = False
moving_left = False
moving_right = False
gravity = 5


def collide(rect, rectangle_list):
    hit_list = []
    for rectangle in rectangle_list:
        if rect.colliderect(rectangle):
            hit_list.append(rectangle)
    return hit_list


def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

    rect.x += movement[0]
    hit_list = collide(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True

    rect.y += movement[1]
    hit_list = collide(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

player_rect = pygame.Rect(100, 51, 50, 50)
while True:
    screen.fill(colour[6])
    pygame.draw.polygon(screen, (255, 0, 255), [(300, 500), (300, 550), (250, 550)])

# ~~~~~~ List of rectangles
    rectlist = []
    small_rect = pygame.Rect(200, 200, 50, 50)
    bottomrect_1 = pygame.Rect(0, screensize[1] - 50, screensize[0], 50)
    bottomrect_2 = pygame.Rect(300, screensize[1] - 100, screensize[0], 50)
    D_rect = pygame.Rect(250, screensize[1] - 100, 50, 50)
    rectlist.append(small_rect)
    rectlist.append(bottomrect_1)
    rectlist.append(bottomrect_2)

# ~~~~~~ Player Movement
    player_movement = [0, 0]
    if moving_up:
        player_movement[1] -= 2
    if moving_down:
        player_movement[1] += 2
    if moving_left:
        player_movement[0] -= 2
    if moving_right:
        player_movement[0] += 2

    player_movement[1] += gravity

# ~~~~~~ Player Collision
    my_rect, collision = move(player_rect, player_movement, rectlist)







    # my attempt at this diagonal humbug. D_rect is the diagonal rect. (the slope)
    if my_rect.colliderect(D_rect):
        dia_height = D_rect.height * (my_rect.right-D_rect.left) / D_rect.width
        D_rect_top = D_rect.bottom - round(dia_height)
        my_rect.bottom = D_rect_top






# ~~~~~~ Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                gravity = -gravity

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    # ~~~~~~ Draw.
    pygame.draw.rect(screen, (0, 255, 125), D_rect, 1)
    pygame.draw.rect(screen, colour[3], small_rect)
    pygame.draw.rect(screen, colour[4], my_rect)
    pygame.draw.rect(screen, colour[5], bottomrect_1)
    pygame.draw.rect(screen, colour[5], bottomrect_2)
    pygame.display.update()
    clock.tick(60)