# pygame1.py
# A simple pygame program

import pygame

pygame.init()   # Initialized pygame module

# Screen size
width, height = 640, 480

screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.gif").convert_alpha()
pygame.draw.circle(ball, pygame.Color('magenta'), (25, 25), 10)
ball_rect = ball.get_rect()

horizontal = 1
vertical = 3

running = True
while running:
#    print 'looping'

    screen.fill((0, 0, 0))          # Redraw background
    screen.blit(ball, ball_rect)    # Draw ball to screen
    pygame.display.flip()           # Display screen in window
    ball_rect[0] += horizontal      # Move ball, 1 pixel right
    ball_rect[1] += vertical        # Move ball, 1 pixel right

    if ball_rect.right >= width:
        horizontal = -1
    elif ball_rect.left <= 0:
        horizontal = 1
    if ball_rect.bottom >= height:
        vertical = -3
    elif ball_rect.top <= 0:
        vertical = 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            # exit()
            running = False