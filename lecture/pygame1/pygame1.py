# pygame1.py
# A simple pygame program

import pygame

width, height = 640, 480

def init():
    pygame.init()   # Initialized pygame module

    # Screen
    return pygame.display.set_mode((width, height))

def main(screen):
    # Load the image
    ball = pygame.image.load("ball.gif").convert_alpha()
    pygame.draw.circle(ball, pygame.Color('green'), (25, 25), 10)
    ball_rect = ball.get_rect()

    horizontal = 1
    vertical = 2

    running = True

    while running:
    #    print 'looping'

        screen.fill((0, 0, 0))          # Redraw background
        screen.blit(ball, ball_rect)    # Draw ball to screen
        pygame.display.flip()           # Display screen in window

        # Ball motion
        # ball_rect = ball_rect.move(horizontal, vertical)      Poor version, that makes new rectangles
        ball_rect.move_ip(horizontal, vertical)

        # Bounds checking
        if ball_rect.right >= width or ball_rect.left <= 0:
            horizontal *= -1
        if ball_rect.bottom >= height or ball_rect.top <= 0:
            vertical *= -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # exit()
                running = False


screen = init()
main(screen)