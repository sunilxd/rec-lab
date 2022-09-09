import sys
import pygame
pygame.init()
size = width, height = 1920, 1080
speed = [2, 2]
background = 255, 255, 255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing ball")
ball = pygame.image.load("ball.gif")

ballrect = ball.get_rect()
font = pygame.font.Font('FreeSansBold.ttf', 32)

# rect
rec_width = 400
rec_height = 20
x = 0
y = 1000
vel = 10
score = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # rect
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        x -= vel
    if keys[pygame.K_RIGHT] and x<width-rec_width:
        x += vel

    
    # ball
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    cen = (ballrect.left+ballrect.right)/2
    if ballrect.bottom>1000:
        if (cen>=x and cen<=x+rec_width):
            speed[1] = -speed[1]
            score  += 1
            if score%2==0:
                speed[0] -= 1
                speed[1] += speed[1]//abs(speed[1])
        else:
            print('Score: ', score)
            sys.exit()

    #screen
    screen.fill(background)
    sc = font.render('Score: '+str(score),True, (0, 0, 0))
    screen.blit(sc, (100, 100))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, rec_width, rec_height))
    screen.blit(ball, ballrect)
    pygame.display.flip()