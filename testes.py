import sys, pygame
pygame.init()

size = width, height = 2000, 2000
speed = [2, 2]
black = 1, 1, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Assets/flaps.png")
IMAGE_SMALL = pygame.transform.scale(ball, (100, 100))
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(IMAGE_SMALL, ballrect)
    pygame.display.flip()