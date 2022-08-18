import sys
import pygame
pygame.init()
size = width, height = 1920, 1080
speed = [2, 2   ]
background = 255, 255, 255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing ball")
ball = pygame.image.load("ball.gif")

ballrect = ball.get_rect()

# rect
x = 20
y = 200
width = 20
height = 20
vel = 10

while 1:
    # pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # rect
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        x -= vel
    if keys[pygame.K_RIGHT] and x<500-width:
          
        # increment in x co-ordinate
        x += vel
         
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
          
        # decrement in y co-ordinate
        y -= vel
          
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and y<500-height:
        # increment in y co-ordinate
        y += vel
    # ball
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    screen.fill(background)
    screen.blit(ball, ballrect)
    pygame.display.flip()