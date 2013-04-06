# pygame1.py
# A simple pygame program

import pygame

width, height = 640, 480

<<<<<<< HEAD
screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.gif").convert()
# pygame.draw.circle(ball, pygame.Color('magenta'), (25, 25), 10)
ball_rect = ball.get_rect()
print 'ball_rect', ball_rect

ball2 = ball.copy()
ball2_rect = ball2.get_rect()

horizontal = 1
vertical = 3
spin = 30

clock = pygame.time.Clock()

running = True
while running:
#    print 'looping'

    screen.fill((0, 0, 0))          # Redraw background
    screen.blit(ball, ball_rect)    # Draw ball to screen
    # screen.blit(ball2, (0, 0), ball2_rect)
    pygame.display.flip()           # Display screen in window
    ball_rect.move_ip(horizontal, vertical)

    # Move the ball
    if ball_rect.right >= width:
        horizontal = -1
    elif ball_rect.left <= 0:
        horizontal = 1
    if ball_rect.bottom >= height:
        vertical = -3
    elif ball_rect.top <= 0:
        vertical = 3

    # # Rotate the ball
    spun = pygame.transform.rotate(ball, spin)
    spun_rect = spun.get_rect()
    shrink = ball_rect.width - spun_rect.width
    spun_rect.inflate_ip(shrink, shrink)
    # ball2.fill((0, 0, 0))
    ball.blit(spun, (0, 0), spun_rect)
    # print spun_rect
    # pygame.display.flip()           # Display screen in window
    # ball2_rect = ball2.get_rect()
    # shrink = ball_rect.width - ball2_rect.width
    # ball2_rect.inflate_ip(shrink, shrink)
    # ball2.blit(ball2, ball2_rect)
    # print 'ball2_rect', ball2_rect
    # ball_rect = ball.get_rect()
    # deflate = ball_rect.width - ball2_rect.width
    # ball2_rect.inflate_ip(deflate, deflate)
    # # print offset
    # # ball.fill((0, 0, 0))
    # ball.blit(ball2, (0, 0), ball2_rect)

    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            # exit()
            running = False
=======
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
>>>>>>> 84d0211154a1133528966662a4d5759e54efc531
