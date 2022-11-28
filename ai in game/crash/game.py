import pygame


pygame.init()
display=(1000,1000)
screen= pygame.display.set_mode(display)
dino=pygame.image.load('dino.png')
rect=dino.get_rect()
vel=10
obstacle=pygame.Rect(800,800,80,80)

def quit_game():
    global run
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

run=True
while run:
    quit_game()
    screen.fill((255,255,255))
    userInput= pygame.key.get_pressed()
    if userInput[pygame.K_LEFT]:
        rect.x -=vel
    if userInput[pygame.K_RIGHT]:
        rect.x +=vel
    if userInput[pygame.K_UP]:
        rect.y -=vel
    if userInput[pygame.K_DOWN]:
        rect.y +=vel

    screen.blit(dino, rect)
    pygame.draw.rect(screen,(0,0,0), obstacle, 4)
    if rect.colliderect(obstacle):
        pygame.draw.rect(screen, (255,0,0), rect, 4)
    
    pygame.display.flip()
    pygame.time.delay(30)