# pygame1.py
# A simple pygame program

import pygame

pygame.init()	# Initialized pygame module

# Screen size
width, height = 640, 480

screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.gif").convert()
ball_rect = ball.get_rect()

running = True
while running:
#    print 'looping'

    screen.fill((0, 0, 0))          # Redraw background
    screen.blit(ball, ball_rect)    # Draw ball to screen
    pygame.display.flip()           # Display screen in window
    ball_rect[0] += 1               # Move ball, 1 pixel right

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            # exit()
            running = False